import pyfiglet
from termcolor import colored

enter = "\n"

def banner():
    bannerr = pyfiglet.figlet_format("WireAttack")
    print(colored("{0}".format(bannerr), "red"))
