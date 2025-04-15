import re

import user_manager


def check_special_characters(userinput: str):
    """
    Check if user's input is only an integer
    :param userinput:
    :return: bool
    """
    regex = re.compile('[@.€ç_!#$%^&*()<>\' \'?\"/\\|}{~:A-z]')
    if regex.search(userinput) is not None:
        print("Only number please")
        return False
    elif userinput == "":
        print("Type something ....")
        return False
    else:
        return True


def init_json_files():
    u = open("users.json", "w")
    f = open("invite.json", "w")
    f.write("""{
        "username": "invite",
        "played_games": 0,
        "nbfail": 0,
        "nbwin": 0,
        "greatest_score": []
    }""")
    u.close()
    f.close()
    user_manager.merge_json_files(user_manager.get_user_files())