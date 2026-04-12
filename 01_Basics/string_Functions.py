str="i am studying Python and I am having fun"
print(str.endswith("am"))

# print(str.capitalize()) #capitalize first character
# print(str) # second time it won't capitalize

# str=str.capitalize() #to resolve this issue it is required to store in another string
# print(str)

#print(str.replace("o", "a"))  #replaces all occurrences of old with new
#print(str.replace("Pythan", "Java"))

str=str.replace("Python", "Java")
print(str)

print(str.find("a")) #returns 1st index of 1st occurrer

print(str.count("I"))
