# Q:1 print numbers from 1 to 100

# i=1
# while i<=100:
#     print(i)
#     i+=1
    
# Q:2 print numbers from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1
    
# Q:3 print the elements of the following list using a loop
# nums=[1,4,9,16,25,36,49,64,81,100]

# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1

# Q:4 Search for a number x in this tuple using loop
# nums=(1,4,9,16,25,36,49,64,81,100, 36)

# i=0
# x=36
# while i<len(nums):
#     if(nums[i]==x):
#         print("FOUND at idx", i)
#     else:
#         print("Finding.....")
#     i+=1

# Q:5 WAP to find the sum of first n numbers(using while loop)
# sum=0
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("Sum of first", n, "numbers is:", sum) 

# Q:5 WAP to find the sum of first n numbers(using for loop)

# n=int(input("Enter number: "))   
# sum=0;
# for i in range(1, n+1):
#     sum+=i
# print("Sum of first", n, "numbers is:", sum)

# Q:6 WAP to find the factorial of first n numbers using for loop and while loop
# n=int(input("Enter a number: "))
# factorial=1
# for i in range(factorial, n+1):
#     factorial=factorial*i
# print(factorial)

n=int(input("Enter a number: "))
factorial=1
i=1
while i<=n:
    factorial *= i
    i+=1
print("factorial =", factorial)
    
