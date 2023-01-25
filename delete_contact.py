import json
import controller


path_to_db = 'db.json'


def delete_contact():
    name = input('Введите имя или фамилию контакта, которого надо удалить:  ')

    _ = 0

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)

        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                del data[i]
                print('\nКонтакт удалён!\n')
                pass

            elif name != data[i]['Name'] and name != data[i]['Surname']:
                _ += 1
                if _ == len(data):
                    print('Контакта с такими именем или фамилией нет!')

    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    controller.user_choice()
