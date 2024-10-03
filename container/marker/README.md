# marker (Dockerized)

From: <https://github.com/VikParuchuri/marker>

PDF -> Markdown

## Usage

Build:

```shell
docker build -t local/marker .
# or
podman build -t local/marker .
```

```shell
docker run --rm -v $(pwd):/workspace local/marker poetry run python convert_single.py /workspace/your.pdf /workspace/your.md
# or
podman run --rm -v $(pwd):/workspace local/marker poetry run python convert_single.py /workspace/your.pdf /workspace/your.md
```

```shell
./convert.sh some.pdf ~/tmp/
```
