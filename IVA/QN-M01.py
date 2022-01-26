#QN-M01: Write a program to count the number of occurances of a string just like the following example:(case insensitive)
#Enter a string: My Name is Iva Systems
#Enter the character to Search==>m
#String you entered is: Iva Systems
#String you have searched is ==>M
#There are 3 occurances of M

## initializing the string and the word
string = str(input("Enter th string:"))
word = str(input("Enter the character to Search==>"))
#word = "am"
## splitting the string at space
words = string.split()
## initializing count variable to 0
count = 0
## iterating over the list
for w in words:
   ## checking the match of the words
   if w == word:
      ## incrementint count on match
      count += 1
## printing the count
print('String you entered is: ',string)
print('String you have searched is ==>',word)
print('There are {} occurances of {}'.format(count,word))

