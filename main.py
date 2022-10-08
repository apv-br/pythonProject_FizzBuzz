# FizzBuzz

number_selected = 0
counter = 1

number_selected = int(input("Select a number between 1 and 100: "))

if number_selected < 1 or number_selected > 100:
    print("Number out of the range. Goodbye")
    number_selected = -1
else:
    print(number_selected)
    print()

while counter <= number_selected:

    remainder_3 = counter % 3
    remainder_5 = counter % 5

    if remainder_3 == 0 and remainder_5 == 0:
        print("fizzbuzz")
    elif remainder_3 == 0:
        print("fizz")
    elif remainder_5 == 0:
        print("buzz")
    else:
        print(str(counter))

    counter = counter + 1

