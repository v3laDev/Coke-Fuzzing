import argparse
import requests
import os
from time import sleep
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

def show_banner():
    banner = r"""
 .d8888b.           888                    8888888888                         
d88P  Y88b          888                    888                                
888    888          888                    888                                
888         .d88b.  888  888  .d88b.       8888888 888  888 88888888 88888888 
888        d88""88b 888 .88P d8P  Y8b      888     888  888    d88P     d88P  
888    888 888  888 888888K  88888888      888     888  888   d88P     d88P   
Y88b  d88P Y88..88P 888 "88b Y8b.          888     Y88b 888  d88P     d88P    
 "Y8888P"   "Y88P"  888  888  "Y8888       888      "Y88888 88888888 88888888
 """
    print(Fore.RED + banner + Style.RESET_ALL)

def find_subdomains(domain, subdomains, delay, log_file=None):
    print(f"Searching subdomains for {domain}...")
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            print(f"Trying URL: {url}")
            requests.get(url)
            print(f"Subdomain found: {url}")
            if log_file:
                log_file.write(f"Subdomain found: {url}\n")
        except requests.exceptions.InvalidURL:
            print(f"Invalid URL: {url}")
            if log_file:
                log_file.write(f"Invalid URL: {url}\n")
        except requests.ConnectionError:
            pass
        sleep(delay)

def find_subdirectories(domain, subdirectories, delay, log_file=None):
    print(f"Searching subdirectories for {domain}...")
    for subdirectory in subdirectories:
        url = f"http://{domain}/{subdirectory}"
        try:
            requests.get(url)
            print(f"Subdirectory found: {url}")
            if log_file:
                log_file.write(f"Subdirectory found: {url}\n")
        except requests.ConnectionError:
            pass
        sleep(delay)

def main():
    parser = argparse.ArgumentParser(
        description='Coke Fuzzing Tool',
        add_help=False,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('domain', type=str, nargs='?', help=argparse.SUPPRESS)
    parser.add_argument('--subdomains', type=str, help='File with list of subdomains.')
    parser.add_argument('--subdirectories', type=str, help='File with list of subdirectories.')
    parser.add_argument('-all', action='store_true', help='Search both subdomains and subdirectories.')
    parser.add_argument('--mode', type=str, choices=['low', 'medium', 'fast'], default='medium', help='Speed mode: low, medium, fast.')
    parser.add_argument('--logs', action='store_true', help='Save results to a log file.')
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit.')

    args = parser.parse_args()

    if args.help or not args.domain:
        show_banner()
        print("\nOptions:")
        for action in parser._actions:
            if action.help != argparse.SUPPRESS:
                print(f"  {', '.join(action.option_strings)}: {action.help}")
        print("\nExample usage:\n  python app.py example.com --subdomains subdomains.txt --subdirectories subdirectories.txt --mode fast --logs")
        return

    delay = {'low': 1.0, 'medium': 0.5, 'fast': 0.1}[args.mode]

    if args.logs:
        os.makedirs('logs', exist_ok=True)
        log_path = os.path.join('logs', f"{args.domain}.log")
        log_file = open(log_path, 'w')
    else:
        log_file = None

    try:
        if args.all:
            if args.subdomains:
                with open(args.subdomains, 'r') as f:
                    subdomains = f.read().splitlines()
                find_subdomains(args.domain, subdomains, delay, log_file)

            if args.subdirectories:
                with open(args.subdirectories, 'r') as f:
                    subdirectories = f.read().splitlines()
                find_subdirectories(args.domain, subdirectories, delay, log_file)
        else:
            if args.subdomains:
                with open(args.subdomains, 'r') as f:
                    subdomains = f.read().splitlines()
                find_subdomains(args.domain, subdomains, delay, log_file)

            if args.subdirectories:
                with open(args.subdirectories, 'r') as f:
                    subdirectories = f.read().splitlines()
                find_subdirectories(args.domain, subdirectories, delay, log_file)
    finally:
        if log_file:
            log_file.close()

if __name__ == "__main__":
    main()
