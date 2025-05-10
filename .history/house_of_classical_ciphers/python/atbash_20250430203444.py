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
    # Since Atbash is symmetric and has no key,
    # cracking just means trying the decryption and verifying it manually
    print("Attempting to crack...")
    possible_plaintext = decrypt(cipher_text)
    print("Decrypted text (guess):", possible_plaintext)
    return possible_plaintext

# مثال للتجريب
if __name__ == "__main__":
    plain = "Hello World"
    encrypted = encrypt(plain)
    decrypted = decrypt(encrypted)
    
    print("Original:", plain)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
    
    # تجربة الكراك
    print("\nCracking Encrypted Text:")
    crack(encrypted)