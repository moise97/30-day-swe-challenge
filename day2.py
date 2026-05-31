name = "Moise"
age = 28
gpa = 3.0
is_cs_student = True

print (f"My name is {name}")
print(f"I am {age} years old")
print(f"My GPA is {gpa}")
print(f"Am I a CS student? {is_cs_student}")

def describe_person(name, age, gpa):
    return f"{name} is {age} years old with a {gpa} GPA"

print (describe_person("Moise", 28, 3.0))
print (describe_person("Angel", 28, 3.0))
print (describe_person("Jordan", 28, 3.0))
