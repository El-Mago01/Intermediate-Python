DNA="TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGAATTTTCC"

char_count={}

for char in DNA:
    # First time initialization to 0
    if char not in char_count:
        char_count[char] = 0

    char_count[char] += 1

for counter, frequency in char_count.items():
    print(f"The char {counter} occurs {frequency} times ")