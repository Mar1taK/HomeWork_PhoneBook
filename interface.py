import random

def generator_id():
    Id = '1'
    list_num = list('0123456789')
    random.shuffle(list_num)
    Id += ''.join(list_num[:5])
    return int(Id)

def get_info ():
    info = []
    id = generator_id()
    info.append(id)
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    meaning = False
    while not meaning:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 12:
                print(f'Ошибка! \nНомер телефона должен содержать 12 цифр.')
            else:
                phone_number = int(phone_number)
                meaning = True
        except:
            print('Ошибка, попробуйте еще раз!.')
    info.append(phone_number)
    description = input('Комментарий: ')
    info.append(description)
    return info

