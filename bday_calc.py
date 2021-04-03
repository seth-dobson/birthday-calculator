'''
Program to calculate the nubmer of days 
until the birthday of each family member
'''

# get required package
import datetime as dt

# get today's date
today = dt.date.today()

# define function
def bday_calc(month, day):
    
    bday0 = dt.date(today.year, month, day)
    bday1 = dt.date(today.year + 1, month, day)
    
    if today < bday0:
        print('Your next birthday is' + ' ' + str((bday0 - today).days) + ' ' + 'days away.')
    else:
        print('Your next birthday is' + ' ' + str((bday1 - today).days) + ' ' + 'days away.')

# get user inputs        
m = input('What month were you born? ')
d = input('What day were you born? ')

# convert string to integer
m = int(m)
d = int(d)

# call function
bday_calc(m,d)
