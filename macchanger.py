#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Coding by xberkay-o
import os
import sys
import time
from os import system

system("cls||clear")

def rainbow_text(text, delay=0.1):
    colors = [
        "\033[31m", "\033[33m", "\033[32m", "\033[36m", "\033[34m", "\033[35m", "\033[37m",
    ]

    for i in range(len(text)):
        char = text[i]
        color = colors[i % len(colors)]
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write("\033[0m")
    sys.stdout.write("\n")

if __name__ == "__main__":
    rainbow_text("Coding by xberkay-o")

print("""
\033[35mWelcome to the MAC Address Changer Program / xberkay-o \033[0m

\033[32m 1) Set MAC Address to Random\033[0m
\033[31m 2) Set MAC Address Manually\033[0m
\033[94m 3) Restore Original MAC Address\033[0m
""")

operation_no = input("Enter Operation No: ")

if operation_no == "1":
    os.system("ifconfig eth0 down")
    os.system("macchanger -r eth0")
    os.system("ifconfig eth0 up")
    print("\033[32m New MAC Address Set to Random. \033[0m")

elif operation_no == "2":
    mac_address = input("\033[31m Enter New MAC Address: ")
    os.system("ifconfig eth0 down")
    os.system("macchanger --mac " + mac_address + " eth0")
    os.system("ifconfig eth0 up")
    print("\033[31m New MAC Address Set Manually. \033[0m")

elif operation_no == "3":
    os.system("ifconfig eth0 down")
    os.system("macchanger -p eth0")
    os.system("ifconfig eth0 up")
    print("\033[94m MAC Address Restored to Original. \033[0m")

else:
    print("Error! Please use Kali Linux.")
