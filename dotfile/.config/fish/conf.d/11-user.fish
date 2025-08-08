if status is-login; and status is-interactive
    /usr/bin/chafa --scale 0.4 /opt/motd.png
end

alias kubectl="minikube kubectl --"
alias tmpctr="podman run -it --rm --log-driver none"
alias tmpxctr="podman run -it --rm --log-driver none -e DISPLAY=$DISPLAY -e XAUTHORITY=$XAUTHORITY -v /tmp/.X11-unix:/tmp/.X11-unix -v $XAUTHORITY:$XAUTHORITY"
alias vim="nvim"
alias ccplay="flatpak run --file-forwarding moe.taoky.clicking-circles-player @@ ~/Projects/clicking-circles-player/song.json @@ ~/.var/app/sh.ppy.osu/data/osu/files/"

function klogg
    if test -z "$argv"
        echo "Usage: klogg <filename>"
        return 1
    end
    flatpak run --file-forwarding dev.filimonov.klogg @@ $argv[1] @@
end

