my_City_name = 'Hong Kong'
my_City_population = 7500000
my_previous_City_name = 'Barcelona'
my_previous_City_population = 5500000
my_City_area = 2000


print('Population Analysis:')

if my_City_population > 10000000:
    print('My City is a Megacity')
elif my_City_population > 150000:
    print('My City is a large metropolitan area')
    if my_City_population > my_previous_City_population:
        print('My city is bigger than the current one')
    else:
        print('My previous city is bigger than the current one')
else:
    print('My city is neither a Megacity nor a large metropolitan area')

print('***********')

print('Area Analysis:')

if my_City_area > 10000000:
    print('My City is a Megacity')
elif my_City_area > 1500000:
    print('My City is a large metropolitan')
elif my_City_area > 500000:
    print('My City is a small metropolitan')
elif my_City_area > 150000:
    print('My City is a city')
else:
    print('My City is small')

print('***********')

print('End of Script')
