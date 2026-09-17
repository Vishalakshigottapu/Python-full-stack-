# even or odd
number = int(input("Enter the number: "))
if number == 0:
    print('Zero is neither even nor odd ')
elif number < 0 and number % 2 == 0:
    print('Negative Even Number')
elif number < 0 and number % 2 != 0:
    print('Negative Odd Number')
elif number % 2 == 0:
    print('Positive Even Number')
elif number % 2 != 0:
    print('Positive Odd Number')
