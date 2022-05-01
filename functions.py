import pyfiglet
import os

def banner():
    banner = pyfiglet.figlet_format("WireAttack")
    return banner

def menu():
    print("""Menu:
    1) Enable Monitor Mode
    2) Disable Monitor Mode
    3) Installing Tools
    4) update system""")

    option = input("\nChoice > ")

    if option == 4:
        os.system("sudo apt-get update")
