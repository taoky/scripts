#!/usr/bin/env python3

import datetime
# you need python-notify2
import notify2
import time

def main():
    now = datetime.datetime.now()
    title = "Time Notification"
    if now.hour >= 23 or now.hour <= 4:
        contents = f"It's {now.hour}:{now.minute} now!"
    else:
        return
    noti = notify2.Notification(title, contents)
    # https://developer-old.gnome.org/notification-spec/#hints
    # transient: When set the server will treat the notification as transient and by-pass the server's persistence capability, if it should exist. 
    noti.set_hint("transient", True)
    noti.show()


if __name__ == "__main__":
    notify2.init("sleep-timer")
    main()
