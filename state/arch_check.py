#!/usr/bin/env python3
import arch_packages

import os
import subprocess


HOSTNAME = os.uname().nodename


def run_cmd(cmd, check=True):
    result = subprocess.run(cmd, check=check, stdout=subprocess.PIPE)
    return result


def pacman_get_installed_packages():
    result = run_cmd(["pacman", "-Qq"])
    installed_packages = result.stdout.decode().splitlines()
    return set(installed_packages)


def pacman_mark_as_explicit(package):
    run_cmd(["pacman", "-D", "--asexplicit", package])


def pacman_mark_as_implicit(package):
    run_cmd(["pacman", "-D", "--asdeps", package])


def pacman_get_orphans():
    result = run_cmd(["pacman", "-Qqdt"], check=False)
    if result.returncode == 1:
        # no orphans
        return set()
    orphans = result.stdout.decode().splitlines()
    return set(orphans)


def main():
    target_packages = arch_packages.packages[HOSTNAME]
    local_packages = pacman_get_installed_packages()

    print("Not installed packages:", sorted(target_packages - local_packages))

    # Mark packages
    for package in target_packages:
        if package in local_packages:
            pacman_mark_as_explicit(package)
    for package in local_packages - target_packages:
        pacman_mark_as_implicit(package)
    
    print("Orphaned packages:", sorted(pacman_get_orphans()))


if __name__ == "__main__":
    if os.geteuid() != 0:
        print("This script must be run as root.")
        exit(1)
    main()
