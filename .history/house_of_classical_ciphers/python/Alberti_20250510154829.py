import sys
import json

circle = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Function to encrypt the text
def encrypt(text, align):
    cipher = ""
    for char in text:
        if char == " ":
            cipher += " "
            continue
        try:
            cipher += circle[circle.index(char) + align]
        except IndexError:
            cipher += circle[circle.index(char) + align - len(circle)]
    return cipher

# Function to decrypt the text
def decrypt(ciphertext, align):
    text = ""
    for char in ciphertext:
        if char == " ":
            text += " "
            continue
        try:
            text += circle[circle.index(char) - align]
        except IndexError:
            text += circle[circle.index(char) - align + len(circle)]
    return text

# Crack function with best guess
def crack(ciphertext):
    common_words = ["HOLA", "ESTA", "COMO", "EL", "LA", "DE", "ES", "UN", "EN", "Y", "POR", "QUE"]  # add more as needed
    best_match = ""
    best_score = 0
    best_shift = 0

    results = []
    for align in range(1, len(circle)):
        result = decrypt(ciphertext, align)
        score = sum(1 for word in common_words if word in result)
        if score > best_score:
            best_score = score
            best_match = result
            best_shift = align
        results.append({"shift": align, "decrypted_text": result})

    if best_score > 0:
        return json.dumps({"best_match": best_match, "shift": best_shift, "attempts": results})
    else:
        return json.dumps({"message": "No likely match found", "attempts": results})

# Main program
if len(sys.argv) < 2:
    print("Usage: python script.py <operation> [text]")
    sys.exit(1)

operation = sys.argv[1].strip()

if operation == '1':
    if len(sys.argv) < 4:
        print("Usage for encryption: python script.py 1 <text> <align>")
        sys.exit(1)
    text = sys.argv[2].upper()
    align = int(sys.argv[3])
    cipher = encrypt(text, align)
    print(json.dumps({"encrypted_text": cipher}))

elif operation == '2':
    if len(sys.argv) < 4:
        print("Usage for decryption: python script.py 2 <ciphertext> <align>")
        sys.exit(1)
    ciphertext = sys.argv[2].upper()
    align = int(sys.argv[3])
    decrypted_text = decrypt(ciphertext, align)
    print(json.dumps({"decrypted_text": decrypted_text}))

elif operation == '3':
    if len(sys.argv) < 3:
        print("Usage for cracking: python script.py 3 <ciphertext>")
        sys.exit(1)
    ciphertext = sys.argv[2].upper()
    cracked_result = crack(ciphertext)
    print(cracked_result)

elif operation == '4':
    print("Exiting program.")
    sys.exit(0)

else:
    print("Invalid choice. Please select again.")
    sys.exit(1)
