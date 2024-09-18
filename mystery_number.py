import random

from utils import check_special_characters


# @TODO: Add differents difficulty ( number of attempts or greater score as possible)
def mystery_number(player: str):
    return_table = []
    win = 0  # When user finds the great number
    counter = 0  # The user's attempt count
    max_counter = 10
    force_counter = 0  # Increment when user doesn't respect game's instructions
    fail_counter = False  # Become True when user has exceeded max attempts
    while win == 0 & fail_counter is not True:
        user_number = 0
        number_min: int = 1
        number_max: int = 100
        random_number = random.randint(number_min, number_max)
        while user_number != random_number | fail_counter is not True | win != -1 | win != -2:
            user_number = input(f"Type a number between {number_min} and {number_max}\n")
            if not check_special_characters(user_number):
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
                if counter < (max_counter - 1):
                    print(f" You have  {(max_counter - 1) - counter} attempts")
            if user_number < random_number:
                print('Your number is smaller than the mystery number')
                if counter < (max_counter - 1):
                    print(f"You have {(max_counter - 1) - counter} attempts yet")
            counter += 1
            if counter == max_counter:
                fail_counter = True
                print("You have exceeded the maximum number of attempts")
                print(f"the mystery number was {random_number}")
                win = -1
    return_table.append(win)
    return_table.append(counter)
    return_table.append(player)
    return_table.append("mystery_number")
    return return_table
