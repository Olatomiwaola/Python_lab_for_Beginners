# Olatomiwa Oladunjoye 101210403

import math

#Exercise 1
#1 - Example
"""
>>> volume_spherical_segment(1, 2, 4)
31.93952531149623

>>> volume_spherical_segment(3, 6, 9)
565.4866776461628

>>> volume_spherical_segment(2, 4, 5)
132.9940890019679

"""

#2 - Header
def volume_spherical_segment(h, R1, R2):
    
#3 - Description
#returns the volume of spherical segment in float type by taking three\
#parameters which are h(height), R1(radius of the base circle segment), \
# and R2(Radius of the top circle segment).
    
#4 - Body 
    return (1 / 6) * math.pi * h * ((3* R1 **2) + (3 * R2**2) + (h**2))
#5 - Test
print(volume_spherical_segment(6, 5, 8))
print(volume_spherical_segment(4, 5, 6))
print(volume_spherical_segment(2, 7, 5))
print(volume_spherical_segment(3, 8, 10))


#Exercise 2
#1 - Example 
"""
>>>i = equivalent_interest_rate(4, 3, 4)
0.03000000000000025
>>>i = equivalent_interest_rate(4, 5, 4)
0.04999999999999982
>>>i = equivalent_interest_rate(4, 7, 4)
0.07000000000000028

"""
#2 - Header
def equivalent_interest_rate(q, r, m) -> float:
    
#3 - Description
#returns equivalent interest rate (i) that takes three paramters which are \
# q(number of times interest rate is compounded per period), r(annual interest \
# rate), m(number of times annual interest rate is compounded per period).
    
#4 Body
    return q * ((1 + r /100 / m)**(m/q) - 1)

#5 Test 
i = equivalent_interest_rate(4, 4, 12)
print(i)
i = equivalent_interest_rate(4, 8, 4)
print(i)
i = equivalent_interest_rate(4, 8, 4)
print(i)
