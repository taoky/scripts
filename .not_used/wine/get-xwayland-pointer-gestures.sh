#!/bin/sh

# See https://bugs.winehq.org/show_bug.cgi?id=53114
# This bug crashes all Windows games in Steam when using touchpad.
# This script shows whether pointer gestures for XWayland is on or not

xinput list --name-only | grep ^xwayland-pointer-gestures | xargs -n1 xinput list-props | grep Enabled
