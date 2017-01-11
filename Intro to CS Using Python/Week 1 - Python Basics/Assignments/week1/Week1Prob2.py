#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

#Ask user for string input
s = input("Enter a string: ")

#Convert to lowercase
s = s.lower()

#Instatiate 'bob' counter
bob_count = 0;

for x in range(len(s)):
    if(s[x] == 'b' and s[x+1] == 'o' and s[x+2] == 'b'):
        bob_count += 1
    if x+2 == len(s)-1:
        break

print("Number of times bob occurs is: " + str(bob_count))