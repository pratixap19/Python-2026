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
nums=(1,4,9,16,25,36,49,64,81,100, 36)

i=0
x=36
while i<len(nums):
    if(nums[i]==x):
        print("FOUND at idx", i)
    else:
        print("Finding.....")
    i+=1