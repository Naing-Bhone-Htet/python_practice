# Day 2 

# Build in Functions
import math 
print("Hello,World!")
print(len("Hello,World!")) # len build in function

a = 123
name = "Nathan"

print(str(a)) #converts from number to string
print(int("123")) #converts from string to number
print(float(a)) #converts to float
print(max([1,2,3])) #return the largest number
print(min([1,2,3])) #return the smallest number
print(sum([1,2,3]))# Sum the numbers
print(type(zip([1,2],[3,4])))

#FullName = input("Enter Your Name : ")  #Input function takes user's input
#print(f"Hello, {FullName}")


random_list = [23,4,56,7,32,35,75563,222423,86796,1,2]
sorted_list = sorted(random_list) # no need to confuse it sorted :)
print(sorted_list)

#Invalid variables names

# first-name
# first@name
# first$name
# num-1
# 1num

First_Name = "Abraharam"
Last_Name = "Lincon"
Full_Name = f"{First_Name} {Last_Name}"
Country = "USA"
Age = 120
City = "New York"
is_married = True
is_Dead = True
Skills = ['Politician','UnDetection Skill','LOW Resilance']
person_info = {
    'firstname':'Abraharam', 
    'lastname':'Lincon', 
    'country':'USA',
    'city':'New York'
    }


print(len(First_Name))
print(len(Last_Name))
print(type(Full_Name))
print(type(Country))
print(type(Age))
print(type(City))
print(type(is_Dead))
print(type(Skills))
print(type(person_info))


num_1 = 5
num_2 = 4

total = num_1 + num_2
diff = num_1 - num_2
product = num_1 * num_2
division = num_1 / num_2
remainder = num_1 % num_2
exp = num_1 ** num_2
floor_division = num_1 // num_2

print(total)  
print(diff)
print(product)  
print(division)  
print(remainder)  
print(exp)  
print(floor_division)  

radius = 30
Pi = math.pi
area_of_circle = Pi * radius ** 2
print(area_of_circle)

circumfrance = 2 * Pi * radius
print(circumfrance)

print("---Simple Circle Area Calculator---")
radius_r = int(input("Enter the Radius: "))
area_of_circle = Pi * radius_r ** 2
print(area_of_circle) 