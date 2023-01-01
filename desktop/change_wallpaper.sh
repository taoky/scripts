#!/bin/sh

if [ -z $1 ]; then
    echo "Usage: $0 <path-to-local-wallpaper-image>"
    exit 1
fi

gdbus call --session \
          --dest org.freedesktop.portal.Desktop \
          --object-path /org/freedesktop/portal/desktop \
          --method org.freedesktop.portal.Wallpaper.SetWallpaperFile \
          "" 20 {} 20<"$1"
