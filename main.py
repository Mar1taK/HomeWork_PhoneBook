from os.path import exists
from creating_data import creating
from writing_data import writing_scv
from writing_data import writing_txt
from writing_data import writing_scv_name
from writing_data import writing_txt_name

path = 'Phonebook.csv'
meaning = exists(path)
if not meaning:
    creating()

writing_scv()
writing_txt()
writing_scv_name()
writing_txt_name()






