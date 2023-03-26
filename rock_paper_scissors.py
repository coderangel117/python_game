import random


def rock_paper_scissors(player: str):
    return_table = []
    win = 0  # When user finds the great number
    while win == 0:
        user_point = 0
        ia_point = 0
        user_movement = ""
        ia_movement = ""
        while user_point < 3 and ia_point < 3:
            ia_movement = random.choice(['r', 'p', 's'])
            user_movement = input(""" Which movement want you to do ?
            Please type 
            'r' - rock 
            'p' - paper 
            's' - scissors 
            """)
            if user_movement in ("r", "p", "s"):
                if ia_movement == "r" and user_movement == "s":
                    print('you lose')
                    ia_point += 1
                if user_movement == "r" and ia_movement == "s":
                    print('you win')
                    user_point += 1
                if ia_movement == "p" and user_movement == "r":
                    print('you lose')
                    ia_point += 1
                if user_movement == "p" and ia_movement == "r":
                    print('you win')
                    user_point += 1
                if ia_movement == "s" and user_movement == "p":
                    print('you lose')
                    ia_point += 1
                if user_movement == "s" and ia_movement == "p":
                    print('you win')
                    user_point += 1
                if ia_movement == user_movement:
                    print("No winner")
                if ia_point > 2:
                    win = -1
                    break
                if user_point > 2:
                    win = 1
                    break
                print(f"You : {user_point} \n IA : {ia_point}")
            else:
                print("Please type 'r' for rock or 'p' for paper or 's' for scissors ")
    return_table.append(win)
    return_table.append(user_point)
    return_table.append(player)
    return_table.append("shifoumi")
    return return_table
