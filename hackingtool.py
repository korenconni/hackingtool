#!/usr/bin/env python3
"""HackingTool - A collection of hacking tools for security researchers.

This is the main entry point for the HackingTool application.
All tools are organized into categories and can be installed/run
directly from this menu-driven interface.
"""

import os
import sys
import subprocess
from time import sleep

# Ensure we're running on a supported platform
if sys.platform not in ("linux", "linux2", "darwin"):
    print("[!] HackingTool is only supported on Linux and macOS.")
    sys.exit(1)

# Ensure Python 3.6+
if sys.version_info < (3, 6):
    print("[!] Python 3.6 or higher is required.")
    sys.exit(1)


BANNER = r"""
 ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗
 ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝
 ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
 ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
 ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
 ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
          ████████╗ ██████╗  ██████╗ ██╗
          ╚══██╔══╝██╔═══██╗██╔═══██╗██║
             ██║   ██║   ██║██║   ██║██║
             ██║   ██║   ██║██║   ██║██║
             ██║   ╚██████╔╝╚██████╔╝███████╗
             ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
"""

CATEGORIES = [
    "Anonymous Surfing Tools",
    "Information Gathering Tools",
    "Wordlist Generator",
    "Wireless Attack Tools",
    "SQL Injection Tools",
    "Phishing Attack Tools",
    "Web Attack Tools",
    "Post Exploitation Tools",
    "Forensic Tools",
    "Payload Creator",
    "Exploit Framework",
    "Reverse Engineering Tools",
    "DDOS Attack Tools",
    "Remote Administrator Tools (RAT)",
    "XSS Attack Tools",
    "Steganography Tools",
    "SocialMedia Brute Forcing",
    "Android Hacking Tools",
    "IDN Homograph Attack",
    "Email Spoofing Tools",
    "Hash Cracking Tools",
    "Wifi Deauthenticate",
    "SocialMedia Finder",
    "Payload Injector",
    "Server Hacking Tools",
    "Other Tools",
]


def clear_screen():
    """Clear the terminal screen."""
    os.system("clear" if os.name == "posix" else "cls")


def print_banner():
    """Print the application banner."""
    clear_screen()
    print("\033[1;31m" + BANNER + "\033[0m")
    print("\033[1;33m" + " " * 10 + "Fork of Z4nzu/hackingtool" + "\033[0m")
    print("\033[1;34m" + " " * 10 + "Use responsibly and ethically!" + "\033[0m")
    print()


def print_menu():
    """Display the main category menu."""
    print("\033[1;32m[*] Select a category:\033[0m")
    print()
    for idx, category in enumerate(CATEGORIES, start=1):
        print(f"  \033[1;36m[{idx:02d}]\033[0m {category}")
    print()
    print("  \033[1;31m[00]\033[0m Exit")
    print()


def check_root():
    """Warn the user if not running as root."""
    if os.geteuid() != 0:
        print("\033[1;33m[!] Warning: Some tools may require root privileges.\033[0m")
        sleep(1)


def get_user_input(prompt="Enter your choice: "):
    """Safely get input from the user."""
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\n\033[1;31m[!] Interrupted. Exiting...\033[0m")
        sys.exit(0)


def main():
    """Main application loop."""
    check_root()

    while True:
        print_banner()
        print_menu()

        choice = get_user_input("\033[1;32mhackingtool~# \033[0m")

        if choice == "00" or choice.lower() in ("exit", "quit", "q"):
            print("\n\033[1;31m[!] Exiting HackingTool. Goodbye!\033[0m")
            sys.exit(0)

        if not choice.isdigit():
            print("\033[1;31m[!] Invalid input. Please enter a number.\033[0m")
            sleep(1)
            continue

        choice_int = int(choice)
        if 1 <= choice_int <= len(CATEGORIES):
            selected = CATEGORIES[choice_int - 1]
            print(f"\n\033[1;33m[*] Loading: {selected}...\033[0m")
            sleep(0.5)
            # Category modules will be imported and dispatched here
            print(f"\033[1;31m[!] '{selected}' module not yet implemented.\033[0m")
            sleep(1.5)
        else:
            print("\033[1;31m[!] Invalid choice. Please select a valid option.\033[0m")
            sleep(1)


if __name__ == "__main__":
    main()
