import sqlite3
from sqlite3 import Error


def create_db(db_file='db/users.db'):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, db_name):
    try:
        c = conn.cursor()
        c.execute(
            '''
            CREATE TABLE users
            (
                userid INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT NOT NULL,
                password VARCHAR(32) NOT NULL
            );
            '''
        )
        c.close()
    except Error as e:
        print(e)


def insert_user(conn, username, password):
    try:
        c = conn.cursor()
        q = "INSERT INTO users (user,password) VALUES ('{}','{}')".format(
            username, password)
        print(q)
        c.execute(q)
        print('User {} added!'.format(username))
        conn.commit()
        c.close()
    except Error as e:
        print('Error, user may already exist, or invalid username / password: {}'.format(e))


def read_entry():
    u = input('Enter a username: ')
    p = input('Enter a password: ')
    return (u, p)


if __name__ == '__main__':
    database = 'db/users.db'
    conn = create_db(database)
    create_table(conn, 'users')
    # insert_user(conn, 'user', 'password')
    u, p = read_entry()
    insert_user(conn, u, p)

    rows = conn.cursor().execute('SELECT * from users').fetchall()
    for r in rows:
        print(r)

    conn.commit()
    conn.close()
