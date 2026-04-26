# Program to count vowels using function

def count_vowels(text):
    count = 0
    
    for ch in text:
        if ch in "aeiouAEIOU":
            count = count + 1
    
    return count


text = input("Enter a string: ")
print("Total vowels =", count_vowels(text))
#Output
"""Enter a string: education
Total vowels = 5"""