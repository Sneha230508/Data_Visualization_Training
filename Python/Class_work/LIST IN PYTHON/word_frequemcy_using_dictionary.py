# Program 10: Count word frequency using dictionary

sentence = "apple banana apple orange banana apple"

words = sentence.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency:")
for key, value in frequency.items():
    print(key, ":", value)
    #Output
    """Word Frequency:
apple : 3
banana : 2
orange : 1"""