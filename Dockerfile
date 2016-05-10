FROM ubuntu:xenial 
MAINTAINER Chris Smith <chris87@gmail.com> 

RUN \
  apt-get update && \ 
  apt-get -y install \
    binutils \
    curl \
    jsvc \
    mongodb-server \
    openjdk-8-jre-headless \
    software-properties-common

# UniFi 4.8.18
RUN curl -L -o unifi_sysvinit_all.deb http://www.ubnt.com/downloads/unifi/4.8.18/unifi_sysvinit_all.deb && \
  dpkg --install unifi_sysvinit_all.deb && \
  rm unifi_sysvinit_all.deb

EXPOSE 8080 8081 8443 8843 8880

VOLUME ["/var/lib/unifi"]

WORKDIR /var/lib/unifi

CMD ["/usr/bin/java", "-Xmx1024M", "-jar", "/usr/lib/unifi/lib/ace.jar", "start"]

