from colorama import init, Fore, Back, Style

init(autoreset=True)  # maps ANSI color code to OS system

messages = [
    'Colorama test case ',
    (Fore.LIGHTYELLOW_EX + Style.BRIGHT + Back.MAGENTA + 'Colored message on terminal!!!!!'),
    'Another message but not colored'
]

for m in messages:
    print(m)
