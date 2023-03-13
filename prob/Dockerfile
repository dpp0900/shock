FROM ubuntu:12.04

ARG DEBIAN_FRONTEND=noninteractive

RUN sed -i -e 's/archive.ubuntu.com\|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install apache2 -y
RUN apt-get install php5 -y
RUN apt-get install wget -y
RUN apt-get install tar -y
RUN apt-get install gcc -y
RUN apt-get install make -y
RUN apt-get install python -y
RUN apt-get install python-pip -y
RUN apt-get install build-essential libssl-dev libffi-dev python-dev -y

RUN cd /tmp && \
    wget --no-check-certificate https://ftp.gnu.org/gnu/bash/bash-4.2.tar.gz && \
    tar -xvf bash-4.2.tar.gz && \
    cd bash-4.2 && \
    ./configure --prefix=/ && \
    make && \
    make install
COPY ./apache2/ /etc/apache2
COPY ./status.cgi /usr/lib/cgi-bin/
COPY ./index.html /var/www/
COPY ./flag.txt /

RUN chmod 777 /flag.txt

RUN chmod 755 /usr/lib/cgi-bin/status.cgi

EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2ctl"]