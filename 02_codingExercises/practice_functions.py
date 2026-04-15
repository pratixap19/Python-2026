#Print average of 3 numbers

# def calc_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg
# calc_avg(80,80,80)

#default parameters
# def calc_prod(a=2,b=4):
#     print(a*b)
#     return a*b
# calc_prod()

#default value is 1
# def calc_prod(a,b=4):
#     print(a*b)
#     return a*b
# calc_prod(1)

# Q:1 WAF to print the length of a list(list is the parameter)

# cities=["Boston", "New York", "Washington D.C" , "Philadelphia"]
# fruits=["Apple", "Mango", "Banana", "Cherry", "Strawberry"]
# def print_len(list):
#     print(len(list))
# print_len(cities)
# print_len(fruits)
    
# Q:2 WAF to print the elements of a list in a single line.(list is the parameter)
# fruits=["Apple", "Mango", "Banana", "Cherry", "Strawberry"]
# def print_list(list):
#     for item in list:
#         print(item, end=" ")   
# print_list(fruits)

# Q:3 WAF to find the factorial of n

# def calc_fact(n):
#     fact=1;
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
    
# calc_fact(6)

# Q:4 WAF to convert USD to INR
def converter(usd_value):
    inr_value = usd_value*83
    print(usd_value, "USD =", inr_value, "INR")
converter(10)

# Q:5 WAF tp print string "ODD" if the number is odd and "EVEN" if the number is even
def print_OddEven(num):
    if(num%2==0):
        print("EVEN")
    else:
        print("ODD")
print_OddEven(6)