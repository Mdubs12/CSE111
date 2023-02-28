from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()

subtotal = float(input('What is the subtotal? '))



if subtotal >= 50 and day_of_week == 1 or day_of_week == 2:
    discount = round(subtotal*.1, 2)
    (print(f'Your discount is {discount}$'))

else:
    discount = 0

tax = round(subtotal*.06, 2)
print(f'sales tax: {tax}')

total = subtotal + tax - discount

print(f'Your total is: {total}$')