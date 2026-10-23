# dotfiles

My [niri](https://github.com/YaLTeR/niri) setup. It runs next to GNOME rather
than replacing it, so Wi-Fi, Bluetooth and sound still go through GNOME
Settings. Look inspired by [saneAspect](https://www.youtube.com/@saneAspect).

| | |
| --- | --- |
| ![Desktop with the calendar open](screenshots/desktop.png) | ![Fastfetch](screenshots/fastfetch.png) |
| ![Launcher](screenshots/launcher.png) | ![Notification](screenshots/notification.png) |
| ![Power menu](screenshots/powermenu.png) | ![Keyboard shortcuts](screenshots/shortcuts.png) |

I use it on Fedora 44 with niri 26.04 on an Acer laptop. It should work on any
distro that has GNOME installed.

## Install

Fedora:

```sh
sudo dnf install niri waybar fuzzel alacritty mako gtklock swayidle swaybg \
    wlogout mate-polkit wl-clipboard cliphist wlsunset playerctl \
    brightnessctl ImageMagick libnotify adwaita-sans-fonts tmux swappy \
    fastfetch stow git
```

Arch (untested):

```sh
sudo pacman -S niri waybar fuzzel alacritty mako swayidle swaybg \
    mate-polkit wl-clipboard cliphist wlsunset playerctl brightnessctl \
    imagemagick libnotify adwaita-fonts ttf-jetbrains-mono-nerd \
    xwayland-satellite power-profiles-daemon tmux swappy fastfetch stow git
yay -S gtklock wlogout
```

On Fedora you also need
[JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip)
in `~/.local/share/fonts/` (run `fc-cache -f` after), otherwise the bar icons
are empty boxes.

Then link the configs with [Stow](https://www.gnu.org/software/stow/):

```sh
git clone https://github.com/vishwajitsarnobat/dotfiles.git ~/dotfiles
cd ~/dotfiles
stow niri waybar fuzzel alacritty mako gtklock wlogout swappy fastfetch \
    applications environment scripts
```

Stow won't overwrite configs you already have, so move those out of the way
first. Pick only the packages you want, but keep `scripts`: most of the others
call into it.

A few extras:

```sh
# wallpaper (also used, blurred, for the lock screen)
setwall ~/Pictures/Wallpapers/something.png

# open files with GNOME's default apps
sudo ln -s /usr/share/applications/gnome-mimeapps.list \
    /usr/share/applications/niri-mimeapps.list

# lock instead of suspending when the lid closes (optional)
sudo install -Dm644 system/etc/systemd/logind.conf.d/10-lid-lock.conf \
    /etc/systemd/logind.conf.d/10-lid-lock.conf
sudo systemctl reload systemd-logind
```

Log out, pick niri at the login screen, and press `Mod + Shift + /` for the
list of keys.

## Keys

`Mod` is the Super key. Window and workspace keys are niri's defaults.

| | |
| --- | --- |
| `Mod + T` / `D` / `E` | terminal / launcher / files |
| ``Mod + ` `` | drop-down terminal |
| `Mod + Tab` | switch window |
| `Mod + Q` | close window (or an open popup) |
| `Mod + Shift + /` | all keys |
| `Print` | screenshot an area (`Space` to take it) |
| `Shift + Print` | screenshot an area and annotate it |
| `Ctrl + Print` / `Alt + Print` | screenshot the screen / window |

System stuff is all on `Mod + Alt`:

| | |
| --- | --- |
| `W` / `B` / `S` | Wi-Fi / Bluetooth / sound settings |
| `C` | calendar |
| `H` | notification history |
| `V` | clipboard history |
| `D` | do not disturb |
| `K` | keep awake |
| `E` | power profile |
| `N` | night light |
| `T` | light / dark apps |
| `R` | start / stop OBS recording |
| `L` | lock |
| `P` | power menu |

## Notes

- Bar icons are blue when on and grey when off. Hover one to see what
  clicking does.
- The screen locks after 15 minutes idle and always before sleep. Keep awake
  turns the idle lock off.
- The drop-down terminal runs in tmux, so hiding it doesn't lose anything.
- For `Mod + Alt + R` to stop a recording, enable OBS's WebSocket server
  (Tools → WebSocket Server Settings).
- GNOME Settings refuses to start outside GNOME, so `applications` and
  `settings-panel` start it with `XDG_CURRENT_DESKTOP=GNOME`.

Laptop-specific bits you may want to drop:

- `XF86Launch6` in the niri config is my laptop's mic-mute key.
- `environment/` sets `GSK_RENDERER=ngl` so GTK 4 apps don't wake the NVIDIA
  GPU and start slowly.
- On a desktop, remove `battery` from the Waybar config.

## Changing things

Most of it is in `niri/.config/niri/config.kdl` (keys, gaps, window rules,
animations) and `waybar/.config/waybar/` (bar). Keys with a
`hotkey-overlay-title` show up in the `Mod + Shift + /` list on their own.
The accent colour is `#8fb8f6`; grep for it to change it everywhere.

If the lock screen ever gets stuck, switch to another console with
`Ctrl + Alt + F3`, log in and run `WAYLAND_DISPLAY=wayland-1 gtklock`, then go
back with `Ctrl + Alt + F2` and unlock.

## Credits

Wallpaper from [typecraft](https://github.com/typecraft-dev/dotfiles), power
menu icons from [Feather](https://feathericons.com), icon font from
[Nerd Fonts](https://www.nerdfonts.com).
