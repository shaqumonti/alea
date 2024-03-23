from colorama import Fore, Back, Style

def cprint(text, color):
    """Prints text in color."""
    if color == 'red':
        print(Fore.RED + text + Style.RESET_ALL)
    elif color == 'green':
        print(Fore.GREEN + text + Style.RESET_ALL)
    elif color == 'yellow':
        print(Fore.YELLOW + text + Style.RESET_ALL)
    elif color == 'blue':
        print(Fore.BLUE + text + Style.RESET_ALL)
    elif color == 'magenta':
        print(Fore.MAGENTA + text + Style.RESET_ALL)
    elif color == 'cyan':
        print(Fore.CYAN + text + Style.RESET_ALL)
    elif color == 'white':
        print(Fore.WHITE + text + Style.RESET_ALL)
    elif color == 'black':
        print(Fore.BLACK + text + Style.RESET_ALL)
    else:
        print(text)

cprint(f"not found (By.TAG_NAME): '{name}'", 'yellow')
