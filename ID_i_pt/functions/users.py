from random import randint

def generate_unique_id(data: list[dict]) -> int:
    lst_id = []
    for user in data:
        lst_id.append(user.get('id'))
    new_id = randint(1, 1000000)
    while new_id in lst_id:
        new_id = randint(1, 1000000)
    return new_id

def add_new_user(data: list[dict])-> dict:
    return {
        "id": generate_unique_id(data),
        "name": input("Enter name: ").strip().lower() or None,
        "surname":input("Enter surname: ").strip().lower() or None,
        "date of birth":input("date of birth: ").strip().lower() or None,
        "grades mathematics": [],
        "grades polish": [], 
        "grades english":[]        
    }

def add_or_remove_grades(data: list[dict]):
    id_name_inp = input("podaj id usera: ").lower().strip()
    for el in data:
        if str(el["id"]) == id_name_inp or el["name"].lower() == id_name_inp:
            #print(el["name"])
            print('grades:')
            for k,v in el.items():
                if k[:6] == 'grades':
                    print(f"  {k[7:]} ----- {v}")
            przedmiot_inp = input('podaj nazwe przedmiotu')
            for k, v in el.items():
                if k[7:] == przedmiot_inp:
                    grade_id_inp = int(input('podaj nr oceny do zmiany, zaczynajac od 0, większa doaje '))
                    
                    grade_inp = int(input('podaj ocene, -1 usuwa,'))
                    if grade_id_inp < len(v):
                        if grade_inp < 0:
                            del v[grade_id_inp]
                        else:
                            v[grade_id_inp] = grade_inp
                    else:
                        if grade_inp >= 0: 
                            v.append(grade_inp)
            break
    if str(el["id"]) != id_name_inp and el["name"].lower() != id_name_inp:
        print('nie ma takiego numeru')    

def find_user_by_id(data: list[dict]) -> None:
    inp_user_id = input('podaj id urzytkownika: ')
    for el in data:
        if str(el["id"]) == inp_user_id:
            print(f'{el}')
            break
    else:
        print('nie ma takiego urzytkownika')

def find_users_by_name(data: list[dict]) -> list[dict]:
    inp_user_name = input('podaj imie urzytkownika: ')
    for el in data:
        if str(el["name"]) == inp_user_name:
            print(f'{el}')
            break
        elif inp_user_name == None:
            find_user_by_id()
        
    else:
        print('nie ma takiego urzytkownika')


