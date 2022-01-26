#QN-E04:Receive a set of numbers with list and display the following:
#Enter the number of numbers: 5
#5
#10
#25
#37
#42
#There are 2 even numbers 
#There are 3 odd numbers
lst =[]
Number=int(input("Enter the numbers "))
even_count,odd_count=0,0
for i in range(0,Number-1):
    elements=int(input())
    lst.append(elements)
print(i)
# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]
even_count, odd_count = 0, 0
num = 0
# using while loop	
while(num < len(list1)):
	
	# checking condition
	if list1[num] % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
	# increment num
	num += 1
print("There {} even numbers ".format(even_count) )
print("There {} odd numbers ".format( odd_count))
