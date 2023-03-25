import glob
import json
import os

from User import User
from utils import check_special_characters


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
            print("There are no user in this list ")
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
        print("This user doesn't exist")


def update_user(username, new_username):
    if find_user(username):
        file_name = username + '.json'
        new_file_name = new_username + '.json'
        with open(file_name, 'r+') as f:
            data = json.load(f)
            data['username'] = new_username  # <--- change `username` value.
            f.seek(0)  # <--- should reset file position to the beginning.
            json.dump(data, f, indent=2)
            f.truncate()  # remove remaining part
        os.rename(file_name, new_file_name)
        users = get_user_files()
        merge_json_files(users)
        get_all_users()
        print(f" The username {username} has been changed to {new_username}")
    else:
        pass
    print('The username you have entered was not found')


def find_user(username: str):
    """
    Return true if user_list contains searched user
    :param username:
    :return: boolean
    """
    if get_user_files().__contains__(username + '.json'):
        print("This user exist in the list")
        return True
    else:
        print("This user doesn't exist")
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


def users_menu():
    """
    Display users' manager menu and execute function with user's choice  or return to main menu
    :return: int
    """
    manage_choice = 0
    while manage_choice != 1 and manage_choice != 2 and manage_choice != 3 and manage_choice != 4 and manage_choice != 5 and manage_choice != 6:
        manage_choice = input('''
        [1] - Display users list    
        [2] - Search a specific user    
        [3] - Create a new user
        [4] - Update user info
        [5] - Delete a user
        [6] - return to main menu
        ''')
        if not check_special_characters(manage_choice):
            manage_choice = 0
        manage_choice = int(manage_choice)
        if manage_choice == 1:
            get_all_users()
            manage_choice = users_menu()
    if manage_choice == 2:
        user = input(
            '''
            Type user's username who want
            ''')
        find_user(user)
        manage_choice = users_menu()
    if manage_choice == 3:
        username = input(
            '''
            Type new user's username you want
            ''')
        new_user(username)
        manage_choice = users_menu()
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
        update_user(username, new_username)
        manage_choice = users_menu()
    if manage_choice == 5:
        get_all_users()
        username = input(
            '''
            Type user's username who want
            ''')
        delete_user(username)
        manage_choice = users_menu()
    if manage_choice == 6:
        return "main"
