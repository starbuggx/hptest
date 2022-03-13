FROM ubuntu:latest
COPY ./honeypot.py /usr/local/share/honeypot.py

RUN apt update && apt install -y \
    curl \
    jq \
    # tzdata \
    tcpdump \
    # nmap \
    # dnsutils \
    # traceroute \
    # zip \
    # git \
    # vim \
    # htop \
    # iftop \
    # net-tools \
    # netcat \
    # less \
    iproute2 \
    python3 \
    python3-pip \
    && \
    python3 -m pip install flask





ENV FLASK_ENV=development
ENV FLASK_APP=/usr/local/share/honeypot.py


ENTRYPOINT flask run -h 0.0.0.0 -p 8080
EXPOSE 8080