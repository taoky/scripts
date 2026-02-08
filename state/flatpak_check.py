#!/usr/bin/env python3
import os
import subprocess

import flatpak_packages


HOSTNAME = os.uname().nodename


def run_cmd(cmd, check=True):
    result = subprocess.run(cmd, check=check, stdout=subprocess.PIPE)
    return result


def flatpak_get_installed_apps():
    result = run_cmd(["flatpak", "list", "--app", "--columns=application"])
    installed_apps = result.stdout.decode().splitlines()
    return set(installed_apps)


def get_target_apps():
    if hasattr(flatpak_packages, "packages"):
        if HOSTNAME not in flatpak_packages.packages:
            print(f"Hostname {HOSTNAME} not found in flatpak_packages.packages.")
            exit(1)
        return flatpak_packages.packages[HOSTNAME]
    if hasattr(flatpak_packages, "COMMON"):
        return set(flatpak_packages.COMMON)
    print("flatpak_packages must define packages or COMMON.")
    exit(1)


def main():
    target_apps = get_target_apps()
    local_apps = flatpak_get_installed_apps()

    print("Not installed packages:", sorted(target_apps - local_apps))


if __name__ == "__main__":
    main()
