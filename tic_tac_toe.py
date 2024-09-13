# @TODO: can create game plate with 3 cols or greater


def tic_tac_toe(player: str):
    win = 0
    # while win == 0:
    game_plate = [
        ["X", 0, 0],
        [0, 0, 0],
        [0, 0, "O"]
    ]
    for i in range(3):
        print(
            i + 1, game_plate[i],
        )
    print("A", "B", "C")
    # print(sum(game_plate[0]))

    return [1, 1, player, "tic tac toe"]
