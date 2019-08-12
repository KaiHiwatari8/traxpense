import datetime

file_name = str(datetime.date.today()) + '.txt'

userId = 'maybejay'
passWord = ''

def write_to_file(text):
    file = open(file_name, 'a')
    file.write(text)
    file.close()

def open_file(name):
    file = open(name, 'r') 
    print('\n' + file.read())
    file.close()