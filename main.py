import tomllib
import os
import json

# == CLEAN TERMINAL ==
def cln_screen():
    try:
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system("cls")
        else:
            raise NotImplementedError(f"Dont Know how to clear for OS: {os.name}")
    except Exception as e:
        print("!Failed to Clean Screen! | Error: ", e)

# == LOAD CONFIG & DATA ==
def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print("Error: ", e)
        return {}

def load_toml(path):
    try:
        with open(path, "rb") as f:
            return tomllib.load(f)
    except Exception as e:
        print("!Error: ", e)
        return {}

def menus_stdout(menu):
    menus = load_toml("config/menus.toml")

    for i, name in enumerate(menus[menu], start=1):
        print(f"[{i}] {name}")
    
    print("_"*60)
    if menu == "main":
        print("[0]. Exit")
    else:
        print("[0]. Back")

def header_ui():
    user_data = load_json("data/user.json")
    username = user_data["username"]
    git = user_data["git"]

    print("="*60)
    print(f"User Name\t| {username}")
    print(f"Git Branch\t| {git['branch']}")
    print(f"Git Remote\t| {git['remote']}")
    print(f'Git Status\t| {git['status']}')
    print("_"*60)

def main():
    while True:
        cln_screen()
        header_ui()
        menus_stdout("main")

        try:
            input_opt = int(input(">>> "))

            if input_opt == 1:
                print("Opsi 1 Dipilih")
            elif input_opt == 2:
                print("Opsi 2 Dipilih")
            elif input_opt == 3:
                print("Opsi 3 Dipilih")
            elif input_opt == 4:
                print("Opsi 4 Dipilih")
            elif input_opt == 5:
                print("Opsi 5 Dipilih")
            elif input_opt == 0:
                print("Opsi 6 Dipilih. !Goodbye")
                break
            else:
                print("1 - 6 Only. Not Found Option ", input_opt)
        
        except ValueError:
            print("!Number Only...")

        input("!Press Enter to Continue...")

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        print("\n!Goodbye...")

