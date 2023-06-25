import os
from colorama import init, Fore, Style

init(autoreset=True)

def printInfoCyan(key, value):
    print(Style.BRIGHT + Fore.CYAN + key + Style.RESET_ALL + Fore.LIGHTCYAN_EX + value)

def printInfoMagenta(key, value):
    print(Style.BRIGHT + Fore.MAGENTA + key + Style.RESET_ALL + Fore.LIGHTMAGENTA_EX + value)

def printInfoYellow(key, value):
    print(Style.BRIGHT + Fore.YELLOW + key + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + value)

def printFileSize(key, filename):
    size = round(os.path.getsize(filename)/ 1024 ** 1, 3)
    print(Style.BRIGHT + Fore.GREEN + key + Style.RESET_ALL + Fore.LIGHTGREEN_EX + filename + Fore.LIGHTWHITE_EX + " (" + str(size) + "kb)")
