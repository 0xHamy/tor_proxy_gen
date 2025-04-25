import requests
import argparse


def print_instructions():
    print("Instructions:")
    print("Run this script from the command line to check the Tor exit node IP.")
    print("Usage: python script.py --ip <proxy_ip>")
    print("Example: python script.py --ip 172.23.0.2")
    print("The script will send an HTTP GET request through the Tor proxy and display the exit node IP.")
    print("Ensure the Tor proxy is running and accessible at the specified IP and port (9050).")


# Set up argument parser
parser = argparse.ArgumentParser(description="Check Tor exit node IP", add_help=False)
parser.add_argument("--ip", required=True, help="Proxy IP address")

try:
    args = parser.parse_args()
except SystemExit:
    print_instructions()
    exit(1)

# Configure the Tor proxy using the provided IP
proxy_ip = args.ip
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