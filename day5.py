def add (a, b):
    return a + b


def subtract (a, b):
    return a - b 


def multiply (a, b):
    return a * b 
 

def divide (a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def calculate (a, b, operation):
    if operation == "add":
        return add (a, b)
    elif operation == ("subtract"):
        return subtract (a, b)
    elif operation == ("multiply"):
        return multiply (a, b)
    elif operation == ("divide"):

        return divide (a, b)
    else:
        return "Unknow Operation"
    
print(calculate(10, 5, "add"))
print(calculate(10, 5, "subtract"))
print(calculate(10, 5, "multiply"))
print(calculate(10, 5, "divide"))
print(calculate(10, 0, "divide"))


def greet(name, greeting="hello"):
    return f"{greeting} {name}"

print(greet("Moise"))
print(greet("Moise", "Yo"))
print(greet("Moise", "Good morning"))

def square (number):
    return number * number 

result = square(5)
print(f"The square of 5 is {result}")
print(f"The square of 10 is {square(10)}")
print(f"Double the square of 3 is {square(3) * 2}")
