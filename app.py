import mariadb
from dbhelpers import connect_db, execute_statement, close_connection


def original():
    print("Welcome to Hacker Protocol")
    print("Please log in fellow Hacker: ")
    verify_user()
    while True:
        print("Please select from the following:\
            \n1. Enter a new exploit\
            \n2. See all of your exploits\
            \n3. See all other exploits by everyone except for the logged in user\
            \n4. Exit the application")
        choice = int(input("Please make a choice: "))
        if choice == 1:
            enter_exploit()
        elif choice == 2:
            user_id = int(input("Enter Hacker ID again: "))
            view_exploit(user_id)
        elif choice == 3:
            user_id = int(input("Hacker please re-enter your UserID#: "))
            specific_exploit(user_id)
        elif choice == 4:
            break
        else:
            print("Please choose from the following options only: ")


def verify_user():
    cursor = connect_db()
    alias = input("Enter alias: ")
    password = input("Enter password: ")
    if cursor == None:
        print("Connection failed")
    else:
        result = execute_statement(cursor, "CALL log_user_cmd(?,?)", [alias, password])
        print(result)
        if result:
            for id in result:
                print("You are now logged in Hacker# {}".format(id[0]))
                return result
        else:
            print("Login Failed. Hacker not found! ")
            verify_user()


def enter_exploit():
    cursor = connect_db()
    content = input("Enter content: ")
    user_id = int(input("Enter user_id: "))
    if cursor == None:
        print("Connection failed")
    else:
        result = execute_statement(cursor, "CALL enter_exploit_cmd(?,?)", [content, user_id])
        print(result)
        print("Content inserted successfully")
    # Result is None as it's an insert query so print will be none. Checked on DB to see if query worked 
    # and it is, as new posts are showing up in DB
    close_connection(cursor)


def view_exploit(user_id):
    cursor = connect_db()
    if cursor == None:
        print("Connection failed")
    else: 
        result = execute_statement(cursor, "CALL see_exploits_cmd(?)", [user_id])
        print("Here are all your exploits: ")
        print(result)
        # print("{}".format(result[1]))
        # print("{}".format(result[2]))
    close_connection(cursor)


def specific_exploit(user_id):
    cursor = connect_db()
    # user_id = int(input("Enter current logged in User#: "))
    if cursor == None:
        print("Connection failed")
    else:
        result = execute_statement(cursor, "CALL exception_exploit_cmd(?)", [user_id])
        print("Here are the resulting exploits excluding logged in Hacker: ", result)
    close_connection(cursor)


original()

# Bonus Option 3 completed and added to specific exploit function
# verify_user()
# enter_exploit()
# user_id = int(input("Enter Hacker ID: "))
# view_exploit(user_id)
# user_id = int(input("Enter current logged in User#: "))
# specific_exploit(user_id)
# exit_hacker()