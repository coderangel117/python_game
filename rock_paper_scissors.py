import random


def rock_paper_scissors(player: str):
    return_table = []
    win = 0  # When user finds the great number
    user_point = 0
    while win == 0:
        ia_point = 0
        while user_point < 3 and ia_point < 3:
            user_movement = 0
            ia_movement = 0
            ia_movement = random.choice([1, 2, 3])
            choice = ["rock", "paper", "scissors"]
            user_movement = int(input(""" Which movement want you to do ?
            Please type 
            '1' - rock
            '2' - paper
            '3' - scissors
            """))
            print(f" You choose {choice[user_movement - 1]}\n"
                  f" ia choose {choice[ia_movement - 1]}")
            if user_movement in (1, 2, 3):
                if ia_movement == user_movement:
                    print("No winner")
                if ia_movement < user_movement:
                    if ia_movement == 1 and user_movement == 3:
                        print("you lose")
                        ia_point += 1
                    else:
                        print("you win")
                        user_point += 1
                elif user_movement < ia_movement:
                    if ia_movement == 3 and user_movement == 1:
                        print("you win")
                        user_point += 1
                    else:
                        print("you lose")
                        ia_point += 1
                if ia_point > 2:
                    win = -1
                    break
                if user_point > 2:
                    win = 1
                    break
                print(f"You : {user_point} \n IA : {ia_point}")
            else:
                print("Please type '1' for rock or '2' for paper or '3' for scissors ")
    return_table.append(win)
    return_table.append(user_point)
    return_table.append(player)
    return_table.append("shifoumi")
    return return_table
