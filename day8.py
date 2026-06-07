class student:
    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa
        
        
    def is_dean_list(self):
        return self.gpa >= 3.7

    def __str__(self):
        return f"{self.name} - GPA: {self.gpa}" 



student1 = student("Moise", 3.5)   
student2 = student("Angel", 3.9)   
student3 = student("Jordan", 3.2)   


print(student1)
print(student2)
print(student3)


print(f"\nDean's list check:")
print(f"{student1.name}: {student1.is_dean_list()}")
print(f"{student2.name}: {student2.is_dean_list()}")
print(f"{student3.name}: {student3.is_dean_list()}")





class car:
    def __init__(self, brand, speed):
        self.brand = brand 
        self.speed = speed


    def is_fast(self):
        return self.speed >150


    def __str__(self):
        return f"{self.brand} - speed: {self.speed}mph"

car1 = car("Toyota", 120)
car2 = car("Ferrari", 200)      
car3 = car("BMW", 160)  


print("\nCar check;")
print(car1)
print(car2)
print(car3)


print(f"\nIs {car1.brand} fast? {car1.is_fast()}")
print(f"\nIs {car2.brand} fast? {car2.is_fast()}")
print(f"\nIs {car3.brand} fast? {car3.is_fast()}")
