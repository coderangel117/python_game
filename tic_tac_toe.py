# @TODO: can create game plate with 3 cols or greater
# @TODO: Add computer turn
from pick import pick

def tic_tac_toe(player: str, stdscr):
    """
    :param player:
    :return: [win, points, winner, game]
    """
    stdscr.clear()
    points = 0
    win = 0
    player_turn = 1
    game_plate = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    stdscr.addstr(1,0,"You are player 1\n")
    stdscr.getch()
    while win == 0 and win != "tie":
        empty_cell = 0
        stdscr.addstr(2,0,f"Player {player_turn}'s turn")
        display_game_plate(game_plate, stdscr)
        stdscr.getch()
        options = [0, 1, 2]
        option_x, player_coordinate_x = pick(options, "Please type coordinate for the row you choose\n", screen=stdscr )
        option_y, player_coordinate_y = pick(options, "Please type coordinate for the column you choose\n", screen=stdscr )
        coordinates = verify_coordinate(
            player_coordinate_x, player_coordinate_y, game_plate, stdscr
        )
        if coordinates:
            x = coordinates[0]
            y = coordinates[1]
            game_plate[x][y] = player_turn
            display_game_plate(game_plate, stdscr)
            win = check_win_condition(game_plate)
            if win != 0:
                stdscr.addstr(5,0, f"Player {player_turn} wins!")
                if player_turn == 1:
                    points = 1
                    break
            player_turn *= -1
        # check tie
        for i in range(3):
            for j in range(3):
                if game_plate[i][j] == game_plate[i][j] == game_plate[i][j] == 0:
                    empty_cell += 1
        if empty_cell == 0:
            stdscr.addstr("it's a tie")
            stdscr.getch()
            win = "tie"
    return [win, points, player, "tic tac toe"]


def verify_coordinate(player_coordinate_x: str, player_coordinate_y: str, game_plate, stdscr):
    """
    This function checks the user's input and returns it if valid.
    :param player_coordinate_x: The x-coordinate input by the player.
    :param player_coordinate_y: The y-coordinate input by the player.
    :param game_plate: The current game board.
    :return: Tuple of coordinates if valid, otherwise False.
    """
    x = int(player_coordinate_x)
    y = int(player_coordinate_y)
    if x in (0, 1, 2) and y in (0, 1, 2):
        if game_plate[x][y] == 0:
            return x, y
        else:
            stdscr.addstr(8, 0,"Cell already taken. Choose another coordinate.")
            stdscr.getch()
    return False


def display_game_plate(game_plate, stdscr):
    start_vertical = 3
    for i, row in enumerate(game_plate):
        line = " | ".join(str(cell) if cell != 0 else " " for cell in row)
        stdscr.addstr(start_vertical + i * 2, 25, line)  # Chaque ligne occupe deux lignes (pour pouvoir mettre un séparateur entre)
        if i < 2:
            stdscr.addstr(start_vertical + i * 2 + 1, 25, "-" * 10)
    stdscr.refresh() 

def check_win_condition(game_plate):
    """
    Check the game board for a win condition.
    :param game_plate: The current game board.
    :return: The winning player number, or 0 if no winner.
    """
    # Check rows and columns
    for i in range(3):
        if game_plate[i][0] == game_plate[i][1] == game_plate[i][2] != 0:
            return game_plate[i][0]
        if game_plate[0][i] == game_plate[1][i] == game_plate[2][i] != 0:
            return game_plate[0][i]
    # Check diagonals
    if game_plate[0][0] == game_plate[1][1] == game_plate[2][2] != 0:
        return game_plate[0][0]
    if game_plate[0][2] == game_plate[1][1] == game_plate[2][0] != 0:
        return game_plate[0][2]
    return 0
