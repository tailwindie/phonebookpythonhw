

def digit_check():
    try:
        input_number = int(input('\nВведите цифру: \n'))
        return input_number
    except ValueError:
        print('Похоже, вы ввели что-то не то. Нужна цифра от 1 до 8.\n')
        return digit_check()