import sqlite3
from sqlite3 import Error
import create_db
import re


def login(conn, username, password):
    c = conn.cursor()
    q = "SELECT * FROM users where user = '{}' and password = '{}'".format(username, password)
    # print(q)
    c.execute(q)
    result = c.fetchall()
    if len(result) == 0:
        return None
    return 'Success'


black_list_re = "['\"]" # Single quote or double quote
escaped_string = "''" # Escape with additional '
pattern = re.compile(black_list_re)


def escape_string(s):
    return pattern.sub(escaped_string, s)
    

def black_list_login(conn, username, password):
    if not username or not password:
        print('Error: Invalid username or password')
        return None
    
    username = escape_string(username)
    password = escape_string(password)        

    return login(conn, username, password)


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


def parameterized_query(conn, username, password):
    c = conn.cursor()
    c.execute("SELECT * FROM users where user = ? and password = ?", (username, password))
    r = c.fetchall()

    if not len(r) == 1:
        return None
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

