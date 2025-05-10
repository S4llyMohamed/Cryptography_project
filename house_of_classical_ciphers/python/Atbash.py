import sys

def atbash_cipher(text):
    """
    Encrypts or decrypts text using Atbash cipher.
    Since Atbash is symmetric, the same function works for both.
    """
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(65 + (25 - (ord(char) - 65)))
            else:
                result += chr(97 + (25 - (ord(char) - 97)))
        else:
            result += char  # Leave other characters unchanged
    return result

def encrypt(text):
    return atbash_cipher(text)

def decrypt(text):
    return atbash_cipher(text)

def crack(cipher_text):
    print("Attempting to crack...")
    possible_plaintext = decrypt(cipher_text)
    print("Decrypted text (guess):", possible_plaintext)
    return possible_plaintext

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python Atbash.py <mode> <text>")
        print("Modes: encrypt, decrypt, crack")
        sys.exit(1)

    mode = sys.argv[1].lower()
    text = sys.argv[2]

    if mode == "encrypt":
        print(encrypt(text))
    elif mode == "decrypt":
        print(decrypt(text))
    elif mode == "crack":
        print(crack(text))
    else:
        print("Invalid mode. Use encrypt, decrypt, or crack.")
