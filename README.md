# UniFi Controller Dockerfile

This is a dockerised version of the Unifi Access Point (UAP) Controller.

## Usage

Create a named volume to persist data:

```bash
docker volume create --name unifi-data
```

Pull the image for the desired version of the controller:

```bash
docker pull csmith/unifi:4.8.18
```

Start a container, exposing ports as needed:

```bash
docker run -d --name unifi \
              --restart always \
              -p 8443:8443 \
              -p 8080:8080 \
              -v unifi-data:/var/lib/unifi \
              csmith/unifi:4.8.18
```

The container exposes these ports:

  * 8080 (used by the UAPs to send messages to the controller)
  * 8443 (admin web interface, HTTPS)
  * 8843 (HTTPS captive portal redirection)
  * 8880 (HTTP captive portal redirection)

