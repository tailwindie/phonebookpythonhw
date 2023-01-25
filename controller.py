
import add_contact as ac
import user_interface as ui
import change_phone_number as cpn
import change_surname as cs
import delete_contact as dc
import view_all_contacts as vac
import export_in_file as eif


def user_choice():

    choice_num = ui.menu()
    if choice_num < 1 or choice_num > 8:
        print('\nПохоже, что вы ввели что-то неверно.\nНеобходимо ввести цифру от 1 до 8.\n')
        user_choice()
    elif choice_num == 1:
        ac.create_json()
    elif choice_num == 2:
        ac.add_to_json()
    elif choice_num == 3:
        cpn.change_phone_number()
    elif choice_num == 4:
        cs.change_surname()
    elif choice_num == 5:
        dc.delete_contact()
    elif choice_num == 6:
        vac.view_all_contacts()
    elif choice_num == 7:
        eif.export_txt()
    elif choice_num == 8:
        exit()
