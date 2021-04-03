'''
Program to calculate the nubmer of days 
until the birthday of each family member
'''

import datetime as dt

today = dt.date.today()

def bdayOptions(month, day):
    bday0 = dt.date(today.year, month, day)
    bday1 = dt.date(today.year + 1, month, day)
    
    bday_options = [bday0, bday1]
    
    return(bday_options)

gen_bday = bdayOptions(3, 16)
gid_bday = bdayOptions(11, 12)
cor_bday = bdayOptions(11, 27)
mom_bday = bdayOptions(11, 20)
dad_bday = bdayOptions(2, 23)


def daysUntilBday(name, bday0, bday1):
    if today < bday0:
        print(name + ' ' + str((bday0 - today).days))
    else:
        print(name + ' ' + str((bday1 - today).days))

daysUntilBday('Gen', gen_bday[0], gen_bday[1])
daysUntilBday('Gid', gid_bday[0], gid_bday[1])
daysUntilBday('Cor', cor_bday[0], cor_bday[1])
daysUntilBday('Mom', mom_bday[0], mom_bday[1])
daysUntilBday('Dad', dad_bday[0], dad_bday[1])
