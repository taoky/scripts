# Ref: https://github.com/zzh1996/mydocker/blob/master/Dockerfile
FROM ustclug/debian:13

# base system
RUN apt update && apt install -y fish build-essential python3 python-is-python3 curl vim sudo
RUN useradd -ms /usr/bin/fish user && \
    usermod -aG sudo user && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    chsh -s /usr/bin/fish && \
    mkdir -p /root/.config/fish/functions && \
    printf '%s\n' \
'function fish_prompt' \
'    set user (whoami)' \
'    set cwd (prompt_pwd)' \
'    set_color green' \
'    echo -n "[DEV] "' \
'    set_color cyan' \
'    echo -n "$user@$cwd> "' \
'    set_color normal' \
'end' > /root/.config/fish/functions/fish_prompt.fish

# Note that in rootless container, root in container = (usually normal) user in host
# So we only create new user for envs that don't like root.

# Python: ruff & uv
RUN curl -LsSf https://astral.sh/ruff/install.sh | sh && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

# Tools
RUN apt install -y ripgrep fd-find tmux wget
RUN curl -fLo /root/.tmux.conf https://github.com/taoky/scripts/raw/refs/heads/master/dotfile/.tmux.conf

# git-keeper dev
RUN apt install -y devscripts debhelper fakeroot lintian dh-exec go-md2man

CMD ["/usr/bin/fish"]
