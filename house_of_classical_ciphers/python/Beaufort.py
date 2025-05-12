import re
import itertools
import sys


class BeaufortCipher:
    ALPHABET_SIZE = 26

    def __init__(self, key: str):
        self._key = key.lower()
        self._key_array = []
        self.set_key(self._key)

    def get_key(self):
        return self._key.upper()

    def set_key(self, key: str):
        if self.is_key_valid(key.lower()):
            self._key = key.lower()
            self._key_array = [ord(letter) - ord('a') for letter in self._key]
        else:
            raise Exception("Invalid Key")

    @staticmethod
    def is_key_valid(key: str):
        return re.match("^[a-z]+$", key) is not None

    def encrypt(self, plaintext: str):
        plaintext = re.sub("[^a-z]+", "", plaintext.lower())
        ciphertext = ""
        i = 0
        for letter in plaintext:
            letter_num = ord(letter) - ord('a')
            cipher_letter_num = (self._key_array[i] - letter_num) % self.ALPHABET_SIZE
            ciphertext += chr(cipher_letter_num + ord('a'))
            i = (i + 1) % len(self._key)
        return ciphertext.upper()

    def decrypt(self, ciphertext: str):
        ciphertext = re.sub("[^a-z]+", "", ciphertext.lower())
        plaintext = ""
        i = 0
        for letter in ciphertext:
            letter_num = ord(letter) - ord('a')
            plain_letter_num = (self._key_array[i] - letter_num) % self.ALPHABET_SIZE
            plaintext += chr(plain_letter_num + ord('a'))
            i = (i + 1) % len(self._key)
        return plaintext

    def crack(self, ciphertext: str, key_length: int):
        ciphertext = re.sub("[^a-z]+", "", ciphertext.lower())
        possible_keys = []

        for combo in itertools.product(range(self.ALPHABET_SIZE), repeat=key_length):
            key_candidate = ''.join(chr(num + ord('a')) for num in combo)
            cracker = BeaufortCipher(key_candidate)
            plaintext_candidate = cracker.decrypt(ciphertext)
            possible_keys.append((key_candidate.upper(), plaintext_candidate))

        return possible_keys


def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <operation> <text> <key_or_keylength>")
        sys.exit(1)

    operation = sys.argv[1].lower()
    input_text = sys.argv[2]
    key_or_len = sys.argv[3]

    if operation == "encrypt":
        cipher = BeaufortCipher(key_or_len)
        result = cipher.encrypt(input_text)
        print(result)

    elif operation == "decrypt":
        cipher = BeaufortCipher(key_or_len)
        result = cipher.decrypt(input_text)
        print(result)

    elif operation == "crack":
        try:
            key_length = int(key_or_len)
        except ValueError:
            print("For crack, the third argument must be an integer key length.")
            sys.exit(1)

        if key_length > 4:
            print("Key length too large for brute force.")
            sys.exit(1)

        cipher = BeaufortCipher("a")  # dummy key
        results = cipher.crack(input_text, key_length)

        for key, text in results:
            print(f"{key}:{text}")
    else:
        print("Invalid operation. Choose from: encrypt, decrypt, crack.")
        sys.exit(1)


if __name__ == "__main__":
    main()
