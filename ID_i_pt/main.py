from functions import data
from functions import users
import os
import time 

def program_menu()->None:
        print(
    """
    ================================================
    \n
    e - exit
    w - add user
    t - edit user
    r - data inf
    y - find user by id
    u - find user by name
    i - delete user by id
    o - update user name
    j - update user surname
    h - update user birth date
    n - is name taken
    m - show one user
    p - count all users
    f - count users with missing name
    l - average math for user
    b - average polish for user
    s - average english for user
    v - overall average for user
    \n
    ================================================
    """)


def main(): 
    loaded_data:list[dict] = data.read_data()
    while True:
        program_menu()
        inp = input("- ").lower().strip()
        if inp == "e":
            print("The program has finished running")
            data.save_data(loaded_data)
            break
        elif inp == "w":
            new_user = users.add_new_user(loaded_data)
            loaded_data.append(new_user)
            data.save_data(loaded_data)
        elif inp == "r":
            data.print_all_data(loaded_data)
        elif inp == "t":
            users.add_or_remove_grades(loaded_data)
            data.save_data(loaded_data)
        elif inp == "y":            
            users.find_user_by_id(loaded_data)
        elif inp == "u":
            users.find_users_by_name(loaded_data)
        elif inp == "i":
            users.delete_user_by_id(loaded_data)
            data.save_data(loaded_data)
        elif inp == "o":
            users.update_user_name(loaded_data)
            data.save_data(loaded_data)
        elif inp == 'j':
            users.update_user_surname(loaded_data)
            data.save_data(loaded_data)
        elif inp == 'h':
            users.update_user_birth_date(loaded_data)
            data.save_data(loaded_data)
        elif inp == 'n':
            users.is_name_taken(loaded_data)
        elif inp == 'm':
            users.show_one_user(loaded_data)
        elif inp == 'p':
            users.count_all_users(loaded_data)
        elif inp == 'f':
            users.count_users_with_missing_name(loaded_data)
        elif inp == 'l':
            users.average_math_for_user(loaded_data)
        elif inp == 'b':
            users.average_polish_for_user(loaded_data)
        elif inp == 's':
            users.average_english_for_user(loaded_data)
        elif inp == 'v':
            users.overall_average_for_user(loaded_data)

        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("There is no such command")
            time.sleep(2)


if __name__ == '__main__':
    main()