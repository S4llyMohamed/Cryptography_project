import math
import itertools
import sys
import json

def encrypt(msg, key):
    cipher = ""
    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1
    return cipher

def decrypt(cipher, key):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")
    null_count = msg.count('_')
    return msg[:-null_count] if null_count > 0 else msg

def decryptMessageWithKeyOrder(cipher, key_order):
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

def crack(ciphertext):
    results = []
    max_key_len = len(ciphertext) // 2
    for key_len in range(2, max_key_len + 1):
        perms = itertools.permutations(range(key_len))
        for perm in perms:
            try:
                decrypted = decryptMessageWithKeyOrder(ciphertext, perm)
                results.append({
                    "key_length": key_len,
                    "order": perm,
                    "decrypted": decrypted
                })
            except Exception:
                continue
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:\n  encrypt <plaintext> <key>\n  decrypt <ciphertext> <key>\n  crack <ciphertext>")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "encrypt" and len(sys.argv) == 4:
        plaintext = sys.argv[2].replace(" ", "")
        key = sys.argv[3]
        result = encrypt(plaintext, key)
        print(result)

    elif mode == "decrypt" and len(sys.argv) == 4:
        ciphertext = sys.argv[2]
        key = sys.argv[3]
        result = decrypt(ciphertext, key)
        print(result)

    elif mode == "crack" and len(sys.argv) == 3:
        ciphertext = sys.argv[2]
        results = crack(ciphertext)
        print(json.dumps(results, indent=2))

    else:
        print("Invalid arguments.")
