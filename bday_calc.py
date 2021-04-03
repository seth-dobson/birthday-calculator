'''
Program to calculate the nubmer of days 
until the birthday of each family member
'''

import datetime as dt

today = dt.date.today()

def bday_calc(month, day):
    
    bday0 = dt.date(today.year, month, day)
    bday1 = dt.date(today.year + 1, month, day)
    
    if today < bday0:
        print('Your next birthday is' + ' ' + str((bday0 - today).days) + ' ' + 'days away.')
    else:
        print('Your next birthday is' + ' ' + str((bday1 - today).days) + ' ' + 'days away.')

m = input('What month were you born? ')
d = input('What day were you born? ')

m = int(m)
d = int(d)

bday_calc(m,d)
