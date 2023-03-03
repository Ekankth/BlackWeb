FROM ekankth/ekankthdev:ekankthdev

WORKDIR /root/Ekankth

RUN apt -qq update
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt -qq install -y --no-install-recommends \
    curl \
    git \
    gnupg2 \
    unzip \
    wget \
    python3-pip \
    ffmpeg

COPY . .

RUN pip3 install --upgrade pip setuptools
RUN pip3 install --upgrade pykillerx
RUN pip3 install -r requirements.txt

CMD [ "bash", "./start" ]
