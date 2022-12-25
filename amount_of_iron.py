# Amount of iron in mg present in diluted solution
def amount_present(conc, volume):
    amount_ltrs = conc / 1000
    mass_amount = amount_ltrs * volume
    return mass_amount

print(amount_present(250, 25))

#concentration of the diluted solution
def concentration(mass, volume):
    return mass/volume 
print(concentration(6.250, 0.50))

#percentage uncertainty for Fe in 500ml
def percentage_uncertainty_500ml(flask_error, flask_volume, mass_error):
    A = flask_error * 100 / 25
    B = flask_volume * 100/ 500
    C = mass_error * 100/ 0.25
    Total = A + B + C
    return Total 

errors = percentage_uncertainty_500ml(0.03, 0.15, 0.0002)
print(errors)

#uncertainty of solution flask
def uncertainty(volume, error_10ml, error_50ml):
    flask_10ml = error_10ml * 100 / volume
    Total_uncertainty = flask_10ml + error_50ml + 0.23
    return Total_uncertainty

print("UNCERTAINTY")
print(uncertainty(4.00, 0.1, 0.1))
print(uncertainty(8.00, 0.1, 0.1))
print(uncertainty(12.00, 0.1, 0.1))
print(uncertainty(16.00, 0.1, 0.1))
print(uncertainty(20.00, 0.1, 0.1))

print("Absolute Uncertainty")
def absolute_uncertainty(mass, flask_error):
    return  mass * flask_error/ 100

print(absolute_uncertainty(0.05, 2.83) )
print(absolute_uncertainty(0.10, 1.58))
print(absolute_uncertainty(0.15, 1.163))
print(absolute_uncertainty(0.20, 0.955))
print(absolute_uncertainty(0.25, 0.83))


name = ""
Blank = " "
name += (input("What is your name?" + Blank))
print("my name is", name, Blank, "--->")
      
boy = int(input("kilonshele\n"))

print(boy + 3)

list = [23, 837, 92, 2, 83, 9283 ,93 ,73738]
for i in range(0, len(list)):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j] , list[i]
            
print(list)



#Exercise 1:


Monday = 30
Tuesday = 30
Wednesday = 30
Thursday = 30
Friday = 30
Saturday = 40
Sunday = 40
weekday = Monday or Tuesday or Wednesday or Thursday or Friday
weekend = Saturday or Sunday
day = weekday or weekend


def ticket_price(age: int, day: str)-> float:
    if day == weekend:
        return T
    else:
        return F
    
    """
    The function name is ticket_price and it takes two parameters namely age in 
    int type and day(which represents the day of the week) in str. It returns an 
    amount that a customer should pay depending on the age bracket and the day of 
    the week. The days of week are distinguished into weekdays and weeekends.
    >>>
    Joy = ticket_price(10, Monday)
    $21.0
    
    >>>Jihg = ticket_price(10, Sunday)
    $28.0

    >>>Hoy = ticket_price(67, Sunday)
    $20.0

    >>>boby = ticket_price(67, Monday)
    $15.0

    >>>Sarah = ticket_price(20, Monday)
    $30

    >>>Akeem = ticket_price(23, Sunday)
    $40

"""

    if age >= 65 and day == weekday:
        return "$" + str(30 * 0.5)
    elif age >= 65 and day == weekend:
        return "$" + str(40 * 0.5) 
    elif age <= 12 and day == weekday:
        return "$" + str(30 * 0.7)
    elif age <= 12 and day == weekend:
        return "$" + str(40 * 0.7) 
    elif (12 < age < 65) and day == weekday:
        return "$" + str(30)    
    else:
        return "$" + str(40) 
    
    
Joy = ticket_price(10, Monday)
print(Joy)
Jihg = ticket_price(10, Sunday)
print(Jihg)
Hoy = ticket_price(67, Sunday)
print(Hoy)
boby = ticket_price(67, Monday)
print(boby)
Sarah = ticket_price(20, Monday)
print(Sarah)
Akeem = ticket_price(23, Sunday)
print(Akeem)

#Exercise 2:
