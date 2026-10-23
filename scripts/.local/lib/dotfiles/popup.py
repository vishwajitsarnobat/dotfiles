# Shared code for calendar-popup and keys-popup. One popup at a time; it grabs
# the keyboard, and Esc, a click outside, running it again or Mod+Q
# (close-focused) closes it. An invisible full-screen layer catches the clicks.
import os, signal, sys

NAMES = ("calendar-popup", "keys-popup")
RUNTIME = os.environ.get("XDG_RUNTIME_DIR", "/tmp")


def _pidfile(name):
    return os.path.join(RUNTIME, f"{name}.pid")


def _running(name):
    """The pid of this popup if it's open (and not a reused pid), else None."""
    try:
        pid = int(open(_pidfile(name)).read())
        if name.encode() in open(f"/proc/{pid}/cmdline", "rb").read():
            return pid
    except (OSError, ValueError):
        pass
    return None


def close_all():
    """Close every open popup. True if one was open."""
    closed = False
    for name in NAMES:
        pid = _running(name)
        if pid:
            os.kill(pid, signal.SIGTERM)
            closed = True
    return closed


def claim(name):
    """Toggle: if this popup is open, close it and exit. Otherwise close any
    other popup and register this process as the open one."""
    if _running(name):
        close_all()
        sys.exit(0)
    close_all()
    with open(_pidfile(name), "w") as f:
        f.write(str(os.getpid()))


BASE_CSS = b"""
* { font-family: "Adwaita Sans"; }
window { background: transparent; }
#card {
    background: rgba(30, 30, 34, 0.97);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35);
}
"""


def run(name, build_card, css=b"", valign="center", top=0, on_key=None, on_scroll=None):
    """Show the card returned by build_card() until it's dismissed."""
    import gi
    gi.require_version("Gtk", "3.0")
    gi.require_version("Gdk", "3.0")
    gi.require_version("GtkLayerShell", "0.1")
    from gi.repository import Gdk, GLib, Gtk, GtkLayerShell

    win = Gtk.Window()
    GtkLayerShell.init_for_window(win)
    GtkLayerShell.set_namespace(win, name)
    GtkLayerShell.set_layer(win, GtkLayerShell.Layer.OVERLAY)
    for edge in (GtkLayerShell.Edge.TOP, GtkLayerShell.Edge.BOTTOM,
                 GtkLayerShell.Edge.LEFT, GtkLayerShell.Edge.RIGHT):
        GtkLayerShell.set_anchor(win, edge, True)
    GtkLayerShell.set_exclusive_zone(win, -1)          # cover the bar too
    GtkLayerShell.set_keyboard_mode(win, GtkLayerShell.KeyboardMode.EXCLUSIVE)

    screen = Gdk.Screen.get_default()
    win.set_visual(screen.get_rgba_visual())
    provider = Gtk.CssProvider()
    provider.load_from_data(BASE_CSS + css)
    Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

    def quit(*_):
        try:
            if _running(name) == os.getpid():
                os.remove(_pidfile(name))
        except OSError:
            pass
        Gtk.main_quit()
        return False

    backdrop = Gtk.EventBox()
    backdrop.connect("button-press-event", quit)
    win.add(backdrop)

    card_box = Gtk.EventBox(halign=Gtk.Align.CENTER, valign=getattr(Gtk.Align, valign.upper()))
    card_box.set_margin_top(top)
    card_box.set_visible_window(False)      # don't clip the card's shadow at the box edge
    card_box.connect("button-press-event", lambda *_: True)
    if on_scroll:
        card_box.add_events(Gdk.EventMask.SCROLL_MASK | Gdk.EventMask.SMOOTH_SCROLL_MASK)
        card_box.connect("scroll-event", lambda _w, e: on_scroll(e, Gdk) or True)
    card_box.add(build_card())
    backdrop.add(card_box)

    def key(_w, event):
        if Gdk.keyval_name(event.keyval) == "Escape":
            return quit()
        if on_key:
            on_key(Gdk.keyval_name(event.keyval))
        return True

    win.connect("key-press-event", key)
    win.connect("destroy", quit)
    try:
        gi.require_version("GLibUnix", "2.0")
        from gi.repository import GLibUnix
        GLibUnix.signal_add(GLib.PRIORITY_DEFAULT, signal.SIGTERM, quit)
    except (ImportError, ValueError):                  # older GLib
        GLib.unix_signal_add(GLib.PRIORITY_DEFAULT, signal.SIGTERM, quit)
    win.show_all()
    Gtk.main()
