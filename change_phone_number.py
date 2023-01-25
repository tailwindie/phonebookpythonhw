import json
import controller


path_to_db = 'db.json'


def change_phone_number():  
    name = input('Введите имя или фамилию контакта, чей номер будем менять:  ')
   
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)

        _ = 0

        for i in range(0, len(data)):  

            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Phone number'] = input(f'Введите новый номер телефона для {name}: ')
                print('\nНомер успешно изменён!\n')
                pass

            elif name != data[i]['Name'] and name != data[i]['Surname']:
                _ += 1
                if _ == len(data):
                    print('Контакта с такими именем или фамилией нет!')

    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    controller.user_choice()