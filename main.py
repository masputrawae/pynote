from apps import core

def main():
    core.main_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n!Goodbye...")
