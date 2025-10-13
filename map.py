import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

#print(f"chars: {chars}")
#print(f"keys: {keys}")

#Encryption 
plaintext = input("Enter message to encrypt: ")
cyphertext = "" 

for letter in plaintext:
    index = chars.index(letter)
    cyphertext += keys[index]

print(f"Original message: {plaintext}")
print(f"Encrypted message: {cyphertext}")

#Decryption
cyphertext = input("Enter message to Decrypt: ")
plaintext = "" 

for letter in cyphertext:
    index = keys.index(letter)
    plaintext += chars[index]

print(f"Encrypted message: {cyphertext}")
print(f"Original message: {plaintext}")