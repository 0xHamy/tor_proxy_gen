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
