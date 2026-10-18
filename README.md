# dotfiles

A calm, keyboard-first [niri](https://github.com/YaLTeR/niri) desktop that
sits alongside GNOME instead of replacing it. Dark GNOME greys,
one blue accent, rounded "island" bars, and GNOME's own Settings for Wi-Fi,
Bluetooth and sound. Style inspired by
[saneAspect](https://www.youtube.com/@saneAspect).

| | |
| --- | --- |
| ![Desktop with the calendar open](screenshots/desktop.png) | ![Fastfetch](screenshots/fastfetch.png) |
| ![Launcher](screenshots/launcher.png) | ![Notification](screenshots/notification.png) |
| ![Power menu](screenshots/powermenu.png) | ![Keyboard shortcuts](screenshots/shortcuts.png) |

## What you get

- **Window manager:** niri, with scrolling columns of windows, rounded
  corners, a blue border on the focused window, and 8px gaps.
- **Bar:** a top bar in three islands. Workspaces and now playing on the
  left, the clock and a calendar in the centre, status icons on the right.
- **System keys:** one easy-to-remember set, `Mod + Alt + <letter>`, for
  Wi-Fi, Bluetooth, sound, power profiles, do not disturb, lock and more.
- **GNOME underneath:** no extra Wi-Fi, Bluetooth or volume apps. Clicking
  the bar opens the matching GNOME Settings page, and clicking again closes it.
- **Matching look everywhere:** the launcher, terminal, notifications, lock
  screen and power menu all use the same colours.
- **Quick tools:** a drop-down terminal, a window switcher, clipboard and
  notification history, screenshot annotation, and a key to start or stop an
  OBS recording.
- **Small touches:** a volume and brightness popup, a low-battery warning,
  night light, keep-awake, do not disturb, and one key to switch apps between
  light and dark.

## Before you start

- **Any Linux distro with GNOME.** I use and test it on Fedora 44 with niri
  26.04, but nothing in it is Fedora-only. GNOME must stay installed, because
  Settings, Files and the GNOME apps come from it. You can still log in to
  plain GNOME whenever you like.
- **A laptop is assumed.** The bar shows battery, and the brightness keys are
  bound. On a desktop, see [Hardware-specific bits](#hardware-specific-bits).
- **Some parts are specific to my laptop**, an Acer Aspire A514-56GM with
  Intel and NVIDIA graphics. They're harmless elsewhere, but you can drop
  them. See [Hardware-specific bits](#hardware-specific-bits).

## Install

**1. Install the packages.** On Fedora:

```sh
sudo dnf install niri waybar fuzzel alacritty mako gtklock swayidle swaybg \
    wlogout mate-polkit wl-clipboard cliphist wlsunset playerctl \
    brightnessctl ImageMagick libnotify adwaita-sans-fonts tmux swappy \
    fastfetch stow git
```

On Arch (not tested by me). `gtklock` and `wlogout` go through an AUR helper
such as `yay`, which also installs them from the official repos if they're
there:

```sh
sudo pacman -S niri waybar fuzzel alacritty mako swayidle swaybg \
    mate-polkit wl-clipboard cliphist wlsunset playerctl brightnessctl \
    imagemagick libnotify adwaita-fonts ttf-jetbrains-mono-nerd \
    xwayland-satellite power-profiles-daemon tmux swappy fastfetch stow git
yay -S gtklock wlogout    # or your AUR helper of choice
```

This also installs the icon font, so you can skip step 2.

On another distro, install the same programs with its package manager.
Names are mostly the same, with a few exceptions:

| Program | What it's for | Notes |
| --- | --- | --- |
| `niri`, `waybar`, `fuzzel`, `alacritty`, `mako` | Window manager, bar, launcher, terminal, notifications | |
| `gtklock`, `swayidle`, `swaybg`, `wlogout` | Lock screen, idle timers, wallpaper, power menu | Install `gtklock` and `wlogout` with your AUR helper on Arch |
| `mate-polkit` | Password prompts for admin actions | Any polkit agent works; change its line in the niri config |
| `wl-clipboard`, `cliphist` | Clipboard and clipboard history | |
| `wlsunset` | Night light | |
| `playerctl`, `brightnessctl` | Media keys, brightness keys | |
| `ImageMagick`, `libnotify` | Blurred lock screen, popups | `imagemagick` on Arch and Debian |
| Adwaita Sans font | Interface text | `adwaita-fonts` on Arch |
| `tmux` | Keeps the drop-down terminal's session alive while hidden | |
| `swappy` | Annotating screenshots | Optional |
| `fastfetch` | System info in the terminal | Optional |
| `obs-studio` | Screen recording with `Mod + Alt + R` | Optional |
| `stow`, `git` | Installing these dotfiles | |
| `xwayland-satellite` | Older X11 apps | Usually pulled in with niri |
| `power-profiles-daemon` or `tuned-ppd` | Power profiles | Most GNOME installs already have one |

**2. Install the icon font.** Download
[JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip),
unzip it into `~/.local/share/fonts/`, then run `fc-cache -f`. Some distros
package it (`ttf-jetbrains-mono-nerd` on Arch). Without it, the bar's icons
show up as empty boxes.

**3. Link the configs.** Each folder in this repo is a
[GNU Stow](https://www.gnu.org/software/stow/) package. Stow links its files
into your home folder, so editing the repo edits your live config.

```sh
git clone https://github.com/vishwajitsarnobat/dotfiles.git ~/dotfiles
cd ~/dotfiles
stow niri waybar fuzzel alacritty mako gtklock wlogout swappy fastfetch \
    applications environment scripts
```

If you already have one of these configs (for example `~/.config/niri`),
Stow stops instead of overwriting it. Move yours away, for example
`mv ~/.config/niri ~/.config/niri.bak`, and run `stow` again.

You can install only some packages, but always include `scripts`: niri, the
bar and the power menu all call the commands in it.

**4. Set a wallpaper.** Put your images in `~/Pictures/Wallpapers/` and run
`setwall ~/Pictures/Wallpapers/<image>`. Run `setwall` on its own to list
them. Until you set one, the background is plain dark grey. The wallpaper in
the screenshots is typecraft's
[`nice-blue-background.png`](https://github.com/typecraft-dev/dotfiles/tree/master/backgrounds/.config/backgrounds).

**5. Use GNOME's default apps in niri.** Without this, images and PDFs may
open in the wrong app. If your distro has
`/usr/share/applications/gnome-mimeapps.list` (Fedora does), link it for
niri:

```sh
sudo ln -s /usr/share/applications/gnome-mimeapps.list /usr/share/applications/niri-mimeapps.list
```

If that file doesn't exist, skip this step and set default apps in GNOME
Settings → Apps → Default Apps.

**6. Log in.** Log out, choose **niri** on the login screen, and log in.
Press `Mod + Shift + /` any time for a card with every key, grouped by what
it does.

## Everyday use

`Mod` is the Super (Windows) key.

### The keys you need first

| Key | Action |
| --- | --- |
| `Mod + T` | Terminal |
| `Mod + D` | App launcher |
| `Mod + E` | Files |
| ``Mod + ` `` | Drop-down terminal: show, or hide if it's in front |
| `Mod + Tab` | Switch window: type to search, `Enter` to jump. The window you were just on is first |
| `Mod + Q` | Close window (or an open calendar / shortcuts card) |
| `Mod + Left / Right` (or `H / L`) | Move between columns |
| `Mod + Up / Down` (or `K / J`) | Move between windows in a column |
| `Mod + 1 … 9` | Go to a workspace |
| `Mod + Ctrl + 1 … 9` | Move the window to a workspace |
| `Mod + R` | Cycle the window width: ⅓, ½, ⅔ |
| `Mod + F` | Make the column full width |
| `Mod + O` | Overview of all windows |
| `Mod + Shift + /` | Keyboard shortcuts card |

The window, workspace and monitor keys are niri's defaults, so niri's own
documentation applies.

### System keys: `Mod + Alt + <letter>`

Most are toggles: press again to undo.

| Key | Action |
| --- | --- |
| `Mod + Alt + W` | Wi-Fi settings |
| `Mod + Alt + B` | Bluetooth settings |
| `Mod + Alt + S` | Sound settings |
| `Mod + Alt + D` | Do not disturb |
| `Mod + Alt + K` | Keep awake (don't lock when idle) |
| `Mod + Alt + E` | Next power profile: power saver, balanced, performance |
| `Mod + Alt + N` | Night light |
| `Mod + Alt + T` | Switch apps between light and dark |
| `Mod + Alt + C` | Calendar (press again to close) |
| `Mod + Alt + H` | Notification history (pick one to copy its text) |
| `Mod + Alt + R` | Start or stop recording in OBS |
| `Mod + Alt + V` | Clipboard history |
| `Mod + Alt + L` | Lock screen |
| `Mod + Alt + P` | Power menu |

Volume, mic mute, brightness and media keys work as usual, even on the lock
screen, and show a small level popup.

### Screenshots

Every screenshot is saved to `~/Pictures/Screenshots/` and copied to the
clipboard, ready to paste.

| Key | Action |
| --- | --- |
| `Print` | Select an area |
| `Shift + Print` | Select an area, then annotate it |
| `Ctrl + Print` | Whole screen, instantly |
| `Alt + Print` | Focused window, instantly |

**While selecting an area** (`Print` or `Shift + Print`):

| Key | Action |
| --- | --- |
| Drag with the mouse | Draw the selection; drag its edges to adjust |
| `Space` | Take the screenshot |
| `P` | Show or hide the mouse pointer in it |
| `Esc` | Cancel |

**Annotating** opens the selection in swappy. Pick a tool from its toolbar
(arrow, rectangle, text, highlighter, blur), then press `Ctrl + S` to save
or `Ctrl + C` to copy. Either one closes the editor.

### The bar

| Island | What's there |
| --- | --- |
| **Left** | Workspaces · now playing (click: play/pause, right-click: next) |
| **Centre** | Date and time (click: calendar) · current window |
| **Right** | Tray · keep awake · do not disturb · microphone · volume · Wi-Fi · Bluetooth · power profile · battery · power |

Hover over any icon to see what its clicks do. The colours follow one rule:
**blue means on, grey means off**. Every crossed-out icon (muted,
disconnected, do not disturb) is grey. Battery is green, turning yellow and
then pink when low.

### Calendar and shortcuts cards

Tap the clock or press `Mod + Alt + C` for a calendar card under the bar.
Scroll, use the arrows, or press `←` / `→` to change month; the dot or `T`
jumps back to today. The footer shows today's date and week number.

`Mod + Shift + /` opens a card with every key, grouped by what it does.

Both work like GNOME's menus: they take the keyboard as soon as they open,
and `Esc`, a click anywhere outside, the same key (or tap) again, or
`Mod + Q` closes them. Only one is open at a time.

### Locking and sleep

- **Lock screen:** a big clock and date over your blurred wallpaper. Just start
  typing: the password field appears with your first key already in it, then
  press `Enter`.
- **Auto lock:** the screen locks after 15 minutes idle, and the display
  turns off 15 seconds after that.
- **Before sleep:** the screen always locks, even with keep-awake on.
- **Keep awake:** turns off the idle lock until you turn it back off, for
  example while watching a video.
- **Low battery:** a notification at 15%, and a second one at 5% that stays
  up, even with do not disturb on.

### Drop-down terminal

`` Mod + ` `` brings up a floating terminal near the top of the screen, over
whatever you're doing, without changing your layout. Press it again to hide
it. Hiding doesn't end anything: the shell keeps running in tmux, so the next
time you open it, your commands and their output are still there.

### Recording with OBS

`Mod + Alt + R` starts OBS in the tray and begins recording if OBS isn't
running. If it is, the key starts or stops recording. For the second case,
turn on OBS's remote control once: in OBS, open **Tools → WebSocket Server
Settings** and tick **Enable WebSocket server**. The key reads the password
from OBS's own settings, so there's nothing to copy.

## Make it yours

Changes apply as soon as you save the file, except where the notes say
otherwise.

| To change | Edit | Notes |
| --- | --- | --- |
| Keys | `niri/.config/niri/config.kdl`, `binds { }` | Give a new key a `hotkey-overlay-title="…"` and it shows up in the shortcuts card by itself |
| Gaps, borders, corner radius | `niri/.config/niri/config.kdl`, `layout { }` and the first `window-rule` | The negative `struts` make the screen edges 4px while gaps between windows stay 8px |
| Apps that open floating | `niri/.config/niri/config.kdl`, "Small pop-up windows float" | Find an app's ID with `niri msg windows` |
| Monitor layout and scaling | `niri/.config/niri/config.kdl` | Add an `output` block; run `niri msg outputs` to get names |
| Bar icons and their order | `waybar/.config/waybar/config.jsonc`, `modules-right` | Restart the bar: `pkill waybar; waybar &` |
| Bar colours and sizes | `waybar/.config/waybar/style.css` | Colours are defined at the top; restart the bar |
| Bar clock format | `waybar/.config/waybar/config.jsonc`, `clock` | 12-hour by default; restart the bar |
| Calendar look, week start | `scripts/.local/bin/calendar-popup` | Sunday-first by default (`FIRST_WEEKDAY`) |
| Idle and lock timers | `scripts/.local/bin/idle-watch` | In seconds; log in again to apply |
| Lock screen look, clock format | `gtklock/.config/gtklock/style.css`, `config.ini` | Takes effect the next time you lock |
| Night light warmth | `niri/.config/niri/config.kdl`, the `Mod+Alt+N` line | `-t 4000` is the colour temperature in kelvin |
| Notification timeout | `mako/.config/mako/config`, `default-timeout` | In ms; run `makoctl reload` |
| Animation speed | `niri/.config/niri/config.kdl`, `animations { }` | Lower `stiffness` and longer `duration-ms` are slower |
| See-through unfocused windows | `niri/.config/niri/config.kdl`, the `is-focused=false` rule | `opacity 1.0` turns it off |
| Drop-down terminal size and position | `niri/.config/niri/config.kdl`, the `dropterm` rule | |
| Low-battery levels | `scripts/.local/bin/battery-watch` | Log in again to apply |
| Terminal font and colours | `alacritty/.config/alacritty/alacritty.toml` | |
| Wallpaper folder | `scripts/.local/bin/setwall`, `WDIR` | |

### Colours

Everything uses one small palette:

| Role | Colour |
| --- | --- |
| Background | `#1e1e22` |
| Raised surface (cards, notifications) | `#2b2b33` |
| Text | `#f2f2f5` |
| Grey (off, inactive) | `#6b6b76` |
| Accent (focus, on) | `#8fb8f6` |
| Pink (urgent, power) | `#f2a1a8` |
| Yellow (warning) | `#f3d98b` |
| Green (battery) | `#a6dba0` |

The accent appears in about a dozen files, including the power menu icons.
To swap it everywhere at once:

```sh
cd ~/dotfiles
grep -rl 8fb8f6 --exclude-dir=.git . | xargs sed -i 's/8fb8f6/YOURHEX/g'
```

Also update the `rgba(143, 184, 246, …)` line in
`waybar/.config/waybar/style.css`: it's the same blue, written as RGB values.

### Hardware-specific bits

| What | Where | Keep it if… |
| --- | --- | --- |
| `XF86Launch6` key bound to mic mute | `niri/.config/niri/config.kdl` | Your mic-mute key does nothing otherwise. Run `wev` and press it to see its name. |
| `GSK_RENDERER=ngl` | `environment/.config/environment.d/gtk.conf` | You have NVIDIA graphics. GTK 4 apps then skip waking the NVIDIA GPU, which saves a few seconds on the first launch. Harmless elsewhere. |
| Battery icon, brightness keys | `waybar/.config/waybar/config.jsonc`, `niri/.config/niri/config.kdl` | You're on a laptop. On a desktop, remove `battery` from `modules-right`. |

## How it fits together

| Folder | App | What it does |
| --- | --- | --- |
| `niri` | [niri](https://github.com/YaLTeR/niri) | Window manager: keys, layout, window rules, startup apps |
| `waybar` | [Waybar](https://github.com/Alexays/Waybar) | Top bar |
| `fuzzel` | [fuzzel](https://codeberg.org/dnkl/fuzzel) | App launcher, also used for clipboard history |
| `alacritty` | [Alacritty](https://alacritty.org) | Terminal |
| `fastfetch` | [fastfetch](https://github.com/fastfetch-cli/fastfetch) | System info in the same colours |
| `swappy` | [swappy](https://github.com/jtheoof/swappy) | Screenshot annotation |
| `mako` | [mako](https://github.com/emersion/mako) | Notifications, the level popup, do not disturb |
| `gtklock` | [gtklock](https://github.com/jovanlanik/gtklock) | Lock screen: a big clock and date over a blurred copy of the wallpaper |
| `wlogout` | [wlogout](https://github.com/ArtsyMacaw/wlogout) | Power menu |
| `applications` | — | Makes GNOME Settings open from the launcher in niri (it normally refuses to start outside GNOME) |
| `environment` | systemd | Session-wide settings for both niri and GNOME |
| `scripts` | — | The helper commands below, in `~/.local/bin`, plus `popup.py` in `~/.local/lib/dotfiles`, shared by the two cards |

Helper commands, which you can also run yourself in a terminal:

| Command | What it does |
| --- | --- |
| `setwall <image>` | Set the wallpaper (run alone to list saved ones) |
| `theme [light\|dark]` | Switch apps between light and dark, including older GTK 3 apps |
| `lockscreen` | Lock the screen |
| `powermenu` | Open or close the power menu |
| `volume`, `brightness` | Change volume or brightness in 5% steps and show the popup |
| `keep-awake [toggle]` | Show or switch keep-awake |
| `power-profile [name]` | Switch to the next power profile, or to `power-saver`, `balanced` or `performance` |
| `dnd-toggle`, `dnd-status` | Switch or show do not disturb |
| `settings-panel <page>` | Open or close a GNOME Settings page: `wifi`, `bluetooth`, `sound`, `power` |
| `dropterm` | Show or hide the drop-down terminal |
| `window-switcher` | The `Mod + Tab` window list |
| `notif-history` | The notification history list |
| `obs-record` | Start or stop an OBS recording |
| `screenshot-annotate` | Select an area, then open it in swappy |
| `idle-watch [awake]` | The idle timers, started by niri at login |
| `battery-watch` | The low-battery warnings, started by niri at login |
| `calendar-popup` | Open or close the calendar card |
| `keys-popup` | Open or close the keyboard shortcuts card |
| `close-focused` | `Mod + Q`: close an open card, otherwise the focused window |
| `osd`, `lockscreen-bg`, `waybar-media` | Used internally by the commands above |

## Troubleshooting

- **Icons show as empty boxes:** the Nerd Font isn't installed, or
  `fc-cache -f` wasn't run. See step 2.
- **`stow` reports a conflict:** you already have that config. Move it away
  and run `stow` again.
- **Settings keys or bar clicks do nothing:** GNOME Settings
  (`gnome-control-center`) isn't installed. Install it with your package
  manager; it comes with any full GNOME install.
- **Power profile icon is missing or does nothing:** neither
  `power-profiles-daemon` nor `tuned-ppd` is running. Install one and enable
  its service.
- **No password prompt when an app needs admin rights:** the polkit agent
  didn't start. Check that `mate-polkit` is installed, or point the niri
  config's polkit line at your distro's agent.
- **Changes to `environment`, `idle-watch` or `battery-watch` don't apply:**
  they're read at login. Log out and back in.
- **The lock screen is stuck or blank:** switch to a text console with
  `Ctrl + Alt + F3`, log in, run `WAYLAND_DISPLAY=wayland-1 gtklock`, then
  go back with `Ctrl + Alt + F2` and unlock. (Your session's console number
  may differ; `loginctl` shows it.)
- **`Mod + Alt + R` says it can't reach OBS:** OBS's WebSocket server is off.
  See [Recording with OBS](#recording-with-obs).

## Removing it

```sh
cd ~/dotfiles
stow -D niri waybar fuzzel alacritty mako gtklock wlogout swappy fastfetch \
    applications environment scripts
```

This removes only the links. Your own files, wallpapers and screenshots stay.

## Credits

- [saneAspect](https://www.youtube.com/@saneAspect): style inspiration
- [typecraft](https://github.com/typecraft-dev/dotfiles): wallpaper
- [Feather icons](https://feathericons.com) (MIT): power menu icons
- [Nerd Fonts](https://www.nerdfonts.com): JetBrainsMono Nerd Font
