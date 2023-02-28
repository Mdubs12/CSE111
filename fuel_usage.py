def main():
    start_miles = float(input('What is your starting miles?: '))

    end_miles = float(input('What is the ending miles?: '))

    amount_gallons = float(input('How many gallons were used?: '))

    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    lp100k = lp100k_from_mpg(mpg)

    print(f'{mpg: .1f} miles per gallon')
    print(f'{lp100k: .2f} liters per 100 kilometers')


def miles_per_gallon(start_miles, end_miles, amount_gallons):

    mpg = abs(end_miles - start_miles) / amount_gallons
    return mpg


def lp100k_from_mpg(mpg):

    lp100k = 235.215 / mpg
    return lp100k



main()
