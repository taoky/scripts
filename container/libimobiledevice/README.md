# iOS with latest libimobiledevice, in Docker container

Requirement: host running usbmuxd. `usbmuxd 1.1.1` is OK.

Use `ideviceinfo` to check if your device is connected.

Use `idevicebackup2` to backup your device.

```shell
sudo docker compose up
```

\* rootless container not supported, obviously as it requires `/run` mounted.
