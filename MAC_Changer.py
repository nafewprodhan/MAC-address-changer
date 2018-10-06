#!/usr/bin/env/python
#python3
import subprocess
Interface = input("Enter your Interface card name: ")
MAC_Address = input("Enter MAC address you want to change: ")
subprocess.call("ifconfig " +Interface + " down",shell=True)
subprocess.call("ifconfig " +Interface + " hw ether " +MAC_Address,shell=True)
subprocess.call("ifconfig " +Interface + " up",shell=True)
subprocess.call("ifconfig " +Interface,shell=True)
