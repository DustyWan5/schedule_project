############################################
######## Тема урока: Введение в GIT ########
############################################

################### Task ###################         
""" Написать программу, которая запрашивает имена и возраст, записывает в файл csv пока пользователь не перестанет записывать, после этого в определенное время должна срабатывать функция, которая делает рассылку всем пользователяи о новой акции, сообщая, что сейчас действует скидка на алкоголь, нужно использовать модуль для рассылки в определенное время, соответственно те пользователи, которым меньше 18 лет, должны игнорироваться. """

import schedule 
import time 
import csv


def write_csv():
    name = input('Enter your name: ')
    age = input('Enter your age: ')
    with open('users.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter = '/')
        writer.writerow(
            (name, age)
        )
    answ = input('Continue? y or n: ')
    if answ == 'y':
        write_csv()
    else:
        print('Stop!')
    
def mailing():
    with open('users.csv', 'r') as csv_file:
        data = csv_file.readlines()
        names = [i.replace('\n', '') for i in data]
        for i in names:
            name = i.split('/')
            if int(name[-1]) >= 18:
                print(f'Скидки сегодня! {name[0]}')

schedule.every(3).seconds.do(mailing)

while True:
    schedule.run_pending()
    time.sleep(1)
    
# mailing()
# write_csv()
