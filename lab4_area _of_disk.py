# Olatomiwa Oladunjoye 101210403 
import math  

#1
def area_of_disk(radius): 
    return math.pi * radius ** 2  
def area_of_ring(outer, inner): 
    return area_of_disk(outer) - area_of_disk(inner) 

#2
LITRES_PER_GALLON = 4.54609 
KMS_PER_MILE = 1.60934
def convert_to_litres_per_100_km(mpg):
    return 100 * LITRES_PER_GALLON / KMS_PER_MILE / mpg

#3
def accumulated_amount(principal, rate, n, time):
    return principal * ( 1 + rate/n) **(n * time)

#4
def area_of_cone(height, radius): 
    return (math.pi * radius **2) + (math.pi * radius) * \
           math.sqrt(radius **2 + height **2)


#Main Script

#Exercise 1
area = area_of_disk(5) 
print(area)
area = area_of_disk(5.0) 
print(area)
area = area_of_ring(10, 5)
print(area)
area = area_of_ring(10.0, 5.0)
print(area)

#Exercise 2
mpg = convert_to_litres_per_100_km(32)
print(mpg)
#mpg = convert_to_litres_per_100_km(0)
print(mpg)
mpg = convert_to_litres_per_100_km(60)
print(mpg)

#Exercise 3
Value = accumulated_amount(12000, 0.04, 3, 5)
print(Value)
Value = accumulated_amount(5000, 0.06, 4, 8)
print(Value)
Value = accumulated_amount(15000, 0.08, 5, 7)
print(Value)


#Excerise 4
# A cone with radius 8cm and a height of 4cm, the surface area will be pi * 
cone = area_of_cone(4, 8)
print(cone)
cone = area_of_cone(10, 5)
print(cone)
cone = area_of_cone(9, 6)
print(cone)