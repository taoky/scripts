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
    "wofi",
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

SIMPLEX = {
    "openbox",
    "picom",
    "xcompmgr",
    "feh",
}

TILIX = {
    "tilix-git",
    "tilix-git-debug",
    "ldc",
    "po4a",
}

TEXLIVE = {
    "texlive-basic",
    "texlive-langchinese",
    "texlive-bibtexextra",
    "texlive-fontsextra",
    "texlive-latexextra",
    "texlive-mathscience",
    "texlive-plaingeneric",
}

COMMON = {
    "1password",
    "1password-cli",
    "adobe-source-code-pro-fonts",
    "aegisub",
    "android-tools",
    "anki",
    "apparmor",
    "arch-checkfw",
    "archlinuxcn-keyring",
    "asar",
    "asciinema",
    "aspell-en",
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
    "btrfs-heatmap",
    "bustle",
    "bpftrace",
    "cabextract",
    "cantarell-fonts",
    "cargo-bloat",
    "cargo-deb",
    "cargo-edit",
    "cargo-flamegraph",
    "cargo-fuzz",
    "cargo-release",
    "chafa",
    "cheese",
    "chromium",
    "clang",
    "claude-code",
    "compsize",
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
    "fsearch",
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
    "gnome-shell-extension-gsconnect-git",
    "gnome-system-monitor",
    "gnome-tweaks",
    "gnome-user-docs",
    "gnome-weather",
    "go",
    "go-md2man",
    "golangci-lint",
    "goreleaser",
    "gparted",
    "grub",
    "gst-plugin-pipewire",
    "guestfs-tools",
    "gtk3-demos",
    "gtk4-demos",
    "gvfs-google",
    "gvfs-nfs",
    "gvfs-onedrive",
    "handbrake-cli",
    "heaptrack",
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
    "kernel-modules-hook",
    "keybase-bin",
    "kolourpaint",
    "konsole",
    "krita",
    "less",
    "lftp",
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
    "musl",
    "mutter",
    "mutter-debug",
    "mutter-devkit",
    "mutter-docs",
    "mypy",
    "nali-go",
    "namcap",
    "nano",
    "nautilus-image-converter",
    "nautilus-python",
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
    "nvme-cli",
    "nvtop",
    "obs-studio",
    "openbsd-netcat",
    "openssh",
    "openvpn",
    "osv-scanner",
    "otf-comicshanns-nerd",
    "pandoc-bin",
    "pango-taoky",
    "pango-taoky-debug",
    "pango-taoky-docs",
    "paru",
    "playerctl",
    "pnpm",
    "podman",
    "powertop",
    "pre-commit",
    "prettier",
    "proxychains-ng",
    "ptyxis-taoky",
    "ptyxis-taoky-debug",
    "pwndbg",
    "pyright",
    "python-aiohttp",
    "python-bcc",
    "python-biliass",
    "python-keyring",
    "python-pip",
    "python-requests",
    "python-tabulate",
    "python-weasyprint",
    "python-uv",
    "pypy3",
    "pv",
    "qadwaitadecorations-qt5-git",
    "qbittorrent",
    "qemu-full",
    "qemu-user-static-binfmt",
    "qt6-tools",
    "qt6-wayland",
    "rapid-photo-downloader",
    "rasdaemon",
    "rclone",
    "remmina",
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
    "skopeo",
    "snapper",
    "socat",
    "soundfont-fluid",
    "speech-dispatcher",
    "sqlitebrowser",
    "strace",
    "stress",
    "sudo",
    "supertuxkart",
    "sushi",
    "syncthing",
    "sysstat",
    "sysprof",
    "tcpdump",
    "tealdeer",
    "teamspeak3",
    "tigervnc",
    "timidity++",
    "tmux",
    "tokei",
    "traceroute",
    "tree",
    "ttf-jetbrains-mono",
    "ttf-jetbrains-mono-nerd",
    "ttf-liberation",
    "ttf-lxgw-wenkai",
    "typescript",
    "unarchiver",
    "uv",
    "vala",
    "valgrind",
    "vim",
    "virt-manager",
    "virt-viewer",
    "visual-studio-code-bin",
    "w3m",
    "waifu2x-ncnn-vulkan",
    "waycheck",
    "weston",
    "whois",
    "wireguard-tools",
    "wireless-regdb",
    "wireshark-qt",
    "wl-clipboard",
    "xdg-terminal-exec",
    "xorg-server-xephyr",
    "xorg-server-xvfb",
    "xorg-xdpyinfo",
    "xorg-xeyes",
    "xorg-xinput",
    "xorg-xlsclients",
    "xterm",
    "xungu-git",
    "xwayland-run",
    "yazi",
    "yt-dlp",
    "zenity",
    "zerotier-one",
    "zsh",
    "zsh-completions",
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
    | SIMPLEX
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
    | PRINTER
    | SIMPLEX
    | TILIX
    | TEXLIVE
)

packages = {
    "nanoka.taoky.moe": NANOKA,
    "shimarin.taoky.moe": SHIMARIN,
}
