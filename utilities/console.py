from colorama import init, Fore, Back, Style
init(autoreset=True)

def printInfoCyan(key, value):
    print(Style.BRIGHT + Fore.CYAN + key + Style.RESET_ALL + Fore.LIGHTCYAN_EX + value)

def printInfoMagenta(key, value):
    print(Style.BRIGHT + Fore.MAGENTA + key + Style.RESET_ALL + Fore.LIGHTMAGENTA_EX + value)

def printInfoYellow(key, value):
    print(Style.BRIGHT + Fore.YELLOW + key + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + value)
