# Program to count words in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()
count = 0

for word in words:
    count = count + 1

print("Total words =", count)
#output
"""Enter a sentence: the sky is blue
Total words = 4"""