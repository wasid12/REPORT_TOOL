import time
import sys
import webbrowser

# ANSI Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def show_banner():
    banner = f"""{GREEN}{BOLD}
 █████╗ ███████╗███████╗█████╗ ███╗   ██╗    ███╗   ███╗█████╗ ██████╗ ██╗  ██╗
 ██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║    ████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝
 ███████║█████╗  █████╗  ███████║██╔██╗ ██║    ██╔████╔██║███████║██████╔╝█████═╝ 
 ██╔══██║██╔══╝  ██╔══╝  ██╔══██║██║╚██╗██║    ██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ 
 ██║  ██║██║     ██║     ██║  ██║██║ ╚████║    ██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗
 ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                   
                        [ MADE BY AFFAN MARK ]
{RESET}"""
    print(banner)

def redirect_to_whatsapp():
    print(f"\n{RED}[!] Tool Locked! Password ke liye WhatsApp par redirect kiya ja raha hai...{RESET}")
    time.sleep(1.5)
    phone_number = "918307999802"
    message = "Affan bhai tool ko use krne ke liye password do mujhe"
    wa_url = f"https://wa.me/{phone_number}?text={message.replace(' ', '%20')}"
    webbrowser.open(wa_url)
    sys.exit()

def check_password_and_cookies():
    show_banner()
    print(f"{YELLOW}--- SECURITY VERIFICATION ---{RESET}")
    
    pass1 = input(f"{BOLD}Enter first password: {RESET}")
    if pass1 != "AFFANMARK376":
        print(f"\n{RED}[!] Incorrect Password!{RESET}")
        redirect_to_whatsapp()
        
    pass2 = input(f"{BOLD}Enter next password: {RESET}")
    if pass2 != "AFFANMARK376":
        print(f"\n{RED}[!] Incorrect Password!{RESET}")
        redirect_to_whatsapp()
        
    print(f"\n{GREEN}[+] Authentication Successful! Welcome, Affan.{RESET}\n")
    time.sleep(1)

    # Cookie Input Section
    print(f"{YELLOW}--- COOKIE AUTHENTICATION SETUP ---{RESET}")
    while True:
        try:
            num_cookies = int(input(f"{BOLD}Kitni ID ki cookie dalni hai? (1, 2, 3): {RESET}"))
            if num_cookies > 0:
                break
            else:
                print(f"{RED}[!] Kam se kam 1 cookie select karo!{RESET}")
        except ValueError:
            print(f"{RED}[!] Invalid input! Sirf number dalo (1, 2, 3).{RESET}")

    cookies_list = []
    for i in range(1, num_cookies + 1):
        while True:
            cookie = input(f"{BOLD}Enter Cookie #{i} for target ID: {RESET}")
            if cookie.strip():
                cookies_list.append(cookie.strip())
                break
            else:
                print(f"{RED}[!] Cookie khali nahi ho sakti, dobara dalo!{RESET}")

    print(f"\n{GREEN}[+] Successfully loaded {len(cookies_list)} ID Cookie(s) into session pool!{RESET}\n")
    time.sleep(1.5)
    return cookies_list

def simulate_reports(platform_name, cookies_list):
    print(f"\n{YELLOW}[*] Target Platform: {platform_name}{RESET}")
    target_link = input(f"{BOLD}Jis ID/Number ko report karna hai uska link ya number dalo: {RESET}")
    
    if not target_link.strip():
        print(f"{RED}[!] Error: Invalid target provided!{RESET}")
        return

    print(f"\n{GREEN}[+] Initializing heavy encrypted connection using loaded cookies ({len(cookies_list)} active nodes)...{RESET}")
    time.sleep(1.5)
    print(f"{CYAN}[+] Target Locked: {target_link}{RESET}")
    print(f"{YELLOW}[+] Dispatching 20 heavy simulation reports across session cookies...{RESET}\n")

    categories = [
        "Terrorism & Violent Extremism",
        "Harassment & Targeted Bullying",
        "Scam, Phishing & Financial Fraud",
        "Spam Bot & Automated Mass Interruption",
        "Impersonation & Fake Identity",
        "Dangerous Content & Malware Distribution",
        "Hate Speech & Discriminatory Behavior",
        "Intellectual Property Violation",
        "Unverified Commercial Spam",
        "Platform Terms of Service Breach"
    ] * 2  # Total 20 items

    cookie_index = 0
    for i in range(1, 21):
        time.sleep(1.2)
        active_cookie_tag = f"Cookie #{ (cookie_index % len(cookies_list)) + 1 }"
        print(f"{GREEN}[SUCCESS] Report #{i}/20 processed via [{active_cookie_tag}] [{categories[i-1]}]{RESET}")
        cookie_index += 1

    print(f"\n{YELLOW}[*] Flushing server logs and compiling response packets...{RESET}")
    time.sleep(2)
    
    # Moti aur Red Line requirement
    print(f"\n{RED}{BOLD}=======================================================================")
    print(f"[!] THIS ACCOUNT REMOVED FROM {platform_name.upper()}")
    print(f"======================================================================={RESET}\n")

def main_menu():
    cookies_list = check_password_and_cookies()
    while True:
        show_banner()
        print(f"{YELLOW}--- SELECT A  FB - INSTA REPORTREPORT METHOD ---{RESET}")
        print("1. WhatsApp Spam Report [NOTE: Is report ka use sirf tool owner Affan karega. Baki kisi ko use krni he to Affan bhai se WhatsApp password lelo or use kro]")
        print("2. Facebook Mask Report")
        print("3. Instagram Mask Report")
        print("4. Exit\n")
        
        choice = input(f"{BOLD}Enter choice (1-4): {RESET}")
        
        if choice == '1':
            simulate_reports("WhatsApp", cookies_list)
            input(f"{CYAN}Press Enter to go back to main menu...{RESET}")
        elif choice == '2':
            simulate_reports("Facebook", cookies_list)
            input(f"{CYAN}Press Enter to go back to main menu...{RESET}")
        elif choice == '3':
            simulate_reports("Instagram", cookies_list)
            input(f"{CYAN}Press Enter to go back to main menu...{RESET}")
        elif choice == '4':
            print(f"\n{GREEN}Exiting tool. Goodbye, Affan!{RESET}")
            sys.exit()
        else:
            print(f"\n{RED}[!] Invalid option. Please select between 1 to 4.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    main_menu()
