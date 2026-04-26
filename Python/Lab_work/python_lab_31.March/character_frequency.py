s = "hello"

# Empty dictionary to store frequency
freq = {}

# Loop through string
for ch in s:
    # get() returns value or 0 if not exists
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
#Output
{'h': 1, 'e': 1, 'l': 2, 'o': 1}