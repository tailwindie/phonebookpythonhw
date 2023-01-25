import check
from export_in_file import export_txt


def start():
    greetings = 'Добро пожаловать в телефонную книгу!\ncreated by Mikhail Kalugin.'

    print(f'{greetings}\n')


def menu():
    what_to_do = 'Что будем делать? Введите соответствующую цифру:'
    new_book = '1. Создать новую книгу или очистить существующую'
    new_contact = '2. Добавить новый контакт'
    change_number = '3. Изменить номер телефона контакта'
    change_surname = '4. Изменить фамилию контакта'
    delete_contact = '5. Удалить контакт'
    view_all_contact = '6. Показать все контакты'
    export_to_file = '7. Экспортировать телефонную книгу в текстовый файл'
    to_exit = '8. Выход'
    print(f'{what_to_do}\n\n{new_book}\n{new_contact}\n{change_number}\n{change_surname}\n{delete_contact}\n{view_all_contact}\n{export_to_file}\n{to_exit}')
    return check.digit_check()
