student={
    "name": "Pratixa",
    "age":"23",
    "is_adult":True,
    "topics":("dictionary", "set"),
    "skills":["Python", "Java", "TypeScript"],
    "subjects": {
        "physics":97,
        "chemistry":98,
        "math":95
    }
}

print(student)
print(student.keys()) #returns all keys
print(student.values()) #returns all values
print(len(student)) #return length
print(student.items()) #returns all(keys:values)
print(student.get("name")) #returns key according to value
