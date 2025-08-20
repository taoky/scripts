#!/bin/sh
export QT_QPA_PLATFORM=xcb
export CURRENT_DINGTALK_VERSION=current_version
export QT_PLUGIN_PATH=/app/dingtalk/7$CURRENT_DINGTALK_VERSION
cd /app/dingtalk/$CURRENT_DINGTALK_VERSION

./com.alibabainc.dingtalk $1
