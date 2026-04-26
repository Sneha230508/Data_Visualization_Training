#To find first non repeating character
s = "aabbcde"

# Loop through each character
for ch in s:
    if s.count(ch) == 1:   # check frequency
        print(ch)
        break              # stop after first found
    #Output
    """c"""