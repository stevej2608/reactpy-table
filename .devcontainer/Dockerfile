FROM python:3.11.4-bookworm

RUN useradd -ms /bin/bash vscode

# RUN apt-get update && apt-get install -y build-essential g++ libx11-dev libxkbfile-dev libsecret-1-dev

# Install chrome for scraper. This reports errors but it's OK
# https://techpiezo.com/linux/install-google-chrome-in-debian-buster/

ENV CHROME_VERSION 114.0.5735.90

RUN mkdir -p /tmp/chrome \
   && cd /tmp/chrome \
   && wget -q http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}-1_amd64.deb

RUN cd /tmp/chrome \
   && ls \
   && dpkg -i google-chrome*.deb || true \
   && apt update \
   && apt --fix-broken install -y

# Install chromedriver

RUN mkdir -p /tmp/ && \
    cd /tmp/ && \
    wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${CHROME_VERSION}/chromedriver_linux64.zip  && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/bin/ && \
    # clean up the container "layer", after we are done
    rm /tmp/chromedriver.zip

# Install nodejs 20.x
# https://computingforgeeks.com/how-to-install-nodejs-on-ubuntu-debian-linux-mint/

RUN apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates && \
    curl -sL https://deb.nodesource.com/setup_20.x | bash - && \
    apt -y install nodejs

RUN npm install -g pnpm


# Mount the VSCODE project in here

RUN mkdir /workspace && \
    chown vscode:vscode /workspace

USER vscode

ENV PATH="/home/vscode/.local/bin:${PATH}"


