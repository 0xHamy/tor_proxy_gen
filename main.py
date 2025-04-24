import requests


# Configure the Tor proxy using the container's IP
proxy_ip = "172.23.0.2" 
proxies = {
    "http": f"socks5h://{proxy_ip}:9050",
}


ip_check_url = "http://icanhazip.com"


try:
    # Send an HTTP GET request through the Tor proxy
    response = requests.get(ip_check_url, proxies=proxies, timeout=30)
    if response.status_code == 200:
        tor_ip = response.text.strip()
        print(f"Tor exit node IP: {tor_ip}")
    else:
        print(f"Failed to retrieve IP. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

