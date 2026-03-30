import requests
import os
import time

# --- COLORS ---
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
WHITE = '\033[97m'
RESET = '\033[0m'

# --- ASCII LOGO DESIGN ---
def show_banner():
    os.system('clear')
    print(f"{CYAN}")
    print(r"  ___   _      __  __   ___   ___    ___   ____ ")
    print(r" / _ \ | |    |  \/  | / _ \ | _ \  / _ \ / ___|")
    print(r"/ /_\ \| |    | |\/| || /_\ \|   / / /_\ \\___ \ ")
    print(r"|  _  || |___ | |  | ||  _  || |\ \|  _  | ___) |")
    print(r"|_| |_||_____||_|  |_||_| |_||_| \_\_| |_||____/ ")
    print(f"{YELLOW}  ==============================================")
    print(f"{WHITE}       FIREBASE SECURITY TESTER BY ALMARAS")
    print(f"{YELLOW}  =============================================={RESET}")
    print("\n")

def test_security():
    # --- INPUT SECTION ---
    print(f"{YELLOW}[?] Please paste your Firebase Database URL{RESET}")
    print(f"{WHITE}(Example: https://your-db-default-rtdb.firebaseio.com/){RESET}")
    target_url = input(f"{CYAN}URL > {RESET}").strip()

    if not target_url:
        print(f"{RED}[-] Error: URL cannot be empty!{RESET}")
        return

    # --- AUTO-FIX URL (Dapat nagtatapos sa .json) ---
    # Kung ang user ay nag-paste lang ng root URL, idagdag natin ang test node
    if not target_url.endswith(".json"):
        if target_url.endswith("/"):
            target_url += "almaras_test.json"
        else:
            target_url += "/almaras_test.json"

    # Fake Data for Injection
    data = {
        "name": "Almaras Guard Hack",
        "balance": 99999.0,
        "email": "hacks@almaras.com",
        "timestamp": int(time.time())
    }

    print(f"\n{WHITE}[*] Connecting to: {target_url}{RESET}")
    print(f"{WHITE}[*] Checking Security...{RESET}")
    time.sleep(2) 

    try:
        # Susubukan nating mag-PATCH (update/inject)
        response = requests.patch(target_url, json=data)
        
        if response.status_code == 200:
            print(f"\n{RED}[!] RESULT: SECURITY VULNERABLE!{RESET}")
            print(f"{RED}[!] Almaras Hacks Data Injected Successfully.{RESET}")
            print(f"{YELLOW}[?] Tip: Update your Fbdb Rules immediately.{RESET}")
        elif response.status_code == 401 or response.status_code == 403:
            print(f"\n{GREEN}[+] RESULT: SECURITY ACTIVE!{RESET}")
            print(f"{GREEN}[+] Access Denied (Hacker Blocked by Rules).{RESET}")
            print(f"{CYAN}[#] Good job streamix! This database is safe.{RESET}")
        else:
            print(f"\n{YELLOW}[?] Unknown Status: {response.status_code}{RESET}")
            print(f"{WHITE}Response: {response.text}{RESET}")

    except Exception as e:
        print(f"\n{RED}[-] Error: {e}{RESET}")

# --- MAIN RUN ---
if __name__ == "__main__":
    show_banner()
    test_security()
    print(f"\n{WHITE}--- Security Test Finished ---{RESET}")
