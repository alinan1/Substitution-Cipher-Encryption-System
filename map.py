import secrets
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

keys = chars.copy()
secrets.SystemRandom().shuffle(keys)

#print(f"chars: {chars}")
#print(f"keys: {keys}")


encrypt_map = dict(zip(chars, keys))
decrypt_map = dict(zip(keys, chars))

#Encryption 
def encrypt(plain_text):
    cipher_text = ""
    for char in plain_text:
        cipher_text += encrypt_map[char]
    return cipher_text

# Decryption
def decrypt(cipher_text):
    plain_text = ""
    for char in cipher_text:
        plain_text += decrypt_map[char]
    return plain_text

if __name__ == "__main__":
    plain_text = input("Enter the plain text: ")
    cipher_text = encrypt(plain_text)
    decrypted_text = decrypt(cipher_text)

    print(f"Plain Text: {plain_text}")
    print(f"Cipher Text: {cipher_text}")
    print(f"Decrypted Text: {decrypted_text}")