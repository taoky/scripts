set -x PIP_REQUIRE_VIRTUALENV true
set -x EDITOR vim
set -x SYSTEMD_EDITOR vim
set -x TLDR_CACHE_MAX_AGE 1680
set -x JQ_COLORS "1;30:0;39:0;39:0;39:0;32:1;39:1;39"
set -x DOCKER_HOST unix://$XDG_RUNTIME_DIR/docker.sock

# User appended path
fish_add_path ~/.cargo/bin
fish_add_path ~/.local/bin

# Arch Linux rustup package after 2023/05/04
fish_add_path /usr/lib/rustup/bin

# "If you installed Nix from the official repositories, you must add the ~/.nix-profile/bin directory to your PATH manually."
fish_add_path ~/.nix-profile/bin

