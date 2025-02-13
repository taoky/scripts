FROM x11docker/xfce

# Probably redundant deps

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    apt-get update && apt-get install -y \
    sudo iputils-ping gstreamer1.0-tools wget firefox-esr gstreamer1.0-plugins-good gstreamer1.0-plugins-bad \
    iproute2 vim strace netcat fonts-noto-cjk libpulse0 vainfo libxv1 \
    va-driver-all vdpau-driver-all mesa-utils mesa-utils-extra \
    pavucontrol

# Install wemeet
RUN wget https://updatecdn.meeting.qq.com/cos/5a910969828531efb24add85626e2372/TencentMeeting_0300000000_3.14.0.402_x86_64_default.publish.deb && \
    apt install -y ./TencentMeeting_0300000000_3.14.0.402_x86_64_default.publish.deb && \
    rm TencentMeeting_0300000000_3.14.0.402_x86_64_default.publish.deb
