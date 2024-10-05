#!/usr/bin/env python3
# Parse "OutgoingBytes" from dbus-send output

# Usage:
# dbus-send --session --dest=org.freedesktop.DBus --type=method_call --print-reply /org/freedesktop/DBus org.freedesktop.DBus.Debug.Stats.GetStats | ./dbus_bytes_stat.py
# or:
# sudo dbus-send --system --dest=org.freedesktop.DBus --type=method_call --print-reply /org/freedesktop/DBus org.freedesktop.DBus.Debug.Stats.GetStats | ./dbus_bytes_stat.py

import sys
import re

CONN_NAME = re.compile(r"string \"(:[\d\.]+)\"")


def main():
    stack = []
    mapping = {}
    for l in sys.stdin:
        l = l.strip()
        if l == "struct {":
            stack.append("struct")
        elif l == "}":
            stack.pop()
        elif "OutgoingBytes" in l:
            stack.append("out")
        else:
            m = CONN_NAME.match(l)
            if m:
                stack.append(m[1])
                continue
            if len(stack) > 0 and stack[-1] == "out" and l.startswith("uint32"):
                bytes = int(l[7:])
                stack.pop()
                conn = stack[-1]
                mapping[conn] = bytes
                stack.pop()
    mapping = {k: v for k, v in mapping.items() if v != 0}
    print(mapping)


if __name__ == "__main__":
    main()
