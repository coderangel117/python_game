import re


def check_special_characters(userinput: str):
    regex = re.compile('[@.€ç_!#$%^&*()<>\' \'?\"/\|}{~:A-z]')
    if regex.search(userinput) is not None:
        print("Only number please")
        return False
    elif userinput == "":
        print("Type something ....")
        return False
    else:
        return True

