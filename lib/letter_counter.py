# File: lib/letter_counter.py

class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 0
        for char in self.text:
            if not char.isalpha():
                continue
            if char not in counter.keys():
                counter[char] = counter.get(char, 1) #+ 1 #Sets number to wrong value
            else:
                counter[char] += 1
            if counter[char] > most_common_count:
                most_common = char
                most_common_count = counter[char] #Directly adds to most_common_count
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]

# 1. Ln 14 Initialising to dict with +2
# Fixing how numbers added to Dict
# 2. Ln 17 Incorrect assigning value to most_common_count
# 3. Ln 10 Most common_count set to 0 at start?

counter = LetterCounter("Dd")
print(counter.calculate_most_common())