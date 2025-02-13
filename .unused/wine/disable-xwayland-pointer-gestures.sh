#!/bin/sh

# See https://bugs.winehq.org/show_bug.cgi?id=53114
# This bug crashes all Windows games in Steam when using touchpad.
# Disabling gestures for xwayland may help

xinput list --name-only | grep ^xwayland-pointer-gestures | xargs -n1 xinput disable
