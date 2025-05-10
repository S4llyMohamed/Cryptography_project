import sys

def caesar_encrypt(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

def caesar_crack(text):
    possibilities = []
    for key in range(1, 26):
        decrypted = caesar_decrypt(text, key)
        possibilities.append(f"Key {key}: {decrypted}")
    return "\n".join(possibilities)

if __name__ == "__main__":
    mode = sys.argv[1]  # encrypt / decrypt / crack
    text = sys.argv[2]
    if mode == "encrypt" or mode == "decrypt":
        key = int(sys.argv[3])
        result = caesar_encrypt(text, key) if mode == "encrypt" else caesar_decrypt(text, key)
    elif mode == "crack":
        result = caesar_crack(text)
    else:
        result = "Invalid mode"
    print(result)
