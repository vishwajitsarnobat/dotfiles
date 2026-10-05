# dotfiles

My [niri](https://github.com/YaLTeR/niri) setup on Fedora, alongside GNOME.
Dark GNOME greys, soft pastel accents, one blue focus colour, and rounded
"island" bars, inspired by [saneAspect](https://www.youtube.com/@saneAspect).

| | |
| --- | --- |
| ![Desktop](screenshots/desktop.png) | ![Fastfetch](screenshots/fastfetch.png) |
| ![Launcher](screenshots/launcher.png) | ![Calendar](screenshots/calendar.png) |
| ![Notification](screenshots/notification.png) | ![Power menu](screenshots/powermenu.png) |

## What's inside

Each folder is a [GNU Stow](https://www.gnu.org/software/stow/) package.

| Folder | App | What it does |
| --- | --- | --- |
| `niri` | [niri](https://github.com/YaLTeR/niri) | Scrolling tiling window manager: keys, gaps, borders, window rules |
| `waybar` | [Waybar](https://github.com/Alexays/Waybar) | Top bar: three rounded islands |
| `fuzzel` | [fuzzel](https://codeberg.org/dnkl/fuzzel) | App launcher |
| `alacritty` | [Alacritty](https://alacritty.org) | Terminal |
| `mako` | [mako](https://github.com/emersion/mako) | Notifications + volume/brightness popup |
| `swaylock` | [swaylock](https://github.com/swaywm/swaylock) | Lock screen over a blurred wallpaper |
| `wlogout` | [wlogout](https://github.com/ArtsyMacaw/wlogout) | Power menu |
| `scripts` | — | Small helper commands (see below) |

**Fonts:** Adwaita Sans for interface text, JetBrainsMono Nerd Font for the
terminal, icons and the calendar.

## Install

Tested on Fedora 44 with niri 26.04.

**1. Packages**

```sh
sudo dnf install niri waybar fuzzel alacritty mako swaylock swayidle swaybg \
    wlogout mate-polkit wl-clipboard cliphist wlsunset playerctl \
    brightnessctl ImageMagick libnotify adwaita-sans-fonts stow git
```

**2. Font:** download
[JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip),
unzip it into `~/.local/share/fonts/`, then run `fc-cache -f`.

**3. Configs**

```sh
git clone https://github.com/vishwajitsarnobat/dotfiles.git ~/dotfiles
cd ~/dotfiles
stow niri waybar fuzzel alacritty mako swaylock wlogout scripts
```

If a config already exists (for example `~/.config/niri`), Stow stops
instead of overwriting it. Move the old one away and run `stow` again.

**4. Wallpaper:** save any image and run `setwall path/to/image`. The one in
the screenshots is typecraft's
[`nice-blue-background.png`](https://github.com/typecraft-dev/dotfiles/tree/master/backgrounds/.config/backgrounds).

**5. Default apps** (so images open in Image Viewer instead of a browser).
This lets niri use GNOME's default apps:

```sh
sudo ln -s /usr/share/applications/gnome-mimeapps.list /usr/share/applications/niri-mimeapps.list
```

Log out and pick **niri** on the login screen.

## Keys

`Mod` is the Super / Windows key.

| Key | Action |
| --- | --- |
| `Mod + T` | Terminal |
| `Mod + D` | App launcher |
| `Mod + E` | Files |
| `Mod + Q` | Close window |
| `Mod + Alt + V` | Clipboard history |
| `Mod + N` | Clear all notifications |
| `Mod + Shift + T` | Switch apps between light / dark |
| `Mod + Alt + L` | Lock screen |
| `Mod + Shift + E` | Power menu |
| `Mod + Shift + /` | Show all keys |

Window, workspace and monitor keys are niri's defaults.

## The bar

| Island | Contents |
| --- | --- |
| **Left** | Workspaces · now playing (click: play/pause, right-click: next, hover: song and source) |
| **Centre** | Date and time (hover: calendar, scroll: change month, click: back to today) · current window |
| **Right** | Tray · keep awake · do not disturb · volume · Wi-Fi · Bluetooth · battery · power menu |

Volume, Wi-Fi, Bluetooth and battery open the matching GNOME Settings page
when clicked. Right-click volume to mute.

## Helper commands

All live in `scripts/.local/bin`.

| Command | What it does |
| --- | --- |
| `setwall <image>` | Set the wallpaper (run alone to list saved ones) |
| `theme [light\|dark]` | Switch apps between light and dark, like GNOME's switch |
| `lockscreen` | Lock with a blurred copy of the wallpaper |
| `powermenu` | Open the power menu, sized to the screen |
| `volume`, `brightness`, `osd` | Media keys in 5% steps with a level popup |
| `waybar-calendar`, `waybar-media` | The bar's calendar and now-playing |
| `dnd-status`, `dnd-toggle` | Do-not-disturb button |

**Night light** is manual: `wlsunset -t 4000 -T 4001 &` to turn it on,
`pkill wlsunset` to turn it off.

**Auto lock:** the screen locks after 5 minutes idle. Once locked, the
display turns off after 15 seconds.

## Credits

- [saneAspect](https://www.youtube.com/@saneAspect): style inspiration
- [typecraft](https://github.com/typecraft-dev/dotfiles): wallpaper
- [Feather icons](https://feathericons.com) (MIT): power menu icons
- [Nerd Fonts](https://www.nerdfonts.com): JetBrainsMono Nerd Font
