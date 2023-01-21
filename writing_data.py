from interface import get_info as gi

info = gi()

def writing_scv ():
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Id: {info[0]}\n\nФамилия: {info[1]}\n\nИмя: {info[2]}\n\nНомер телефона: {info[3]}\n\nОписание: {info[4]}\n\n\n')

def writing_txt ():
    file = 'Phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Id: {info[0]}\n\nФамилия: {info[1]}\n\nИмя: {info[2]}\n\nНомер телефона: {info[3]}\n\nОписание: {info[4]}\n\n\n')

def writing_scv_name ():
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[1]}\n\nИмя: {info[2]}\n\n')

def writing_txt_name ():
    file = 'Phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[1]}\n\nИмя: {info[2]}\n\n')


