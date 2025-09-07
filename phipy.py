import requests
import time
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Typing effect function
def slow_print(text, delay=0.04, color=Fore.CYAN):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Banner
def banner():
    print(Fore.GREEN + Style.BRIGHT + """
██████╗ ██╗  ██╗██╗██████╗ ██╗   ██╗
██╔══██╗██║  ██║██║██╔══██╗╚██╗ ██╔╝
██████╔╝███████║██║██████╔╝ ╚████╔╝ 
██╔═══╝ ██╔══██║██║██╔═══╝   ╚██╔╝  
██║     ██║  ██║██║██║        ██║   
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   
    """)
    slow_print("⚡ Professional Public  IP Lookup Tool ⚡", 0.04, Fore.MAGENTA)
    slow_print("👑 Created by: Dhiru", 0.04, Fore.YELLOW)
    print(Fore.RED + "─────────────────────────────────────────────")

# Function to track IP
def phipy(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url).json()

    if response.get("status") == "fail":
        slow_print("[!] Invalid or Private IP. Cannot fetch details.", 0.04, Fore.RED)
        return

    slow_print("\n🔍 IP Tracker Results 🔍", 0.04, Fore.YELLOW)
    time.sleep(0.3)

    print(Fore.CYAN + f"IP Address : {response.get('query')}")
    print(Fore.CYAN + f"Country    : {response.get('country')}")
    print(Fore.CYAN + f"Region     : {response.get('regionName')}")
    print(Fore.CYAN + f"City       : {response.get('city')}")
    print(Fore.CYAN + f"ISP        : {response.get('isp')}")
    print(Fore.CYAN + f"Org        : {response.get('org')}")
    print(Fore.CYAN + f"Timezone   : {response.get('timezone')}")
    print(Fore.CYAN + f"Latitude   : {response.get('lat')}")
    print(Fore.CYAN + f"Longitude  : {response.get('lon')}")

    # Google Maps Link
    if response.get("lat") and response.get("lon"):
        maps_link = f"https://www.google.com/maps?q={response.get('lat')},{response.get('lon')}"
        print(Fore.MAGENTA + f"\n🌍 Google Maps Link: {maps_link}")

    print(Fore.GREEN + "\n✔ Lookup Complete!\n")

# Detect own IP
def get_my_ip():
    return requests.get("https://api64.ipify.org?format=json").json()["ip"]

# Footer
def footer():
    print(Fore.RED + "─────────────────────────────────────────────")
    slow_print("🔥 Follow me on Instagram: https://www.instagram.com/devil_dhiru69/ 🔥", 0.04, Fore.MAGENTA)
    slow_print("💻 GitHub:  https://github.com/dhiru69-tech", 0.04, Fore.CYAN)
    print(Fore.RED + "─────────────────────────────────────────────\n")

# Main Program
if __name__ == "__main__":
    banner()
    slow_print("Welcome to Dhiru's Custom IP Tracker", 0.04, Fore.CYAN)

    choice = input(Fore.YELLOW + "\nDo you want to track your own Public IP? (y/n): ").lower()

    if choice == "y":
        ip = get_my_ip()
        slow_print(f"🌐 Your Public IP Detected: {ip}", 0.04, Fore.CYAN)
        ip_tracker(ip)
    else:
        ip = input(Fore.GREEN + "🎯 Enter Target Public  IP Address: ")
        phipy(ip)

    footer()
