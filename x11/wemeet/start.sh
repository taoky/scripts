#!/bin/sh -e

# Start weston
echo "Starting weston"
weston -c $(pwd)/weston.ini --socket=wayland-114 &

sleep 3

# Start xwayland
echo "Starting Xwayland"
WAYLAND_DISPLAY=wayland-114 Xwayland :114 -ac -retro +extension RANDR +extension RENDER +extension GLX +extension XVideo +extension DOUBLE-BUFFER +extension SECURITY +extension DAMAGE +extension X-Resource -extension XINERAMA -xinerama -extension MIT-SHM +extension Composite +extension COMPOSITE -extension XTEST -tst -dpms -s off &

sleep 3

# Start mutter and wemeet
echo "Starting mutter"
DISPLAY=:114 mutter --x11 &

echo "Starting wemeet"
DISPLAY=:114 flatpak run com.tencent.wemeet