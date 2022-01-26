#QN-M02:Write a program which inserts a number to any position in a list, which is hardcored inside the program. The list size will be 5. The output must be as follows:
#Your current list is: 1,2,3,4,5
#Specify the position:3
#Enter the value:100
#Value inserted.
#The new list is:1,2,100,4,5
# initializing list
test_list = [1, 2, 3, 4, 5]
# printing original list
print ("Your current list is: " + str(test_list))
# insert element
k = 100
print("Enter the value:",k)
for i in range(len(test_list)):
	if test_list[i] > k:
		index = i
		break
res = test_list[: i] + [k] + test_list[i :]
print("Value inserted.")
# printing result
print ("The new list is: " + str(res))
