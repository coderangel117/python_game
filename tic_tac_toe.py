# @TODO: can create game plate with 3 cols or greater
import utils


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
        print(player_turn)
        display_game_plate(game_plate)
        player_coordonate_x = input('Please type coordonate for the row you choose\n')
        player_coordonate_y = input('Please type coordonate for the column you choose\n')
        coordonates = verify_coordonate(player_coordonate_x, player_coordonate_y, game_plate)
        if coordonates:
            x = coordonates[0]
            y = coordonates[1]
            game_plate[x][y] = player_turn
            display_game_plate(game_plate)
            player_turn *= -1
        else:
            player_turn *= 1
    else:
        player_turn *= 1
    return [1, 1, player, "tic tac toe"]


def verify_coordonate(player_coordonate_x: str, player_coordonate_y: str, game_plate):
    """
    This function permit to check user's input and return it if all character is clean
    :param player_coordonate_y:
    :param player_coordonate_x:
    :param game_plate:
    :return: boolean
    """
    check_x = utils.check_special_characters(player_coordonate_x)
    check_y = utils.check_special_characters(player_coordonate_x)
    if check_x and check_y:
        x = int(player_coordonate_x)
        y = int(player_coordonate_y)
        if x in (0, 1, 2) and y in (0, 1, 2):
            if game_plate[x][y] == 0:
                return x, y
            else:
                print("foo", game_plate[x][y])
                print("Please choose another coordonate")
                return False
    return False


def display_game_plate(game_plate):
    for i in range(3):
        print(
            i,
            game_plate[i],
        )
    print("A", "B", "C")
