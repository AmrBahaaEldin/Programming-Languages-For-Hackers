#!usr/bin/python3
import rsa 
publicKey,privateKey=rsa.newkeys(512)
print(f"{publicKey} && {privateKey}")
print("__________________________________________________")
