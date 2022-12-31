import glob
import json
import os
import random
from User import User
from mystery_number import users_menu, main_menu


def get_all_users():
    users = get_user_files()
    merge_json_files(users)
    with open('users.json') as users:
        tab = json.load(users)
        if tab:
            for p in tab:
                print(p['username'])
        else:
            print("Il n' y a pas d'utilisateur dans la liste")
    # Parcours du fichier users.json


def get_user_files():
    users = []
    for file in glob.glob("*.json"):
        users.append(file)
    if users.__contains__('users.json'):
        users.remove('users.json')
    else:
        with open("users.json", 'w') as file:
            file.write('[]')
            file.close()
    return users


def new_user(username):
    """
    Create a new user with class User
    :param username:
    :return: user:User
    """
    users = get_user_files()
    user = User(username)
    user.username = username
    save_user(user)
    merge_json_files(users)
    return user


def get_user_info(user: User):
    """
    return user.tostring
    :param user:
    :return:str
    """
    return user.tostring()
    pass


def delete_user(username: str):
    users = get_user_files()
    filename = username + '.json'
    if users.__contains__(filename):
        os.remove(filename)
        get_all_users()
    else:
        print('cet utilisateur n\existe pas')


def update_user():
    pass


def find_user(username: str):
    """
    Return true if user_list contains searched user
    :param username:
    :return: boolean
    """
    if get_user_files().__contains__(username + '.json'):
        print('cet utilisateur existe bien dans la liste')
        return True
    else:
        print('Cet utilisateur n\'existe pas ')
        return False


def save_user(user: User):
    """
    Create a json file with user's information
    :param user:
    :return:
    """
    users = get_user_files()
    username = user.username
    nbfail = user.nbfail
    nbwin = user.nbwin
    greatest_score = user.greatest_score
    file_name = user.username + ".json"
    users.append(file_name)
    json_string = {
        'username': username,
        'nbfail': nbfail,
        'nbwin': nbwin,
        'greatest_score': greatest_score,
    }

    file = open(file_name, "w")
    json.dump(json_string, file, indent=2)
    file.close()


def merge_json_files(filename):
    """
    Merge all user's json files in one
    :param filename:
    :return:
    """
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.append(json.load(infile))

    with open('users.json', 'w') as output_file:
        json.dump(result, output_file, indent=2)


def loop_usermanager(choice: int):
    while choice != 0:
        if choice == 1:
            get_all_users()
            choice = users_menu()
        if choice == 2:
            user = input(
                '''
                Type user's username who want
                ''')
            find_user(user)
            choice = users_menu()
        if choice == 3:
            username = input(
                '''
                Type new user's username you want
                ''')
            new_user(username)
            choice = users_menu()
        if choice == 4:
            update_user()
            choice = users_menu()
        if choice == 5:
            get_all_users()
            username = input(
                '''
                Type user's username who want
                ''')
            delete_user(username)
            choice = users_menu()
        if choice == 6:
            main_menu()
