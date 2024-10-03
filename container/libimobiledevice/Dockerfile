FROM docker.io/ustclug/debian:bookworm
ARG LIBIMOBILEDEVICE_COMMIT=6fc41f57fc607df9b07446ca45bdf754225c9bd9
ARG LIBIMOBILEDEVICE_GLUE_COMMIT=214bafdde6a1434ead87357afe6cb41b32318495
ARG LIBPLIST_COMMIT=d45396aad911d496494a587bd2d3ef20c2e8a8d0
# ARG USBMUXD_COMMIT=c7a0dd9b82633ea347497626282e3051a469ef50
ARG LIBUSBMUXD_COMMIT=30e678d4e76a9f4f8a550c34457dab73909bdd92

# Install git and build deps
RUN apt update && apt install -y --no-install-recommends git ca-certificates \
    build-essential \
	pkg-config \
	checkinstall \
	git \
	autoconf \
	automake \
    python3-dev \
	libtool-bin \
	libssl-dev \
    libusb-1.0-0-dev \
    adduser

WORKDIR /tmp

# Clone and build libplist
RUN git clone https://github.com/libimobiledevice/libplist.git && \
    cd libplist && \
    git checkout $LIBPLIST_COMMIT && \
    NOCONFIGURE=1 ./autogen.sh && \
    ./configure --prefix=/usr && \
    make && \
    make install

# Clone and build libimobiledevice-glue
RUN git clone https://github.com/libimobiledevice/libimobiledevice-glue && \
    cd libimobiledevice-glue && \
    git checkout $LIBIMOBILEDEVICE_GLUE_COMMIT && \
    NOCONFIGURE=1 ./autogen.sh && \
    ./configure --prefix=/usr && \
    make && \
    make install

# Clone and build libusbmuxd
RUN git clone https://github.com/libimobiledevice/libusbmuxd.git && \
    cd libusbmuxd && \
    git checkout $LIBUSBMUXD_COMMIT && \
    NOCONFIGURE=1 ./autogen.sh && \
    ./configure --prefix=/usr && \
    make && \
    make install

# Clone and build libimobiledevice
RUN git clone https://github.com/libimobiledevice/libimobiledevice.git && \
    cd libimobiledevice && \
    git checkout $LIBIMOBILEDEVICE_COMMIT && \
    NOCONFIGURE=1 ./autogen.sh && \
    ./configure --prefix=/usr && \
    make && \
    make install

# Use host usbmuxd instead

# Clone and build usbmuxd
# RUN git clone https://github.com/libimobiledevice/usbmuxd && \
#     cd usbmuxd && \
#     git checkout $USBMUXD_COMMIT && \
#     NOCONFIGURE=1 ./autogen.sh && \
#     ./configure --prefix=/usr && \
#     make && \
#     make install

# Create user
RUN adduser --disabled-password --gecos "" --uid 1000 ios
USER 1000:1000
WORKDIR /home/ios

CMD echo "Run docker exec -it <container> bash to enter the container."; tail -f /dev/null
