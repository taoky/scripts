AMDCPU = {"amd-ucode"}

INTELCPU = {"intel-ucode"}

AMDGPU = {
    "llama.cpp-hip",
    "rocm-hip-sdk",
}

INTELGPU = {
    "intel-gpu-tools",
    "vulkan-intel",
}

TUNED = {
    "tuned",
    "tuned-ppd",
}

TLP = {"tlp"}

APFS = {
    "apfs-fuse-git",
}

NIRI = {
    "niri",
    "xwayland-satellite",
    "swaybg",
    "swayidle",
    "swaylock",
    "mako",
    "fuzzel",
    "waybar",
    "xdg-desktop-portal-gtk",
    "xdg-desktop-portal-gnome",
}

ICEPINYIN = {
    "fcitx5-rime",
    "rime-ice-pinyin-git",
    "rime-pinyin-moegirl",
    "rime-pinyin-zhwiki",
}

WLAN_FALLBACK = {
    "iw",
    "iwd",
}

STEAM_HOST = {
    "steam",
}

LOGITECH = {
    "piper",
}

DOCKER = {
    "docker",
    "docker-compose",
}

PRINTER = {
    "hplip",
    "captdriver-git",
}

COMMON = {
    "1password",
    "1password-cli",
    "aegisub",
    "android-tools",
    "anki",
    "apparmor",
    "arch-checkfw",
    "archlinuxcn-keyring",
    "audacity",
    "autocorrect-bin",
    "base",
    "base-devel",
    "bat",
    "bc",
    "bcc",
    "bcc-libbpf-tools",
    "bear",
    "bind",
    "bluez-utils",
    "bmon",
    "btrfs-progs",
    "bustle",
    "bpftrace",
    "cantarell-fonts",
    "cargo-bloat",
    "cargo-deb",
    "cargo-edit",
    "cargo-flamegraph",
    "cargo-release",
    "chafa",
    "cheese",
    "chromium",
    "clang",
    "claude-code",
    "cpio",
    "dconf-editor",
    "debootstrap",
    "devtools",
    "digikam",
    "direnv",
    "dive",
    "dmidecode",
    "dnsmasq",
    "dotnet-sdk",
    "dpkg",
    "efibootmgr",
    "esbuild",
    "eslint",
    "evtest",
    "extension-manager",
    "eza",
    "fastfetch",
    "fcitx5",
    "fcitx5-chinese-addons",
    "fcitx5-configtool",
    "fcitx5-gtk",
    "fcitx5-mozc",
    "fcitx5-pinyin-moegirl",
    "fcitx5-pinyin-zhwiki",
    "fcitx5-qt",
    "fd",
    "file-roller",
    "filezilla",
    "fio",
    "firefox",
    "firefoxpwa",
    "fish",
    "flatpak",
    "flatpak-builder",
    "fwupd",
    "fx",
    "gcc",
    "gdb",
    "gdm",
    "gimp",
    "git",
    "git-delta",
    "git-keeper-git",
    "git-lfs",
    "github-cli",
    "glib2-devel",
    "gnome-backgrounds",
    "gnome-calculator",
    "gnome-calendar",
    "gnome-control-center",
    "gnome-font-viewer",
    "gnome-keyring",
    "gnome-session",
    "gnome-shell",
    "gnome-shell-debug",
    "gnome-shell-docs",
    "gnome-shell-extensions",
    "gnome-system-monitor",
    "gnome-tweaks",
    "gnome-weather",
    "go",
    "golangci-lint",
    "goreleaser",
    "gparted",
    "grub",
    "gst-plugin-pipewire",
    "gtk3-demos",
    "gtk4-demos",
    "gvfs-nfs",
    "gvfs-onedrive",
    "handbrake-cli",
    "htop",
    "ibus",
    "iftop",
    "inxi",
    "inkscape",
    "iotop-c",
    "iperf",
    "iperf3",
    "jq",
    "kate",
    "kcharselect",
    "kolourpaint",
    "konsole",
    "krita",
    "less",
    "libadwaita-demos",
    "libreoffice-fresh",
    "linux",
    "localsend",
    "lollypop",
    "loupe",
    "lrzsz",
    "luminance",
    "man-db",
    "man-pages",
    "mangohud",
    "markdownlint-cli2",
    "memtest86+-efi",
    "mesa-utils",
    "meson",
    "moreutils",
    "mpv",
    "mpv-mpris",
    "mpv-osc-modern-git",
    "mpv-osc-thumbfast-git",
    "mtr",
    "mutter",
    "mutter-debug",
    "mutter-devkit",
    "mutter-docs",
    "mypy",
    "nali-go",
    "namcap",
    "nano",
    "nautilus-open-any-terminal",
    "ncdu",
    "net-tools",
    "netease-cloud-music-gtk4",
    "nethack",
    "nethogs",
    "networkmanager",
    "networkmanager-openvpn",
    "nginx",
    "noto-cjk-ui-patched",
    "noto-fonts-emoji",
    "nvtop",
    "obs-studio",
    "openbsd-netcat",
    "openssh",
    "openvpn",
    "osv-scanner",
    "pandoc-bin",
    "pango-taoky",
    "pango-taoky-debug",
    "pango-taoky-docs",
    "papers",
    "paru",
    "playerctl",
    "pnpm",
    "podman",
    "powertop",
    "pre-commit",
    "prettier",
    "ptyxis-taoky",
    "ptyxis-taoky-debug",
    "pwndbg",
    "pyright",
    "python-bcc",
    "python-biliass",
    "python-keyring",
    "python-tabulate",
    "python-weasyprint",
    "pv",
    "qbittorrent",
    "qemu-full",
    "qemu-user-static-binfmt",
    "qt6-tools",
    "qt6-wayland",
    "rapid-photo-downloader",
    "rasdaemon",
    "rclone",
    "repo",
    "ripgrep",
    "ripgrep-all",
    "rsync",
    "ruby-bundler",
    "ruby-erb",
    "ruff",
    "rustscan",
    "rustup",
    "sg3_utils",
    "shellcheck-static",
    "shfmt",
    "showmethekey",
    "siege",
    "snapper",
    "sqlitebrowser",
    "strace",
    "stress",
    "sudo",
    "supertuxkart",
    "sushi",
    "syncthing",
    "tealdeer",
    "teamspeak3",
    "tigervnc",
    "tmux",
    "tokei",
    "tree",
    "ttf-jetbrains-mono",
    "ttf-liberation",
    "ttf-lxgw-wenkai",
    "typescript",
    "uv",
    "vala",
    "vim",
    "virt-manager",
    "virt-viewer",
    "visual-studio-code-bin",
    "w3m",
    "waycheck",
    "weston",
    "whois",
    "wireguard-tools",
    "wireless-regdb",
    "wireshark-qt",
    "wl-clipboard",
    "xorg-server-xephyr",
    "xorg-xdpyinfo",
    "xorg-xeyes",
    "xorg-xinput",
    "xorg-xlsclients",
    "xterm",
    "xungu-git",
    "xwayland-run",
    "yt-dlp",
    "zenity",
    "zerotier-one",
}

NANOKA_FIRMWARE = {
    "linux-firmware-amdgpu",
    "linux-firmware-other",
    "linux-firmware-realtek",
    "linux-firmware-atheros",
}

SHIMARIN_FIRMWARE = {
    "linux-firmware-intel",
    "sof-firmware",
}

NANOKA = (
    AMDCPU
    | AMDGPU
    | TUNED
    | COMMON
    | NIRI
    | WLAN_FALLBACK
    | STEAM_HOST
    | LOGITECH
    | NANOKA_FIRMWARE
)
SHIMARIN = (
    INTELCPU
    | INTELGPU
    | TLP
    | APFS
    | COMMON
    | NIRI
    | ICEPINYIN
    | LOGITECH
    | SHIMARIN_FIRMWARE
    | DOCKER
)

packages = {
    "nanoka.taoky.moe": NANOKA,
    "shimarin.taoky.moe": SHIMARIN,
}
