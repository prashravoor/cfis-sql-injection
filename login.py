import sqlite3
from sqlite3 import Error
import create_db


def login(conn, username, password):
    c = conn.cursor()
    q = "SELECT * FROM users where user = '{}' and password = '{}'".format(username, password)
    # print(q)
    c.execute(q)
    result = c.fetchall()
    if len(result) == 0:
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

