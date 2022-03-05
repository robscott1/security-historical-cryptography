import subprocess
import sys

from Util import Util
import subprocess, os


def main():
    tool = Mono("mono_medium_encrypt")
    freq = Util.frequency(tool._letter_list)
    tool.solve()


class Mono:

    def __init__(self, file):
        self.file = file
        self._letter_list, self._full_text = self._make_letter_list()

    def solve(self):
        solved, mappings = self.swap_loop()
        with open(f"unencrypted/{self.file}_unencrypted.txt", 'w') as f:
            f.write("".join(solved))
        key_pairs = [f"{x},{y}" for x, y in zip(mappings.keys(), mappings.values())]
        with open(f"{self.file}-key", 'w') as f:
            f.writelines(key_pairs)

    def decrypt(self):
        with open(f"keys/{self.file}_key.txt", 'r') as r:
            keys = r.readlines()
        keys = list(map(lambda x: x.strip("\n").split(","), keys))
        mystery_text = ["%" if x.isalpha() else x for x in self._full_text]
        for pair in keys:
            mystery_text = self.swap_letters(pair[0], pair[1], mystery_text)
        print("".join(mystery_text))
        with open(f"decrypted/{self.file}_decrypted.txt", 'w') as w:
            w.write("".join(mystery_text))





    def swap_loop(self):

        print("".join(self._full_text))
        mystery_text = ["%" if x.isalpha() else x for x in self._full_text]
        mappings = {}
        while "%" in "".join(mystery_text):
            old = input("Enter target letter: ")
            new = input("Enter a replacement letter: ")
            mappings[old] = new
            mystery_text = self.swap_letters(old, new, mystery_text)
            print("".join(self._full_text))
            print("-------------------------------------------")
            print("".join(mystery_text))
            print("-------------------------------------------")
        Util.print_frequencies(mappings)

        return mystery_text, mappings



    def _make_letter_list(self):
        letters = []
        text = []
        with open(f"encrypted4/{self.file}.txt", 'r') as f:
            for word in f:
                for letter in word:
                    text.append(letter)
                    if letter.isalpha():
                        letter = letter.lower()
                    letters.append(letter)

        return text, letters

    def swap_letters(self, old, new, working_result):
        idx = self.find_index(old)
        for i in idx:
            working_result[i] = new
        return working_result


    def find_index(self, target):
        idx = []
        for i in range(len(self._full_text)):
            if self._full_text[i] == target:
                idx.append(i)
        return idx








if __name__ == "__main__":
    main()