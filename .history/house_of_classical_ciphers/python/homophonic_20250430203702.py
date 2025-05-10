import random

# مفتاح التشفير: لكل حرف رمز أو أكثر
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

# المفتاح العكسي لفك التشفير
reverse_key = {}
for letter, symbols in key.items():
    for sym in symbols:
        reverse_key[sym] = letter

# دالة التشفير
def encrypt(text):
    result = ''
    for char in text.upper():
        if char in key:
            result += random.choice(key[char]) + ' '
        else:
            result += char + ' '
    return result.strip()

# دالة فك التشفير
def decrypt(text):
    symbols = text.split()
    result = ''
    for sym in symbols:
        result += reverse_key.get(sym, '?')  # ? لو الرمز مش معروف
    return result

# دالة التخمين (كراك)
def crack(cipher_text):
    print("Trying to crack... (based on known symbols only)")
    return decrypt(cipher_text)

# الدالة الرئيسية
def main():
    while True:
        print("\nChoose an option:")
        print("1 - Encrypt")
        print("2 - Decrypt")
        print("3 - Crack")
        print("4 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            plain = input("Enter text to encrypt: ")
            print("Encrypted:", encrypt(plain))

        elif choice == '2':
            cipher = input("Enter encrypted symbols (separated by space): ")
            print("Decrypted:", decrypt(cipher))

        elif choice == '3':
            cipher = input("Enter cipher text to crack: ")
            print("Cracked:", crack(cipher))

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# تشغيل البرنامج
if __name__ == "__main__":
    main()