number = int(input("Enter a number: "))

for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")

print("\nCountdown:")
count = 10
while count >= 0:
    print(count)
    count -= 1

print("Blast off!")

def get_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

print(get_evens([1,2,3,4,5,6,7,8,9,10]))