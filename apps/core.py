import readchar

from colorama import Fore, Style, init
from .utils import date, load_data, cln_screen

def user_header():
    data = load_data("../data/config.toml", "toml")
    username = data['username']
    git_branch = data["git"]["branch"]
    git_remote = data["git"]["remote"]
    git_ssh = data["git"]["ssh"]
    base_path = data["vault"]["base_path"]

    separator = Fore.BLUE + Style.BRIGHT + "="*60
    print(f'''{separator}
{"PY NOTES".center(60)}
{separator}
[*] User Name\t| {username}
[*] Git Branch\t| {git_branch}
[*] Git Remote\t| {git_remote}
[*] Git SSH\t| {git_ssh}
[*] Note Path\t| {base_path}
{separator}''')

def create_menu():
    config = load_data("../data/config.toml", "toml")
    notes = config["notes"]
    menus = []

    for i, opt in enumerate(notes):
        menus.append(opt["type"])
    menus.append("BACK")

    opt = select_option(menus)

    if not opt == len(menus) - 1:
        for field, prompt in notes[opt]["field"].items():
            value = input(f"{prompt}")

def select_option(menus):
    init(autoreset=True)
    index = 0

    while True:
        cln_screen()
        user_header()
        print(Fore.CYAN + Style.BRIGHT + "=== OPTION ===")
        for i, opt in enumerate(menus):
            if i == index:
                print(Fore.YELLOW + Style.BRIGHT + f"[{i + 1}] {opt}👈")
            else:
                print(Fore.WHITE + f"[{i + 1}] {opt}")

        key = readchar.readkey()
        if key == readchar.key.UP or key == "k":
            index = (index - 1) % len(menus)
        elif key == readchar.key.DOWN or key == "j":
            index = (index + 1) % len(menus)
        elif key == readchar.key.ENTER:
            return index

def main_menu():
    menus = ["CREATE", "READ", "UPDATE", "DELETE", "EXIT"]
    while True:
        cln_screen()
        opt = select_option(menus)
        if opt == 0:
            print("GO CREAD")
            create_menu()
        elif opt == 1:
            print("GO READ")
        elif opt == 2:
            print("GO UPDATE")
        elif opt == 3:
            print("GO DELETE")
        elif opt == 4:
            print("!Goodbye")
            break

