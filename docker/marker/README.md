# marker (Dockerized)

From: <https://github.com/VikParuchuri/marker>

PDF -> Markdown

## Usage

Build:

```console
docker build -t local/marker .
```

```console
docker run --rm -v $(pwd):/workspace local/marker poetry run python convert_single.py /workspace/your.pdf /workspace/your.md
```
