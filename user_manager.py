import curses
import glob
import json
import os

from pick import pick

from User import User


def get_user_files():
    """
    create a string array with all json file name corresponding to all usernames
    :return:array
    """
    users = []
    for file in glob.glob("*.json"):
        users.append(file)
    if users.__contains__('users.json'):
        users.remove('users.json')  # Remove users.json from list
    else:
        with open("users.json", 'w') as file:  # Create the file if not exists
            file.write('[]')
            file.close()
    return users


def merge_json_files(filename: list[str]):
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
    # All default value are 0 without username

    users = get_user_files()
    f = open("users.json", "w")
    f.close()
    username = user.username
    played_games = user.played_games
    nbfail = user.nbfail
    nbwin = user.nbwin
    greatest_score = user.greatest_score
    file_name = user.username + ".json"
    users.append(file_name)
    json_string = {
        'username': username,
        'played_games': played_games,  # default value to 0
        'nbfail': nbfail,  # default value to 0
        'nbwin': nbwin,  # default value to 0
        'greatest_score': greatest_score,  # default value to 0
    }

    file = open(file_name, "w")
    json.dump(json_string, file, indent=2)
    file.close()


def get_all_users(stdscr):
    """
    return all user in users.json
    :return: users
    """
    users_list = get_user_files()
    merge_json_files(users_list)
    with open('users.json') as users:
        tab = json.load(users)
        if tab:
            for p in tab:
                stdscr.addstr(12, 0, f"{p['username']}")
        else:
            new_user('invite', stdscr)
    return users_list


def new_user(username: str, stdscr):
    """
    Create a new user with class User
    :param stdscr:
    :param username:str
    :return: user:User
    """
    users = get_user_files()  # Get all username
    if users.__contains__(username + ".json"):  # Check if username is free
        stdscr.addstr(12, 0, f"User {username} already exists. ")
    user = User(username)  # Create user
    user.username = username
    save_user(user)  # Save user json file wit info
    merge_json_files(users)  # Update the users.json file
    return user


def get_user_info(username: str, stdscr):
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
                if data['nbfail'] > 0 or data['nbwin'] > 0:
                    if data['played_games'] == data['nbfail'] + data['nbwin']:  # Check if stats can be coherent
                        stdscr.addstr(12, 0, f"User {data['username']} has {data['played_games']} played games ")
                        stdscr.addstr(13, 0,
                                      f"with {data['nbfail']} fails ({int((data['nbfail'] / data['played_games']) * 100)}%) ")
                        stdscr.addstr(14, 0,
                                      f"and {data['nbwin']} wons ({int((data['nbwin'] / data['played_games']) * 100)}%)")
                    else:
                        stdscr.addstr(12, 0, 'There are error in played games count....')
                else:
                    stdscr.addstr(12, 0, 'There are error in win or fail count....')
            else:
                stdscr.addstr(12, 0, "User {data['username']} have never played")
    else:
        stdscr.addstr(12, 0, "User chosen doesn't exists")


def delete_user(username: str, stdscr):
    users = get_user_files()
    filename = username + '.json'
    if users.__contains__(filename):
        os.remove(filename)  # Remove the user's json file
        get_all_users(stdscr)
        stdscr.addstr(12, 0, f"User {username} has been successfully deleted")
        stdscr.refresh()
        stdscr.getch()
    else:
        stdscr.addstr(12, 0, "User doesn't exist")
        stdscr.refresh()
        stdscr.getch()


def update_username(username: str, new_username: str, stdscr):
    get_all_users(stdscr)
    if find_user(username):
        file_name = username + '.json'
        new_file_name = new_username + '.json'
        users = get_user_files()
        if users.__contains__(new_file_name):
            stdscr.addstr(12, 0, f"User {username} already exists.")
        else:
            with open(file_name, 'r+') as f:
                users = get_user_files()
                data = json.load(f)
                data['username'] = new_username  # change `username` value.
                f.seek(0)  # should reset file position to the beginning.
                json.dump(data, f, indent=2)
                f.truncate()  # remove remaining part
            merge_json_files(users)
            os.rename(file_name, new_file_name)
            get_all_users(stdscr)
            stdscr.addstr(12, 0, f" The username {username} has been changed to {new_username}")
    else:
        stdscr.addstr(12, 0, f'The username {username} you have entered was not found')


def add_win(username: str):
    if find_user(username):
        file_name = username + '.json'
        with open(file_name, 'r+') as f:
            data = json.load(f)
            data['nbwin'] += 1  # increase win stat value.
            f.seek(0)  # should reset file position to the beginning.
            json.dump(data, f, indent=2)
            f.truncate()  # remove remaining part
        users = get_user_files()
        merge_json_files(users)


def add_played_game(username: str):
    if find_user(username):
        file_name = username + '.json'
        with open(file_name, 'r+') as f:
            data = json.load(f)
            data['played_games'] += 1  # change played game value.
            f.seek(0)  # should reset file position to the beginning.
            json.dump(data, f, indent=2)
            f.truncate()  # remove remaining part
        users = get_user_files()
        merge_json_files(users)


def add_fail(username: str):
    if find_user(username):
        file_name = username + '.json'  # Get user's file
        with open(file_name, 'r+') as f:
            data = json.load(f)  # load file
            data['nbfail'] += 1  # increase fail value.
            f.seek(0)  # should reset file position to the beginning.
            json.dump(data, f, indent=2)
            f.truncate()  # remove remaining part
        users = get_user_files()
        merge_json_files(users)  # Update the users.json


def users_menu(stdscr):
    """
        Display users' manager menu and execute function with user's choice  or return to main menu
        :return: int
    """
    while True:
        title = 'Choose an action to do with users'
        options = ['Display users list', 'Search a specific user', 'Create a new user',
                   'Update user username', 'Delete a user', 'Display user info', 'return to main menu']
        _, manage_choice = pick(options, title, screen=stdscr)

        if manage_choice == 0:
            # stdscr.clear()
            stdscr.addstr(9, 0, 'Users list:\n')
            stdscr.refresh()
            get_all_users(stdscr)
            stdscr.addstr(10, 0, 'Press any key to continue')
            stdscr.getch()
        if manage_choice == 1:
            stdscr.addstr(9, 0, 'Type the username you want to search\n')
            curses.echo()
            username = stdscr.getstr(10, 0).decode('utf-8')
            curses.noecho()
            if find_user(username):
                stdscr.addstr(12, 0, f'{username} is in the list')
                stdscr.refresh()
                stdscr.getch()
            else:
                stdscr.addstr(12, 0, f'{username} is not in the list')
                stdscr.refresh()
                stdscr.getch()
        if manage_choice == 2:
            get_all_users(stdscr)
            stdscr.addstr(9, 0, 'Type the username you want to create\n')
            curses.echo()
            username = stdscr.getstr(10, 0).decode('utf-8')
            curses.noecho()
            new_user(username)
            stdscr.addstr(10, 0, 'Press any key to continue')
        if manage_choice == 3:
            get_all_users(stdscr)
            stdscr.addstr(9, 0, "Type user's username you want to change\n")
            curses.echo()
            username = stdscr.getstr(10, 0).decode('utf-8')
            curses.noecho()
            stdscr.addstr(11, 0, "Type the new username\n")
            curses.echo()
            new_username = stdscr.getstr(12, 0).decode('utf-8')
            curses.noecho()
            update_username(username, new_username, stdscr)
        if manage_choice == 4:
            stdscr.clear()
            get_all_users(stdscr)
            stdscr.addstr(9, 0, "Type user's username who want to delete\n")
            curses.echo()
            username = stdscr.getstr(10, 0).decode('utf-8')
            curses.noecho()
            delete_user(username, stdscr)
        if manage_choice == 5:
            get_all_users(stdscr)
            username = input(
                '''
                Type user's username you want
                ''')
            get_user_info(username, stdscr)
        if manage_choice == 6:
            return "main"
