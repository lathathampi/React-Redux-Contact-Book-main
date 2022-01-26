#QN-E02: Write a program which accepts a number and print whether it is odd or even.
#The program should show error if it is not a number.
# defining the function having
# the one parameter as input
def evenOdd(n):
    if(n % 2 == 0):
        return True
    elif(n %2 != 0):
        return False
    else:
        return evenOdd(n)
num = int(input("Enter the number"))
if(evenOdd( num )):
    print(num ,"num is even")
else:
    print(num ,"num is odd")
