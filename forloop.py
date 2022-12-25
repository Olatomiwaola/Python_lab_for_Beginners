#present_prices = []

#for i in range (0, 5):
    #price = i % 2
    #i = i // 2
    #if i <= 0:
        #present_prices.append(price)

for i in range (1, 13):
    for j in range (1, 13):
        value = i * j
        print(value, end =' "\n" ')
    print()