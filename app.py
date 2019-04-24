import login
import create_db

print('User Login Service')

conn = create_db.create_db()
if not conn:
    print('Failed to connect to DB')
    exit()

while True:
    level = input(
        """
Select Security Level: 
0 - No Security
1 - Blacklist Approach
2 - Whitelist Approach
3 - Parameterized Query
4+ - Exit
Choice: """)

    if not str(level).isnumeric():
        print('Invalid choice, Exiting!')
        break

    level = int(level)

    if level >= 4:
        break

    op = int(input('1 - Login\n2 - Query User\nChoice: '))

    if op == 1:
        u = input('Enter username to login: ')
        p = input('Password: ')
    else:
        u = input('Enter userid to query: ')

    r = None
    if level == 0:
        if op == 1:
            r = login.login(conn, u, p)
        else:
            r = login.query_user_info(conn, u)
    elif level == 1:
        if op == 1:
            r = login.black_list_login(conn, u, p)
        else:
            r = login.black_list_query_user_info(conn, u)
    elif level == 2:
        if op == 1:
            r = login.white_list_login(conn, u, p)
        else:
            r = login.white_list_query_info(conn, u)
    else:
        if op == 1:
            r = login.parameterized_query(conn, u, p)
        else:
            r = login.parameterized_query_user(conn, u)

    if not r:
        print('Operation Failed\n\n')
    else:
        print('Operation succeeded for user \'{}\''.format(u))

conn.close()
