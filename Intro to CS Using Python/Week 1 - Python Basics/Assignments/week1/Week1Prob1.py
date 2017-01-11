#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

#Ask user for string input
s = input("Enter a string: ")

#Convert to lowercase
s = s.lower()

#Instatiate counter
number_of_vowels = 0

#Iterate through chars in string and keep count of vowels
for x in range(len(s)):
    if(s[x] == 'a' or s[x] == 'e' or s[x] == 'i' or
       s[x] == 'o' or s[x] == 'u'):
            number_of_vowels += 1

print("Number of vowels: " + str(number_of_vowels))