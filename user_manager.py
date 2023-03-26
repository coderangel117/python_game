import glob
import json
import os

import utils
from User import User


def get_all_users():
    """
    return all user in users.json
    :return:
    """
    users = get_user_files()
    merge_json_files(users)
    with open('users.json') as users:
        tab = json.load(users)
        if tab:
            for p in tab:
                print(p['username'])
        else:
            new_user('invite')
    return users
    # Parcours du fichier users.json


def get_user_files():
    """
    create a string array with all json file name
    :return:
    """
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
    if users.__contains__(username + ".json"):
        print(f"User {username} already exists. ")
    user = User(username)
    user.username = username
    save_user(user)
    merge_json_files(users)
    return user


def get_user_info(username: str):
    """
    return user.tostring
    :param username:
    :return:str
    """
    users = get_user_files()
    file_name = username + '.json'
    if users.__contains__(file_name):
        with open(file_name, 'r+') as f:
            data = json.load(f)
            if data['played_games'] > 0:
                if data['played_games'] >= data['nbfail'] & data['played_games'] >= data['nbfail'] & \
                        data['played_games'] == data['nbfail'] + data['nbwin']:
                    print(
                        f" User {data['username']} has {data['nbfail']} fails"
                        f" ({(data['nbfail'] / data['played_games']) * 100}%) "
                        f"and {data['nbwin']} wons ({(data['nbwin']  / data['played_games'] )* 100}% )")
                else:
                    print('There are error in played games count....')
            else:
                print(f"User {data['username']} have never played")
    else:
        print('User chosen doesn\'t exists')


def delete_user(username: str):
    users = get_user_files()
    filename = username + '.json'
    if users.__contains__(filename):
        os.remove(filename)
        get_all_users()
    else:
        print("This user doesn't exist")


def update_username(username, new_username):
    get_all_users()
    if find_user(username):
        file_name = username + '.json'
        new_file_name = new_username + '.json'
        with open(file_name, 'r+') as f:
            data = json.load(f)
            data['username'] = new_username  # <--- change `username` value.
            f.seek(0)  # <--- should reset file position to the beginning.
            json.dump(data, f, indent=2)
            f.truncate()  # remove remaining part
        users = get_user_files()
        print(users)
        if users.__contains__(file_name):
            print(f"User {username} already exists.")
        else:
            os.rename(file_name, new_file_name)
            merge_json_files(users)
            get_all_users()
            print(f" The username {username} has been changed to {new_username}")
    else:
        print('The username you have entered was not found')


def add_win(username):
    if find_user(username):
        file_name = username + '.json'
        with open(file_name, 'r+') as f:
            data = json.load(f)
            data['nbwin'] += 1  # <--- change `username` value.
            f.seek(0)  # <--- should reset file position to the beginning.
            json.dump(data, f, indent=2)
            f.truncate()  # remove remaining part
        users = get_user_files()
        merge_json_files(users)


def add_played_game(username):
    if find_user(username):
        file_name = username + '.json'
        with open(file_name, 'r+') as f:
            data = json.load(f)
            data['played_games'] += 1  # <--- change `username` value.
            f.seek(0)  # <--- should reset file position to the beginning.
            print(data['played_games'])
            json.dump(data, f, indent=2)
            f.truncate()  # remove remaining part
        users = get_user_files()
        merge_json_files(users)


def add_fail(username):
    if find_user(username):
        file_name = username + '.json'
        with open(file_name, 'r+') as f:
            data = json.load(f)
            data['nbfail'] += 1  # <--- change `username` value.
            f.seek(0)  # <--- should reset file position to the beginning.
            json.dump(data, f, indent=2)
            f.truncate()  # remove remaining part
        users = get_user_files()
        merge_json_files(users)


def find_user(username: str):
    """
    Return true if user_list contains searched user
    :param username:
    :return: boolean
    """
    if get_user_files().__contains__(username + '.json'):
        return True
    else:
        return False


def save_user(user: User):
    """
        Create a json file with user's information
        :param user:
        :return:
    """
    users = get_user_files()
    username = user.username
    played_games = user.played_games
    nbfail = user.nbfail
    nbwin = user.nbwin
    greatest_score = user.greatest_score
    file_name = user.username + ".json"
    users.append(file_name)
    json_string = {
        'username': username,
        'played_games': played_games,
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


def users_menu():
    """
        Display users' manager menu and execute function with user's choice  or return to main menu
        :return: int
    """
    manage_choice = 0
    while manage_choice != 1 and manage_choice != 2 and manage_choice != 3 and manage_choice != 4 \
            and manage_choice != 5 and manage_choice != 6 and manage_choice != 7:
        manage_choice = input('''
        [1] - Display users list    
        [2] - Search a specific user    
        [3] - Create a new user
        [4] - Update user username
        [5] - Delete a user
        [6] - Display user info
        [7] - return to main menu
        ''')
        if not utils.check_special_characters(manage_choice):
            manage_choice = 0
        manage_choice = int(manage_choice)
    if manage_choice == 1:
        get_all_users()
    if manage_choice == 2:
        user = input(
            '''
            Type user's username you want to show
            ''')
        if find_user(user):
            print("This user exist in the list")
        else:
            print("This user doesn't exist")
    if manage_choice == 3:
        get_all_users()
        username = input(
            '''
            Type new user's username you want
            ''')
        new_user(username)
    if manage_choice == 4:
        get_all_users()
        username = input(
            '''
            Type user's username you want to change
            ''')
        new_username = input(
            '''
            Type the new username 
            ''')
        update_username(username, new_username)
    if manage_choice == 5:
        get_all_users()
        username = input(
            '''
            Type user's username who want
            ''')
        delete_user(username)
    if manage_choice == 6:
        get_all_users()
        username = input(
            '''
            Type user's username you want
            ''')
        get_user_info(username)
    if manage_choice == 7:
        return "main"
