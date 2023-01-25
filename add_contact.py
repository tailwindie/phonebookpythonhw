import json
import controller
from random import randint


def create_json():
    json_data = []
    with open('db.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    controller.user_choice()


def add_to_json():
    print('Создаём новый контакт:')
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите коментарий: ')
    json_data = {
        "ID": randint(10000, 99999),
        "Name": name,
        "Surname": surname,
        "Phone number": phone,
        "Comment": comment,
    }
    data = json.load(open("db.json"))
    data.append(json_data)

    with open("db.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print('\nНовый контакт успешно добавлен!\n')
    controller.user_choice()
