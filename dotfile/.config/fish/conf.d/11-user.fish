if status is-login; and status is-interactive
    if test -f /opt/motd.png
        /usr/bin/chafa --scale 0.4 /opt/motd.png
    else
        /usr/bin/chafa --scale 0.4 /opt/motd.jpg
    end
end

set host (cat /etc/hostname)

alias tmpctr="podman run -it --rm --log-driver none"
alias tmpxctr="podman run -it --rm --log-driver none -e DISPLAY=$DISPLAY -e XAUTHORITY=$XAUTHORITY -v /tmp/.X11-unix:/tmp/.X11-unix -v $XAUTHORITY:$XAUTHORITY"
alias ccplay="flatpak run --file-forwarding moe.taoky.clicking-circles-player @@ ~/Projects/clicking-circles-player/song.json @@ ~/.var/app/sh.ppy.osu/data/osu/files/"

function dev
    tmpctr -v $(pwd):$(pwd) -w $(pwd) $argv local/dev-debian:13
end

if test $host = "nanoka.taoky.moe"
    alias gptoss20b='HIP_VISIBLE_DEVICES=0 llama-server -hf ggml-org/gpt-oss-20b-GGUF --ctx-size 32768 --jinja -ub 2048 -b 2048'
end

function klogg
    if test -z "$argv"
        echo "Usage: klogg <filename>"
        return 1
    end
    flatpak run --file-forwarding dev.filimonov.klogg @@ $argv[1] @@
end

function auto_theme --description 'Use osc11 (0=light, 1=dark) to set fish theme'
    if not status --is-interactive
        return
    end

    set -l theme "Tomorrow Night"
    if command -q osc11
        if osc11
            set theme "fish_default"
        end
    end

    fish_config theme choose "$theme" >/dev/null 2>/dev/null
end

auto_theme
