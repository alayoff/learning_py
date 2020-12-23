temperature = float(input("Enter the degree number: "))
temperature_type = str(input("if it's Celsius type \"C\":\nif it's Fahrenheit type \"F\": ")).upper()
celsius = temperature
fahrenheit = temperature

if temperature_type == 'F':
    print((5 * fahrenheit - 160) / 9,'C')
elif temperature_type == 'C':
    print((9*celsius+32*5) / 5,'F')
else:
    print('Oops, wrong imput\nPlease try again')
