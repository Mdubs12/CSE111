w = int(input("What is the width in millimeters?"))

a = int(input("What is the aspect ratio?"))

d = int(input("What is the diameter in inches?"))

import math


v = round((math.pi)* w*w*a*(w*a+2540*d)/10000000000, 2)

print(v)


from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()


answer = input(print('Would you like to buy tires with these dimensions? y for yes, n for no '))

if answer == "y":

    number = input(print('What is your phone number? '))

    with open('volumes.txt', 'at') as volume_file:

        print(f'{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v}, {number}', file=volume_file)

else:
    with open('volumes.txt', 'at') as volume_file:

        print(f'{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v}', file=volume_file)



