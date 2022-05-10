import pyfiglet
import os

enter = "\n"

def banner():
    res = pyfiglet.figlet_format("WireAttack")
    return res

def is_crunch():
    installed = os.popen("dpkg -s crunch")
    for line in installed.readlines():
        if "Status: install ok installed" in line:
            return line
