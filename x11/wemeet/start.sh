#!/bin/sh -e

# Start xwayland
echo "Starting Xwayland"
Xwayland :114 -ac -retro +extension RANDR +extension RENDER +extension GLX +extension XVideo +extension DOUBLE-BUFFER +extension SECURITY +extension DAMAGE +extension X-Resource -extension XINERAMA -xinerama +extension Composite +extension COMPOSITE -extension XTEST -tst -dpms -s off -decorate -geometry 1920x1080 &

echo "Waiting for X server to be ready"
while ! xdpyinfo -display :114 >/dev/null 2>&1; do
    sleep 1
done

# Start openbox and wemeet
echo "Starting openbox"
DISPLAY=:114 openbox &
DISPLAY=:114 xcompmgr &

echo "Starting wemeet"
DISPLAY=:114 flatpak run com.tencent.wemeet
