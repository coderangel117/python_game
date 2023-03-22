import random

from utils import check_special_characters


def mystery_number():
    return_table = []
    win = 0  # When user finds the great number
    counter = 0  # The user's attempt count
    force_counter = 0  # Increment when user doesn't respect game's instructions
    fail_counter = False  # Become True when user has exceeded max attempts
    while win == 0 & fail_counter != True:
        user_number = 0
        number_min: int = 1
        number_max: int = 100
        random_number = random.randint(number_min, number_max)
        while user_number != random_number | fail_counter != True | win != -1 | win != -2:
            user_number = input(f"Type a number between {number_min} and {number_max}\n")
            if not check_special_characters(user_number):
                break
            if user_number == "":
                print("Type something ....")
                break
            user_number = int(user_number)
            if user_number == 0 or user_number > number_max or user_number < number_min:
                if force_counter >= 5:
                    win = -2
                    break
                else:
                    print(f"It's between {number_min} and {number_max} ....")
                    force_counter += 1
                    break
            if user_number == random_number:
                counter += 1
                win = 1
                break
            if user_number > random_number:
                print('Your number is bigger than the mystery number')
            if user_number < random_number:
                print('Your number is smaller than the mystery number')
            counter += 1
            if counter > 5:
                fail_counter = True
                win = -1
    return_table.append(win)
    return_table.append(counter)
    return return_table

