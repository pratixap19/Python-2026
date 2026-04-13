collection={1,2,3,4,5,2,1,"hello", "world"}
print((type(collection)))
print(collection)

student=set()
print(type(student))

marks=set()
marks.add(23)
marks.add(56)
marks.add(68)
marks.add(79)
marks.add("UMASS")
marks.add((1,2,3))
print(marks)

print(collection.pop())

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))

print(set1.intersection(set2))