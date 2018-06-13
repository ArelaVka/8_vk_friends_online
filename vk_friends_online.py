import vk
import getpass

APP_ID = 6604044

def get_user_login():
    return input('Enter your login: ')


def get_user_password():
    return getpass.getpass('Enter your password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, v='5.8')
    id_of_online_friends = api.friends.getOnline()
    return api.users.get(user_ids=id_of_online_friends)


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], ' ', friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    if login and password:
        friends_online = get_online_friends(login, password)
        print('\nList of online users:\n')
        output_friends_to_console(friends_online)
    else:
        print('You forget to enter login or password')
