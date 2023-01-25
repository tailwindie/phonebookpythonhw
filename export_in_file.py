import json
import controller
path_to_db = 'db.json'


def export_txt():

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
                with open('Export_contact.txt', 'a') as export:
                    export.write('\n' + "".join(data[i]['Name']) + ' ' + "".join(
                        data[i]['Surname']) + ' ' + "".join(data[i]['Phone number']) + ' ' + "".join(data[i]['Comment']))

    print('\nТелефонная книга успешно экспортирована в текстовый файл!\nНазвание файла: Export_contact.txt\n')
    controller.user_choice()
