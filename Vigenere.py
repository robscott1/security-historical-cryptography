from Util import Util
from caesar import CaesarTool

KEY_LENS = [5, 9, 13]

EXP_KEY_LENGTH = 13

def main():
    filename = "vigerene_hard_encrypt.txt"
    tool = VigenereTool(filename)
    tool.find_key_length()
    print(f"\nPerforming chi-squared analysis on "
          f"caesar shifts with a key length of {EXP_KEY_LENGTH}...")
    for i in range(EXP_KEY_LENGTH):
        print(f"Key Index {i}: \n", tool.find_shift_key(i, EXP_KEY_LENGTH))


class VigenereTool:

    def __init__(self, file):
        self.file = file
        self._letter_list = self._make_letter_list()

    def repeats(self):
        print(Util.repeats(self._letter_list))

    def _make_letter_list(self):
        letters = []
        with open(f"encrypted4/{self.file}", 'r') as f:
            for word in f:
                for letter in word:
                    if letter.isalpha():
                        letter = letter.lower()
                    letters.append(letter)

        return letters

    def frequency_analysis(self):
        Util.print_frequencies(Util.freq_proportions(self._letter_list))
        print(Util.ioc(self._letter_list))

    def find_key_length(self):
        results = []
        for key_len in KEY_LENS:
            total = 0
            groups = Util.get_letter_groupings(key_len, self._letter_list)
            for group in groups:
                total += Util.ioc(group)
            results.append(total / key_len)
        for key_len, result in zip(KEY_LENS, results):
            print(f"IOC with key length of {key_len}: {result}")

    """
    find_shift_key
    
    Takes a given index (must be within range of key length) and 
    does chi squared analysis on every possible caesar shift  on that idx
    
    Not sure if the shift supposed to be all indices at once or just 
    the index of one key idx
    """
    def find_shift_key(self, idx, key_len):
        results = []
        letter_list = list(filter(lambda x: x.isalpha(), self._letter_list))
        tool = CaesarTool(letters=letter_list)
        for rotation in range(1, 25):
            rotation = rotation * -1
            # TODO: shift the ciphertext

            shifted_list = tool.vigenere_shift(letter_list, rotation, idx, key_len)
            shifted_freq = Util.frequency(shifted_list)

            # TODO: do chi-sq on letter frequency
            score = Util.chi_sq(shifted_freq)
            # return top 3 shift candidates and score (min x^2 value)
            results.append((rotation, score))

        return sorted(results, key=lambda x: x[1])[:3]






if __name__ == "__main__":
    main()