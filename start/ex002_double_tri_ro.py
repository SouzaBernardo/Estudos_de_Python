# Say double, triple and the number root (int)...
colors = {
    'no_color':'\033[m',
    'yellow':'\033[33m',
    'red':'\033[31m',
    'blue':'\033[34m',
    'green':'\033[32m'
}

num_user = input('Enter a number:')
# Error
while num_user.count(',') or num_user.count('.'):
    print(f'{colors["red"]}ERROR!!! Enter a number integer!{colors["no_color"]}')
    num_user = input('Enter a number:')
# calc
num_user = int(num_user)
do = num_user * 2
tri = num_user * 3 
ro = num_user ** (1/2)
# result
print(f'Your number is {colors["yellow"]}{num_user}{colors["no_color"]}.')
print(f'The double is {colors["red"]}{do}{colors["no_color"]}')
print(f'The triple is {colors["blue"]}{tri}{colors["no_color"]}')
print(f'The root is {colors["green"]}{ro:.2f}{colors["no_color"]}')
