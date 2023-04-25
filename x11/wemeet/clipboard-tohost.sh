#!/bin/sh

xclip -selection clipboard -o -display :114 | xclip -selection clipboard -i -display :0
