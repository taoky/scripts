set -x PIP_REQUIRE_VIRTUALENV true
set -x EDITOR vim
set -x TLDR_CACHE_MAX_AGE 1680

# User appended path
fish_add_path ~/.cargo/bin
fish_add_path ~/.local/bin

# Arch Linux rustup package after 2023/05/04
fish_add_path /usr/lib/rustup/bin

