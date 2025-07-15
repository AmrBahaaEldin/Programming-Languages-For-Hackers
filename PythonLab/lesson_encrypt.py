import rsa
message="help me for cia".encode()
publicKey,privateKey=rsa.newkeys(512)
cipher=rsa.encrypt(message,publicKey)
print(cipher)
decipher=rsa.decrypt(cipher,privateKey)
print(decipher)
print("__________________________________________________")