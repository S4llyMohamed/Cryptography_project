import sys

external_circle = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
internal_circle = "ZYXWVUTSRQPONMLKJIHGFEDCBAÑ"

def encrypt(text, key):
    cipher = ""
    key_index = external_circle.index(key.upper())
    for char in text:
        if char == " ":
            cipher += " "
            continue
        external_index = external_circle.index(char)
        cipher += internal_circle[(external_index + key_index) % len(external_circle)]
    return cipher

def decrypt(ciphertext, key):
    text = ""
    key_index = external_circle.index(key.upper())
    for char in ciphertext:
        if char == " ":
            text += " "
            continue
        internal_index = internal_circle.index(char)
        text += external_circle[(internal_index - key_index) % len(external_circle)]
    return text

def crack(ciphertext, key):
    decrypted_text = decrypt(ciphertext, key)
    print(f"Cracked text: {decrypted_text}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <KEY> <TEXT_TO_ENCRYPT> <CIPHERTEXT_TO_CRACK>")
        sys.exit(1)

    key = sys.argv[1].upper()
    text = sys.argv[2].upper()
    to_crack = sys.argv[3].upper()

    cipher = encrypt(text, key)
    print(f"Encrypted: {cipher}")

    decrypted = decrypt(cipher, key)
    print(f"Decrypted: {decrypted}")

    crack(to_crack, key)
