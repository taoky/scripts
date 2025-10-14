# Ref: https://github.com/zzh1996/mydocker/blob/master/Dockerfile
FROM ustclug/debian:13

# Note that in rootless container, root in container = (usually normal) user in host
# So we don't create new user here.

# base system
RUN apt update && apt install -y fish build-essential python3 python-is-python3 curl vim

# Python: ruff & uv
RUN curl -LsSf https://astral.sh/ruff/install.sh | sh && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

# git-keeper dev
RUN apt install -y devscripts debhelper fakeroot lintian dh-exec go-md2man
