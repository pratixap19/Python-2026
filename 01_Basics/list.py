marks=[94.7,87.9,95.6,66.8,34.7]
print(marks)
print(type(marks))
print(marks[0])
print(marks[3])
print(len(marks))
student=["Karan", 67.9, 17,"Delhi"]
print(student)

#List slicing
marks1=[85,94,76,63,48]
print(marks1[1:])

#negative index
print(marks1[-4:-1])

#List methods
list=[2,1,3]
list.append(4)
print(list)
print(list.sort())
print(list)

list.sort(reverse=True)
print(list)

list1=["banana", "apple", "lichi"]
list1.sort() #sort list in ascending order
print(list1)

list1.sort(reverse=True)
print(list1)

list2=['a', 'd', 'e', 'f', 'c', 'b']
list2.reverse()
print(list2)
list.sort(reverse=True) #sort list in descending order
print(list2)
list2.sort()
print(list2)

list2.insert(1,'g')
print(list2)

list2.remove('g') #remove first occurrence of element 
print(list2)

list2.pop(2)
print(list2) #removes element at index


