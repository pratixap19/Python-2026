#using for loop print the element of the following list and tuple

# list=[1,4,9,16,25,36,49,64,81,100]

# for value in list:
#     print(value)
    
    
# tup=(1,4,9,16,25,36,49,64,81,100,49)
# x=49
# idx=0
# for value in tup:
#     if(value==x):
#         print("number found at index: ", idx)
#         break
#     idx += 1

#using for and range()
#print number from 1 to 100
# for i in range(1, 101, 1):
#     print(i)
    
#print from 100 to 1
# for i in range(100, 0, -1):
#     print(i)

#print multiplication table of a number n
n=int(input("Enter number: "))
for i in range(1, 11):
 print(n, "*", i, "=", n*i)