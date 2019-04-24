import sqlite3
from sqlite3 import Error
import create_db
import re


def login(conn, username, password):
    c = conn.cursor()
    q = "SELECT * FROM users where user = '{}' and password = '{}'".format(
        username, password)
    # print(q)
    c.execute(q)
    result = c.fetchall()
    if len(result) == 0:
        return None
    for r in result:
        print(r)
    return 'Success'


black_list_re = "['\";]"  # Single quote or double quote
escaped_string = "''"  # Escape with additional '
pattern = re.compile(black_list_re)

blacklist_words = ['select', 'SELECT', 'WHERE', 'UNION', 'union']


def black_list_login(conn, username, password):
    if not username or not password:
        print('Error: Invalid username or password')
        return None

    if pattern.search(username):
        print('Invalid characters in username!')
        return None

    if pattern.search(password):
        print('Invliad characters in password!')
        return None

    for word in blacklist_words:
        if word in username:
            username = str(username).replace(word, '')
            print('Removing word "{}" from username'.format(word))
        if word in password:
            password = str(username).replace(word, '')
            print('Removing word "{}" from password'.format(word))

    return login(conn, username, password)


def black_list_query_user_info(conn, userid):
    if not userid:
        print('Error: Invalid userid')
        return None

    if pattern.search(userid):
        print('Invalid characters in userid!')
        return None

    for word in blacklist_words:
        if word in userid:
            userid = str(userid).replace(word, '')
            print('Removing word "{}" from username'.format(word))

    return query_user_info(conn, userid)


def query_user_info(conn, userid):
    c = conn.cursor()
    q = 'SELECT * from users where userid = {}'.format(userid)
    c.execute(q)
    results = c.fetchall()

    for r in results:
        print(r)

    return 'Success'


def white_list_login(conn, username, password):
    if not username or not password:
        print('Error: Invalid Username or Password')
        return None

    if not str(username).isalnum():
        print('Username contains invalid characters')
        return None

    if not str(password).isalnum():
        print('Password contains invalid characters')
        return None

    return login(conn, username, password)


def white_list_query_info(conn, userid):
    if not str(userid).isnumeric():
        print('Invalid number entered for userid!')
        return None

    return query_user_info(conn, userid)


def parameterized_query(conn, username, password):
    c = conn.cursor()
    c.execute("SELECT * FROM users where user = ? and password = ?",
              (username, password))
    results = c.fetchall()

    for r in results:
        print(r)

    if not len(results) == 1:
        return None
    return 'Success'


def parameterized_query_user(conn, userid):
    c = conn.cursor()
    c.execute("SELECT * from users where userid = ?", (userid, ))
    results = c.fetchall()

    for r in results:
        print(r)

    return 'Success'


if __name__ == '__main__':

    dbfile = 'db/users.db'
    conn = create_db.create_db(dbfile)

    if not conn:
        print('Failed to connect to DB')
        exit()

    u = input('Enter username to login: ')
    p = input('Password: ')

    if login(conn, u, p):
        print('User {} successfully logged in'.format(u))
    else:
        print('Login Failed')
