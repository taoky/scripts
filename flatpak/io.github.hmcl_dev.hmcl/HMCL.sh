#!/bin/sh

mkdir -p $XDG_DATA_HOME/HMCL
cd $XDG_DATA_HOME/HMCL || (echo "Can't open $XDG_DATA_HOME/HMCL" && exit 1)
exec /app/jdk/21/bin/java -XX:MinHeapFreeRatio=5 -XX:MaxHeapFreeRatio=15 -jar /app/HMCL/HMCL.jar
