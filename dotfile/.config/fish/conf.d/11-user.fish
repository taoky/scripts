if status is-login; and status is-interactive
    /usr/bin/chafa --scale 0.4 /opt/motd.png
end

alias kubectl="minikube kubectl --"
alias tmpctr="podman run -it --rm --log-driver none"
alias vim="nvim"
