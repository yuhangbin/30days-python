
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

dog = {}

dog = {
    "name": "ein"
}

student = {
    "name": "kid",
    "skills": ["swimming", "reading"]
}

print(len(student))


print(type(student["skills"]))

student["skills"].append("running")

print(student["skills"])

print(student.keys())
print(student.values())

print(student.items())

del student["skills"]

print(student)

del student