import random
import itertools
import math
import re
import json
import sys

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def strip_repeats(s):
    return "".join(dict.fromkeys(s))

def answerize(s):
    regex = re.compile('[^a-zA-Z]')
    ret = regex.sub('', s)
    return ret.upper()

def letter_to_num(x):
    return ord(x.upper()) - 65

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
        plaintext = ''
        for i in range(0, len(binary), 5):
            chunk = binary[i:i+5]
            if len(chunk) == 5:
                plaintext += debaconify(chunk)
        return plaintext

    def crack(self, ciphertext):
        results = []
        max_key_len = len(ciphertext) // 2
        for key_len in range(2, max_key_len + 1):
            perms = itertools.permutations(range(key_len))
            for perm in perms:
                try:
                    decrypted = self.decryptMessageWithKeyOrder(ciphertext, perm)
                    results.append({
                        "key_length": key_len,
                        "order": perm,
                        "decrypted": decrypted
                    })
                except Exception:
                    continue
        return results

    def decryptMessageWithKeyOrder(self, cipher, key_order):
        msg = ""
        msg_len = float(len(cipher))
        msg_lst = list(cipher)
        col = len(key_order)
        row = int(math.ceil(msg_len / col))
        dec_cipher = []
        for _ in range(row):
            dec_cipher += [[None] * col]
        msg_indx = 0
        for k in key_order:
            for r in range(row):
                if msg_indx < len(msg_lst):
                    dec_cipher[r][k] = msg_lst[msg_indx]
                    msg_indx += 1
        try:
            msg = ''.join(sum(dec_cipher, []))
        except TypeError:
            raise TypeError("Error during cracking.")
        null_count = msg.count('_')
        return msg[:-null_count] if null_count > 0 else msg

def main():
   
    if len(sys.argv) != 4:
        print("Usage: python script.py <operation> <input_text>")
        sys.exit(1)

    operation = sys.argv[1]  
    input_text = sys.argv[2]  

    baconian = Baconian()

    if operation == "encrypt":
        result = baconian.encrypt(input_text)
        print( result)

    elif operation == "decrypt":
        result = baconian.decrypt(input_text)
        print( result)

    elif operation == "crack":
        results = baconian.crack(input_text)
        print("Possible decrypted texts:")
        print(json.dumps(results, indent=2))

    else:
        print("Invalid operation.")
        sys.exit(1)

if __name__ == "__main__":
    main()