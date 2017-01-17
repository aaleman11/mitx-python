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
temp_string = ''

if (len(s)==1):
    print("Longest substring in alphabetical order is:", s)
else:
    for i in range(len(s)-1):
        if (s[i] <= s[i+1]):
            temp_string += s[i]
            if (i+1 == len(s)-1):
                temp_string += s[i+1]
                if (len(temp_string) > len(longest_substring)):
                    longest_substring = temp_string
                temp_string = ''
        else:
            temp_string += s[i]
            if (len(temp_string) > len(longest_substring)):
                longest_substring = temp_string
            temp_string = ''
    if(len(temp_string) == len(s)-1):
        print("Longest subtring in alphabetical order is:", s)
    else:
        print("Longest substring in alphabetical order is:", longest_substring)




