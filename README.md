# Tor Proxy Generator

This project sets up a Tor proxy using a Docker container, allowing you to route traffic through the Tor network. The container configures Tor with a custom `torrc` file, and you can access the proxy using the container's local IP address.

The local IP forwards your traffic through the Tor network for anonymous requests.

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

# Starting Docker
```
sudo docker compose up --build -d
```

# Getting Container's Local IP
```
sudo docker inspect tor-proxy | grep "IPAddress"
```

# Testing Tor
To test the Tor proxy, use the container's IP with `main.py`. First, set up a Python virtual environment and install dependencies from `requirements.txt`:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py --ip <container-ip>
```

Example:
```
python3 main.py --ip 172.20.0.3
```

