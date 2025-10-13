import random
from pick import pick


def rock_paper_scissors(player: str, stdscr):
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
            title = f"""Which movement want you to do ?\n
            1 - rock
            2 - paper
            3 - scissors"""
            options = [1, 2 ,3]
            user_movement = pick(options, title, screen=stdscr)
            stdscr.refresh()
            user_movement = user_movement[0]
            if user_movement in (1, 2, 3):
                stdscr.refresh()
                if ia_movement == user_movement:
                    stdscr.addstr(7, 0, "No winner")
                    stdscr.refresh()
                    stdscr.getch()
                if ia_movement < user_movement:
                    if ia_movement == 1 and user_movement == 3:
                        stdscr.addstr(7, 0, "you lose")
                        stdscr.getch()
                        ia_point += 1
                    else:
                        stdscr.addstr(7, 0, "you win")
                        stdscr.getch()
                        user_point += 1
                elif user_movement < ia_movement:
                    if ia_movement == 3 and user_movement == 1:
                        stdscr.addstr(7, 0, "You win")
                        stdscr.getch()
                        user_point += 1
                    else:
                        stdscr.addstr(7, 0, "you lose")
                        stdscr.getch()
                        ia_point += 1
                if ia_point > 2:
                    win = -1
                    break
                if user_point > 2:
                    win = 1
                    break
                stdscr.addstr(8, 0, f"You : {user_point} IA : {ia_point}")
                stdscr.getch()
            else:
                stdscr.addstr(
                    5,
                    0,
                    "Please type '1' for rock or '2' for paper or '3' for scissors ",
                )
                stdscr.refresh()
                stdscr.getch()
    return_table.append(win)
    return_table.append(user_point)
    return_table.append(player)
    return_table.append("shifoumi")
    return return_table
