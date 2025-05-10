import re
import itertools
import sys
import json
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

    @staticmethod
    def crack(ciphertext: str):
        ciphertext = ciphertext.lower()
        ciphertext = re.sub("[^a-z]+", "", ciphertext)

        probable_lengths = BeaufortCipher.find_probable_key_lengths(ciphertext)

        results = []

        for key_length in probable_lengths:
            possible_keys = itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=key_length)
            for key_tuple in possible_keys:
                key = ''.join(key_tuple)
                try:
                    cipher = BeaufortCipher(key)
                    plaintext = cipher.decrypt(ciphertext)
                    if BeaufortCipher.is_plaintext_likely(plaintext):
                        results.append({
                            "key": key.upper(),
                            "decrypted": plaintext
                        })
                except Exception:
                    continue
        return results

    @staticmethod
    def find_probable_key_lengths(ciphertext: str):
        distances = []
        for seq_len in range(3, 6):
            for i in range(len(ciphertext) - seq_len):
                seq = ciphertext[i:i + seq_len]
                for j in range(i + seq_len, len(ciphertext) - seq_len):
                    if ciphertext[j:j + seq_len] == seq:
                        distances.append(j - i)

        if not distances:
            return [1, 2, 3, 4, 5, 6, 7, 8]

        factor_counts = Counter()
        for distance in distances:
            for factor in range(2, 21):
                if distance % factor == 0:
                    factor_counts[factor] += 1

        most_common = [item[0] for item in factor_counts.most_common(5)]
        return most_common if most_common else [1, 2, 3, 4, 5]

    @staticmethod
    def is_plaintext_likely(text: str):
        common_words = ["the", "and", "that", "have", "for", "not", "with", "you", "this"]
        return any(word in text for word in common_words)


# Entry point for Flutter integration
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:\n  encrypt <plaintext> <key>\n  decrypt <ciphertext> <key>\n  crack <ciphertext>")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "encrypt" and len(sys.argv) == 4:
        plaintext = sys.argv[2].replace(" ", "")
        key = sys.argv[3]
        try:
            cipher = BeaufortCipher(key)
            result = cipher.encrypt(plaintext)
            print(result)
        except Exception as e:
            print(f"Error: {e}")

    elif mode == "decrypt" and len(sys.argv) == 4:
        ciphertext = sys.argv[2]
        key = sys.argv[3]
        try:
            cipher = BeaufortCipher(key)
            result = cipher.decrypt(ciphertext)
            print(result)
        except Exception as e:
            print(f"Error: {e}")

    elif mode == "crack" and len(sys.argv) == 3:
        ciphertext = sys.argv[2]
        results = BeaufortCipher.crack(ciphertext)
        print(json.dumps(results, indent=2))

    else:
        print("Invalid arguments.")
