# This is a sample Python script.
import os
import sys

MAX_UPPER = 90
MIN_UPPER = 65
MAX_LOWER = 122
MIN_LOWER = 97

KNOWN_KEYS = {
    "caesar_hard_2_encrypt.txt": 23,
    "caesar_easy_encrypted.txt": 18,
    "caesar_easy_2_encrypted.txt": 11,
    "caesar_hard_encrypt.txt": 6
}

def main():
    for filename in KNOWN_KEYS.keys():
        tool = CaesarTool(filename)
        tool.brute_force_solve()

class CaesarTool:

    def __init__(self, file=None, letters=None):
        self.file = file
        self.letters = letters
        self._letter_list = self._make_letter_list()

    def brute_force_solve(self):
        tmp_list = []
        for rotation in range(1, 25):
            for letter in self._letter_list:
                new_letter = self._shift(rotation, ord(letter))

                tmp_list.append(new_letter)
            print(f"Shift key: {rotation}\n{''.join(tmp_list)}")
            if rotation == KNOWN_KEYS.get(self.file):
                self.write_file(self.file, tmp_list)

            tmp_list.clear()

    def write_file(self, file, letter_list):
        with open(f"decrypted/{file}", 'w') as f:
            f.write("".join(letter_list))


    def _shift(self, rotation: int, letter_value: int):
        if (letter_value <= MAX_LOWER) and (letter_value >= MIN_LOWER):
            return self._boundary_shift(rotation, letter_value, MAX_LOWER, MIN_LOWER)
        if (letter_value <= MAX_UPPER) and (letter_value >= MIN_UPPER):
            return self._boundary_shift(rotation, letter_value, MAX_UPPER, MIN_UPPER)
        return chr(letter_value)

    def _boundary_shift(self, rotation: int, letter_value: int, max: int, min: int):
        new_value = letter_value + rotation
        if new_value > max:
            new_value = min + (new_value - max - 1)
        if new_value < min:
            new_value = max - (min - new_value - 1)
        return chr(new_value)

    def _make_letter_list(self):
        letters = []
        if self.file is None:
            return self.letters
        else:
            with open(f"encrypted4/{self.file}", 'r') as f:
                for word in f:
                    for letter in word:
                        letters.append(letter.lower())

            return letters

    def vigenere_shift(self, letter_list, rotation, start_idx, key_len):
        tmp_list = []
        for idx in range(start_idx, len(letter_list), key_len):
            letter = letter_list[idx]
            new_letter = self._shift(rotation, ord(letter))
            tmp_list.append(new_letter)
        return tmp_list

if __name__ == '__main__':
    main()

