if status is-login; and status is-interactive
    if test -f /opt/motd.png
        /usr/bin/chafa --scale 0.4 /opt/motd.png
    else
        /usr/bin/chafa --scale 0.4 /opt/motd.jpg
    end
end

alias tmpctr="podman run -it --rm --log-driver none"
alias tmpxctr="podman run -it --rm --log-driver none -e DISPLAY=$DISPLAY -e XAUTHORITY=$XAUTHORITY -v /tmp/.X11-unix:/tmp/.X11-unix -v $XAUTHORITY:$XAUTHORITY"
alias ccplay="flatpak run --file-forwarding moe.taoky.clicking-circles-player @@ ~/Projects/clicking-circles-player/song.json @@ ~/.var/app/sh.ppy.osu/data/osu/files/"
alias dev='tmpctr -v $(pwd):$(pwd) -w $(pwd) local/dev-debian:13'

function klogg
    if test -z "$argv"
        echo "Usage: klogg <filename>"
        return 1
    end
    flatpak run --file-forwarding dev.filimonov.klogg @@ $argv[1] @@
end

