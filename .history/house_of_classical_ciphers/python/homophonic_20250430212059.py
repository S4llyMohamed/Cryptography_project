# homophonic.py
import sys
import random

key = {
    'A': ['@', '4'],
    'B': ['8'],
    'C': ['('],
    'D': ['|)'],
    'E': ['3', '€'],
    'F': ['#'],
    'G': ['6'],
    'H': ['#'],
    'I': ['1', '!'],
    'J': ['_|'],
    'K': ['<'],
    'L': ['|_'],
    'M': ['^^'],
    'N': ['^'],
    'O': ['0'],
    'P': ['|*'],
    'Q': ['(,)'],
    'R': ['|2'],
    'S': ['$', '5'],
    'T': ['7'],
    'U': ['(_)'],
    'V': ['\\/'],
    'W': ['\\/\\/'],
    'X': ['%'],
    'Y': ['`/'],
    'Z': ['2']
}

reverse_key = {}
for letter, symbols in key.items():
    for sym in symbols:
        reverse_key[sym] = letter

def encrypt(text):
    result = ''
    for char in text.upper():
        if char in key:
            result += random.choice(key[char]) + ' '
        else:
            result += char + ' '
    return result.strip()

def decrypt(text):
    symbols = text.split()
    result = ''
    for sym in symbols:
        result += reverse_key.get(sym, '?')
    return result

def crack(text):
    return decrypt(text)

if __name__ == "__main__":
    mode = sys.argv[1]  # encrypt / decrypt / crack
    text = sys.argv[2]

    if mode == "encrypt":
        print(encrypt(text))
    elif mode == "decrypt":
        print(decrypt(text))
    elif mode == "crack":
        print(crack(text))
    else:
        print("Invalid mode")
