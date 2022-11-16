# Kurt Jonathan L. Gozano and Sheena Mechaela Basiga

import random

number = random.randrange(1,10)
attempt = 0

while True: 
    while attempt < 3:
        guessed_num = int(input("Enter number "))
        attempt += 1

        if guessed_num > number:
            print("Too high, try again!")
        elif guessed_num < number:
            print("Too low, try again!")
        else:
            break

    if guessed_num == number:
        print("You got it right in", attempt, "attempts")
        break
    else:
        print("You didn't guessed the right number after 3 attempts. Try again next time!")
        break