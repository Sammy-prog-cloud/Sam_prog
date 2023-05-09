weight = int(input('Enter in your weight >>> '))
convert = int(input('''What do you wish to convert to ? 
         1. L(bs)
         2. K(g)
                                                            '''))
if convert == 1:
    kilo = weight * 0.45
    print(f"You are : {kilo} kilos")
elif convert == 2:
    pound = weight / 0.45
    print(f"Y0u are : {pound} Pounds")
else:
    print('Invalid response')


print('''
            Name length    ''')
name = input('Enter in yor name >>>  ')
if len(name) < 3:
    print('Name must be at least 3 characters ')
elif len(name) > 50:
    print("Name must be maximum of 50 characters")
else:
    print('Name looks good !')
