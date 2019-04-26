# SQL Injection Demo - using Python and SQLITE3
Simple code to demo how SQL injection works, and how it can be addressed <br>

## Setup and Install
Python version - 3.6+ <br>
Ensure the pysqlite package is installed (should be there by default) <br>
Create the initial Data base with a few users to test the program. User creation can be done through 'python create_db.py'. <br>

## Running the code
Start the program using `python app.py`. Rest is fairly straightforward <br>

## Some SQL Injections for each case
### No Security
* For login workflow, Set password to `p' or 1=1`
* For login workflow, set password to `p' union select * from users --`
* For query user workflow, set user id to `100 or 1=1`
* For query user workflow, set user id to `100 union select * from users`

### Blacklist appraoch
A few of the vulnerabilties are blocked, and it is slightly more secure <br>
* For login workflow, there are no simple injections possible.
* For query user workflow, set user id to `100 or 1=1`
* For query user workflow, set user id to `100 UniOn selselectect * from users`

### Whitelist approach
Gaining information is not possible, but server can be crashed <br>
* For the query user workflow, set userid to `0x313030206f722031203d2031` (This is a hex representation of `100 or 1 = 1`). Since the number is too big for SQLite, it cause a crash of the program.

### Parameterized approach
None <br>
