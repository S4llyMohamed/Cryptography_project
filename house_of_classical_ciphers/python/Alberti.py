import sys

external_circle = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
internal_circle = "ZYXWVUTSRQPONMLKJIHGFEDCBAÑ"

def encrypt_alberti(text, key):
    cipher = ""
    key_index = external_circle.index(key.upper())
    for char in text:
        if char == " ":
            cipher += " "
            continue
        external_index = external_circle.index(char)
        cipher += internal_circle[(external_index + key_index) % len(external_circle)]
    return cipher

def decrypt_alberti(ciphertext, key):
    text = ""
    key_index = external_circle.index(key.upper())
    for char in ciphertext:
        if char == " ":
            text += " "
            continue
        internal_index = internal_circle.index(char)
        text += external_circle[(internal_index - key_index) % len(external_circle)]
    return text

def crack_alberti(ciphertext, key):
    return decrypt_alberti(ciphertext, key)

def main():
    if len(sys.argv) != 4:
        print("Usage: python alberti.py <operation> <text> <key>")
        sys.exit(1)

    operation = sys.argv[1].lower()
    input_text = sys.argv[2].upper()
    key = sys.argv[3].upper()

    if key not in external_circle:
        print("Invalid key. Please enter a single character from the external alphabet.")
        sys.exit(1)

    if operation == "encrypt":
        result = encrypt_alberti(input_text, key)
        print(result)

    elif operation == "decrypt":
        result = decrypt_alberti(input_text, key)
        print(result)

    elif operation == "crack":
        result = crack_alberti(input_text, key)
        print(result)

    else:
        print("Invalid operation. Choose from: encrypt, decrypt, crack.")
        sys.exit(1)

if __name__ == "__main__":
    main()
