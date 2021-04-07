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
        print(f'Your next birthday is {(bday0 - today).days} days away.')
    else:
        print(f'Your next birthday is {(bday1 - today).days} days away.')

# get user inputs
while True:
    try:
        m = int(input('What month were you born? '))
        break
    except ValueError:
        print('Oops! You did not enter a valid number. Please try again...')

while True:
    try:
        d = int(input('What day were you born? '))
        break
    except ValueError:
        print('Oops! You did not enter a valid number. Please try again...')

# call function
bday_calc(m,d)
