#!/bin/sh
# Usage:
# echo -n "测试剪贴板" | ./pipe-toguest.sh

xclip -selection clipboard -i -display :114
