# Ask for a number and tell your successor and predecessor

colors = {
    'no_color':'\033[m',
    'yellow':'\033[33m',
    'red':'\033[31m',
    'blue':'\033[34m'
}

successor = 0
predecessor = 0
line = f'{colors["yellow"]}=/' * 9 + f'={colors["no_color"]}'
number = 0

print(line)
number = input('Enter a number:')
while number.count('.') or number.count(','):
    print(line)
    print(f'{colors["red"]}ERROR!!! Enter an integer{colors["no_color"]}')
    number = input('Enter a number:')

successor = int(number) + 1 
predecessor = int(number) - 1 

print(line)
print(f'Your number is {colors["yellow"]}{number}{colors["no_color"]}')
print(f'The {colors["yellow"]}predecessor{colors["no_color"]} is {colors["yellow"]}{predecessor}{colors["no_color"]};')
print(f'The {colors["blue"]}successor{colors["no_color"]} is {colors["blue"]}{successor}{colors["yellow"]}.') 
print(line)
print('END')
