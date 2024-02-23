FROM ustclug/debian:bookworm-slim

ARG COMMIT=ad6c97ca916084b225cc3319637449efbd4b0cb6

RUN apt update && apt install -y sudo git wget build-essential python3-poetry python3-pip && \
    git clone https://github.com/VikParuchuri/marker workdir && \
    cd workdir && \
    git checkout ad6c97ca916084b225cc3319637449efbd4b0cb6
WORKDIR /workdir
RUN echo "deb https://notesalexp.org/tesseract-ocr5/bookworm/ bookworm main" | tee /etc/apt/sources.list.d/notesalexp.list && \
    apt-get update -oAcquire::AllowInsecureRepositories=true && \
    apt-get install --allow-unauthenticated -y notesalexp-keyring && \
    apt-get update && \
    apt-get install -y tesseract-ocr
RUN apt install -y ghostscript && \
    cat scripts/install/apt-requirements.txt | xargs apt install -y
RUN poetry install && \
    poetry remove torch && \
    poetry run pip3 install --break-system-packages torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
# huggingface cache
RUN poetry run python -c "from marker.models import load_all_models; load_all_models()"
