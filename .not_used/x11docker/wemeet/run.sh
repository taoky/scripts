#!/bin/sh

# Line 4031 Westonoutput="WL"
x11docker --gpu -I --weston-xwayland --westonini=$(pwd)/weston.ini --home --clipboard --desktop --pulseaudio=host --webcam --sudouser -i local/wemeet-x11
