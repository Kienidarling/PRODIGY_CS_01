import time
import os

# Optional: Install colorama for colors (only once needed)
try:
    from colorama import init, Fore, Style
except ImportError:
    print("Installing colorama for colored output...")
    os.system('pip install colorama')
    from colorama import init, Fore, Style

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fancy_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def banner():
    print(Fore.YELLOW + Style.BRIGHT)
    print("╔══════════════════════════════════════╗")
    print("║ ✨Welcome to Kiile'S Caesar Cipher✨  ║")
    print("╚══════════════════════════════════════╝" + Style.RESET_ALL)
    print()

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        clear()
        banner()
        fancy_print(Fore.CYAN + "🔐 Let's keep your secrets safe...\n")

        choice = input(Fore.GREEN + "Would you like to (E)ncrypt or (D)ecrypt? (Type Q to quit): ").strip().upper()

        if choice == 'Q':
            fancy_print(Fore.YELLOW + "\n👋 Thank you for using Caesar Cipher Pro. Stay mysterious!", 0.05)
            break

        if choice not in ['E', 'D']:
            fancy_print(Fore.RED + "Oops! Invalid choice. Try again...\n")
            time.sleep(1.5)
            continue

        message = input(Fore.MAGENTA + "💌 Enter your message: ").strip()
        shift_input = input(Fore.BLUE + "🔢 Enter shift value (e.g., 3): ")

        if not shift_input.isdigit():
            fancy_print(Fore.RED + "🚫 Shift must be a number. Try again!", 0.04)
            time.sleep(1.5)
            continue

        shift = int(shift_input)

        if choice == 'E':
            result = encrypt(message, shift)
            fancy_print(Fore.YELLOW + "\n✅ Encrypted Message:\n", 0.04)
            fancy_print(Fore.WHITE + Style.BRIGHT + result + "\n", 0.02)
        else:
            result = decrypt(message, shift)
            fancy_print(Fore.YELLOW + "\n✅ Decrypted Message:\n", 0.04)
            fancy_print(Fore.WHITE + Style.BRIGHT + result + "\n", 0.02)

        input(Fore.GREEN + "\nPress Enter to continue...")

if __name__ == "__main__":
    main()
