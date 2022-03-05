class Util:

    expected_frequencies = {
        "e": 12.02,"t": 9.1,"a": 8.12,"o": 7.68,"i": 7.31,"n": 6.95,"s": 6.28,"r": 6.02,
        "h": 5.92,"d": 4.32,"l": 3.98,"u": 2.88,"c": 2.71,"m": 2.61,"f": 2.30,"y": 2.11,
        "w": 2.09,"g": 2.03,"p": 1.82,"b": 1.49,"v": 1.11,"k": 0.69,"x": 0.17,"q": 0.11,
        "j": 0.1,"z": 0.07
    }

    @classmethod
    def freq_proportions(cls, letter_list):
        result = {}
        freq = cls.frequency(letter_list)
        num_letters = len(list(filter(lambda x: x.isalpha(), letter_list)))
        for key, value in zip(freq.keys(), freq.values()):
            proportion = value / num_letters
            result[key] = proportion
        return result



    @classmethod
    def frequency(cls, letter_list):
        letter_list = list(filter(lambda x: x.isalpha(), letter_list))
        freq = {}
        for letter in letter_list:
            if letter not in freq:
                freq[letter] = 0
            else:
                freq[letter] += 1
        return freq

    @classmethod
    def repeats(cls, letter_list):
        substrings = {}
        letter_list = list(filter(lambda x: x.isalpha(), letter_list))
        for key_len in range(5, 13):
            curr_idx = 0
            while curr_idx + key_len <= len(letter_list):
                substr = "".join(letter_list[curr_idx: curr_idx + key_len])
                if " " in substr:
                    curr_idx += 1
                    continue
                curr_idx += 1
                if substr not in substrings:
                    substrings[substr] = 1
                else:
                    substrings[substr] += 1
        pop_list = []
        for key, value in zip(substrings.keys(), substrings.values()):
            if value < 2:
                pop_list.append(key)
        for item in pop_list:
            substrings.pop(item)
        return substrings

    @classmethod
    def print_frequencies(cls, f: dict):
        for kv_pair in f.items():
            print(kv_pair)

    @classmethod
    def ioc(cls, letter_list):
        letter_list = list(filter(lambda x: x.isalpha(), letter_list))
        freq = cls.frequency(letter_list)
        x = 0
        y = 0
        for value in freq.values():
            i = value
            x += i * (i - 1)
            y += i
        return x / (y * (y - 1))

    @classmethod
    def get_letter_groupings(cls, num_groups, letter_list):
        letter_list = list(filter(lambda x: x.isalpha(), letter_list))
        groupings = [[] for _ in range(num_groups)]
        for group in range(num_groups):
            for idx in range(group, len(letter_list), num_groups):
                groupings[group].append(letter_list[idx])
        return groupings



    @classmethod
    def chi_sq(cls, freq_list):
        score = 0.0
        for key, value in zip(freq_list.keys(), freq_list.values()):
            observed = freq_list.get(key)
            expected = (cls.expected_frequencies.get(key) / 100) * \
                       (sum(list(freq_list.values())))
            score += pow(observed - expected, 2) / expected
        return score

    @classmethod
    def find_closest_mapping(cls, obs_freq_dict: dict):
        mappings = []
        keys_used = set()
        for obs_key, obs_freq in zip(obs_freq_dict.keys(), obs_freq_dict.values()):
            lowest_diff = 1000000000
            for exp_key, exp_freq in \
                    zip(cls.expected_frequencies.keys(),
                        cls.expected_frequencies.values()):
                diff = abs(exp_freq - obs_freq)
                if diff < lowest_diff and exp_key not in keys_used:
                    lowest_diff = diff
                    closest_letter = exp_key
                    keys_used.add(exp_key)
            mappings.append((obs_key, closest_letter))

        return mappings





