#!/bin/sh

# nginx -c "$PWD"/rtmp.conf

# Use docker image tiangolo/nginx-rtmp here, instead of nginx-mod-rtmp on AUR
docker run --rm --network=host --name nginx-rtmp -v "$PWD"/rtmp.conf:/etc/nginx/nginx.conf tiangolo/nginx-rtmp

