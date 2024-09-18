# @TODO: can create game plate with 3 cols or greater


def tic_tac_toe(player: str):
    """

    :param player:
    :return: [win, points, winner, game]
    """
    win = 0
    player_turn = 1
    game_plate = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    while win == 0:
        print(f"Player {player_turn}'s turn")
        display_game_plate(game_plate)
        player_coordinate_x = input('Please type coordinate for the row you choose\n')
        player_coordinate_y = input('Please type coordinate for the column you choose\n')
        coordinates = verify_coordinate(player_coordinate_x, player_coordinate_y, game_plate)
        if coordinates:
            x = coordinates[0]
            y = coordinates[1]
            game_plate[x][y] = player_turn
            display_game_plate(game_plate)
            win = check_win_condition(game_plate)
            if win != 0:
                break
            player_turn *= -1
        else:
            print("Invalid move. Try again.")
    print(f"Player {player_turn} wins!")
    return [1, 1, player, "tic tac toe"]


def verify_coordinate(player_coordinate_x: str, player_coordinate_y: str, game_plate):
    """
    This function checks the user's input and returns it if valid.
    :param player_coordinate_x: The x-coordinate input by the player.
    :param player_coordinate_y: The y-coordinate input by the player.
    :param game_plate: The current game board.
    :return: Tuple of coordinates if valid, otherwise False.
    """
    if player_coordinate_x.isdigit() and player_coordinate_y.isdigit():
        x = int(player_coordinate_x)
        y = int(player_coordinate_y)
        if x in (0, 1, 2) and y in (0, 1, 2):
            if game_plate[x][y] == 0:
                return x, y
            else:
                print("Cell already taken. Choose another coordinate.")
    return False


def display_game_plate(game_plate):
    for row in game_plate:
        print(" | ".join(str(cell) if cell != 0 else " " for cell in row))
        print("-" * 10)


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
