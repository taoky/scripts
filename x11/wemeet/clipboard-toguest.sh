#!/bin/sh

xclip -selection clipboard -o -display :0 | xclip -selection clipboard -i -display :114
