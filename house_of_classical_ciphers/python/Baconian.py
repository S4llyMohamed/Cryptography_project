import re
import random
import sys
import json

# Alphabet constant
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Utility functions
def strip_repeats(s):
    return "".join(dict.fromkeys(s))

def answerize(s):
    regex = re.compile('[^a-zA-Z]')
    ret = regex.sub('', s)
    return ret.upper()

def letter_to_num(x):
    return (ord(x.upper()) - 65)

def A0Z25(x):
    return chr((x % 26) + 65)

def baconify(s):
    ret = ''
    a = letter_to_num(s)
    if a >= 9:
        a -= 1
    if a >= 20:
        a -= 1
    for i in range(5):
        ret += str(a % 2)
        a //= 2
    return ret[::-1]

def debaconify(s):
    a = sum(pow(2, 4 - i) * int(s[i]) for i in range(len(s)))
    if a >= 8:
        a += 1
    if a >= 20:
        a += 1
    return A0Z25(a)

class Baconian:
    
    def __init__(self):
        self.zero_set = set('ABCDEFGHIJKLM')
        self.one_set = set('NOPQRSTUVWXYZ')

    def encrypt(self, plaintext):
        plaintext = answerize(plaintext)
        binary = ''.join(baconify(c) for c in plaintext)
        ciphertext = ''.join(
            random.choice(list(self.zero_set)) if bit == '0' else random.choice(list(self.one_set))
            for bit in binary
        )
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = answerize(ciphertext)
        binary = ''
        for char in ciphertext:
            if char in self.zero_set:
                binary += '0'
            elif char in self.one_set:
                binary += '1'
            else:
                continue
        plaintext = ''
        for i in range(0, len(binary), 5):
            chunk = binary[i:i+5]
            if len(chunk) == 5:
                plaintext += debaconify(chunk)
        return plaintext

# Main program loop for command-line interaction
if len(sys.argv) < 2:
    print("Usage: python script.py <operation> [text]")
    sys.exit(1)

operation = sys.argv[1].strip()
cipher = Baconian()

if operation == '1':  # Encrypt
    if len(sys.argv) < 4:
        print("Usage for encryption: python script.py 1 <plaintext>")
        sys.exit(1)
    plaintext = sys.argv[2]
    encrypted = cipher.encrypt(plaintext)
    print(json.dumps({"encrypted_ciphertext": encrypted}))

elif operation == '2':  # Decrypt
    if len(sys.argv) < 4:
        print("Usage for decryption: python script.py 2 <ciphertext>")
        sys.exit(1)
    ciphertext = sys.argv[2]
    decrypted = cipher.decrypt(ciphertext)
    print(json.dumps({"decrypted_plaintext": decrypted}))

elif operation == '3':  # Crack
    if len(sys.argv) < 3:
        print("Usage for cracking: python script.py 3 <ciphertext>")
        sys.exit(1)
    ciphertext = sys.argv[2]
    cracked = cipher.decrypt(ciphertext)  # Assumes classic Baconian encoding
    print(json.dumps({"cracked_plaintext": cracked}))

elif operation == '4':  # Exit
    print("Exiting...")
    sys.exit(0)

else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")
    sys.exit(1)
