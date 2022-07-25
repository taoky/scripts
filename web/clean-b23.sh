#!/bin/bash

use_open=0

while getopts "o" arg; do
	case $arg in
		o)
			use_open=1
			;;
		*)
			;;
	esac
done

b23=${!OPTIND}
b23_real=$(curl -Ls -w '%{url_effective}' "$b23" -o /dev/null)

b23_notrack=$(echo "${b23_real}" | cut -f1 -d"?")
echo "$b23_notrack"

if [ $use_open = 1 ]; then
	xdg-open "$b23_notrack"
fi
