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
            pass
        elif inp == "o":
            pass
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("There is no such command")
            time.sleep(2)


if __name__ == '__main__':
    main()