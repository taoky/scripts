#!/bin/bash

shopt -s globstar nullglob
for i in ~/.ssh/control-*; do
    name=$(basename "$i")
    name=${name#"control-"}
    IFS=":" read -r -a name_arr <<< "$name"
    host=${name_arr[0]}
    port=${name_arr[1]}
    echo "Closing $host:$port"
    ssh -O exit -p "$port" "$host"; 
done

