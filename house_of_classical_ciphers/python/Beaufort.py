import re
import itertools
import sys
from collections import Counter


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
        plaintext = plaintext.lower()
        plaintext = re.sub("[^a-z]+", "", plaintext)
        ciphertext = ""

        i = 0
        for letter in plaintext:
            letter_num = ord(letter) - ord('a')
            cipher_letter_num = (self._key_array[i] - letter_num) % self.ALPHABET_SIZE
            ciphertext += chr(cipher_letter_num + ord('a'))

            i = (i + 1) % len(self._key)

        return ciphertext.upper()

    def decrypt(self, ciphertext: str):
        ciphertext = ciphertext.lower()
        ciphertext = re.sub("[^a-z]+", "", ciphertext)
        plaintext = ""

        i = 0
        for letter in ciphertext:
            letter_num = ord(letter) - ord('a')
            plain_letter_num = (self._key_array[i] - letter_num) % self.ALPHABET_SIZE
            plaintext += chr(plain_letter_num + ord('a'))

            i = (i + 1) % len(self._key)

        return plaintext

    def crack(self, ciphertext: str, key_length: int):
        ciphertext = ciphertext.lower()
        ciphertext = re.sub("[^a-z]+", "", ciphertext)

        total_combinations = 26 ** key_length

        if key_length > 3:
            return []  

        count = 0
        possible_keys = []
        for combo in itertools.product(sorted(range(self.ALPHABET_SIZE)), repeat=key_length):
            key_candidate = ''.join(chr(num + ord('a')) for num in combo)
            cracker = BeaufortCipher(key_candidate)
            plaintext_candidate = cracker.decrypt(ciphertext)
            possible_keys.append((key_candidate.upper(), plaintext_candidate))

            count += 1
           

        with open('crack_results.txt', 'w') as f:
            for guessed_key, cracked_plaintext in possible_keys:
                f.write(f"Key: {guessed_key} | Text: {cracked_plaintext}\n")

        return possible_keys


def main():
    print("--- Beaufort Cipher ---")

    if len(sys.argv) < 3:
        print("Usage: python script.py <key> <text> [<crack_key_length>]")
        return

    key = sys.argv[1]
    message = sys.argv[2]

    cipher = BeaufortCipher(key)
    print(f"Key: {cipher.get_key()}")

    encrypted = cipher.encrypt(message)
    print(f"Encrypted: {encrypted}")

    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")

    if len(sys.argv) >= 4:
        crack_length = int(sys.argv[3])
        possible_cracks = cipher.crack(encrypted, crack_length)

        if possible_cracks:
            print("\nCrack Results (written to crack_results.txt):")
            for guessed_key, cracked_plaintext in possible_cracks:
                print(f"Key: {guessed_key} | Text: {cracked_plaintext}")


if __name__ == "__main__":
    main()
