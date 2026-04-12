# (==) = equality operator-compare contents
# (is) = identity operator-compare memory
#a=[1,2,3]
#b=[1,2,3]
#print(a==b)
#print(a is b)

#Python does something called string interning-It reuses the same object in memory for certain strings to save space and improve performance.
x='hello'
y='hello'
print(x is y)