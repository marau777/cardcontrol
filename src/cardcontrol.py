#!/usr/bin/env python3
from gpiozero import Servo
from time import sleep
import socket
import sys
from enum import Enum
import subprocess

def usage():
    print("USAGE:")
    print("python3 cardcontrol.py insert")
    print("python3 cardcontrol.py remove")
    print("python3 cardcontrol.py update")
    return

def get_ip_address():
 ip_address = '';
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 ip_address = s.getsockname()[0]
 s.close()
 return ip_address

# Print usage if no arguments given.
nArgs = len(sys.argv)
if (nArgs <= 1):
    usage()
    exit()

print("\nApp: ")
for i in range(0, nArgs):
    print(sys.argv[i], end = " ")

print("\nIP Address:", get_ip_address())

servo = Servo(18)

if (sys.argv[1] == "insert"):
    print("Command: Card Inserted\n")
    servo.min()
    sleep(1.0)

if (sys.argv[1] == "remove"):
    print("Command: Card Removed\n")
    servo.max()
    sleep(1.0)

if (sys.argv[1] == "update"):
    print("Command: Software Update\n")
    updateCmd = "cd ~/git/cardcontrol | git pull --rebase"
    subprocess.run(updateCmd, shell=True) 

sys.stdout.flush()