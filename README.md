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

Port 8443 is used for the HTTPS web interface, port 8080 used by APs.

The Dockerfile exposes these ports: 8081 8443 8843 8880
