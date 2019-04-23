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

    u = input('Enter username to login: ')
    p = input('Password: ')

    r = None
    if level == 0:
        r = login.login(conn, u, p)
    elif level == 1:
        r = login.black_list_login(conn, u, p)
    elif level == 2:
        r = login.white_list_login(conn, u, p)
    else:
        r = login.parameterized_query(conn, u, p)
    
    if not r:
        print('Login Failed\n\n')
    else:
        print('User \'{}\' logged in'.format(u))
    
conn.close()


