import math

i = int(input('Enter the number of items '))

x = int(input('Enter the number of items per box '))

b = int(math.ceil(i/x))

print(f'You will need {b} boxes')