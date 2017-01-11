# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

#Ask user for string input
s = input("Enter a string: ")

#Convert to lowercase
s = s.lower()

#instantiate variables for longest substring and length of substring
longest_substring = ''
length_of_substring = len(longest_substring)

#slicing syntax is word[include:exclude]

for x in range(len(s)):
    next_index = x+1

    if(s[x] < s[next_index]):
        print("true")
        curr_inclusive_index = next_index





