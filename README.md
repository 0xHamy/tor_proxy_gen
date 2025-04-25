# Tor proxy generator

You can generate a tor IP by connecting to the tor network using torrc. The docker container provided will setup tor for you and you can access it using your docker container's IP address.

That local IP address forwards your traffic through the Tor network.

[Dockerfile source code:](./Dockerfile) 
```dockerfile
# Use a lightweight Debian-based image
FROM debian:bullseye-slim

# Install Tor
RUN apt-get update && \
    apt-get install -y tor && \
    rm -rf /var/lib/apt/lists/*

# Copy custom Tor configuration
COPY torrc /etc/tor/torrc

# Expose the Tor SOCKS5 proxy port
EXPOSE 9050

# Run Tor as the main process
CMD ["tor", "-f", "/etc/tor/torrc"]

```

[docker-compose.yaml source code:](./docker-compose.yaml)
```yaml
services:
  tor:
    build:
      context: .
      dockerfile: Dockerfile
    image: tor-proxy
    ports:
      - "9050:9050"
    container_name: tor-proxy
    restart: unless-stopped

```

[torrc source code:](./torrc)
```
SocksPort 0.0.0.0:9050
Log notice stdout
```

# Starting docker
```
sudo docker compose up --build -d
```

Getting container's local IP:
```
sudo docker inspect tor-proxy | grep "IPAddress"
```

# Testing Tor 
Use that IP with main.py to test proxy, first setup a python virtual environment for packages and install `requirements.txt`:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py --ip 172.20.0.3
```




