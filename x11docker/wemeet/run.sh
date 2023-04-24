#!/bin/sh

x11docker --gpu=virgl -I --xephyr --clipboard --desktop --pulseaudio=host --webcam --sudouser -i local/wemeet-x11
