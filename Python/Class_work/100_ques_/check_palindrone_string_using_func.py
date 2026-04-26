# Program to check palindrome string using function

def is_palindrome(text):
    rev = ""
    
    for ch in text:
        rev = ch + rev
    
    if text == rev:
        return True
    else:
        return False


text = input("Enter a string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
#Output
"""Enter a string: madam
Palindrome"""