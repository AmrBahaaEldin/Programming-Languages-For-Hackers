#!/usr/bin/python3
#name=input("what s your name:")
#print(f"dear {name} the service is not available")
print("________________________________________________")
#file=open("/home/sonic/Desktop/LinuxUsage/import_1","w")
#file.write("this is new line from python")
#file.close()

print("________________________________________________")
#file=open("/home/sonic/Desktop/LinuxUsage/import_1","r")
#print(file.read())

#print(file.read())
import os
target=input("pls enter domain to scan :")
# using && or ; include ""
os.system(f"nmap {target} && free" )

os.system("free ; df -h ")