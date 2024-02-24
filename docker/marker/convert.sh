#!/bin/sh -ex

if [ -z "$1" ]; then
  echo "Usage: $0 <input> (<output>)"
  exit 1
fi

# get absolute path
input=$(realpath "$1")
filename=$(basename "$input")

if [ -z "$2" ]; then
    output=/tmp/marker-convert/result.md
    mkdir -p /tmp/marker-convert
    touch "$output"
else
    output=$(realpath "$2")
fi

# add filename if output is a directory
if [ -d "$output" ]; then
    output="$output/$filename.md"
    touch "$output"
fi

docker run --rm -v "$input":/workspace/"$filename" -v "$output":/workspace/result/result.md local/marker poetry run python convert_single.py /workspace/"$filename" /workspace/result/result.md

echo "Result is in $output"
