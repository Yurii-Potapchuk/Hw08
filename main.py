import datetime as DT


users = [
        {'name':'Mykola', 'birthday':DT.datetime(1996, 6, 30)},
        {'name':'Ivan', 'birthday':DT.datetime(1994, 6, 28)},
        {'name':'Petro', 'birthday':DT.datetime(1987, 7,21)},
        {'name':'Yurii', 'birthday':DT.datetime(1988, 8, 13)},
        {'name':'Olga', 'birthday':DT.datetime(1987, 1, 13)},
        {'name':'Nataliia', 'birthday':DT.datetime(2001, 7, 4)},
        {'name':'Maxym', 'birthday':DT.datetime(2001, 5, 3)},
        {'name':'Robert', 'birthday':DT.datetime(1994, 4, 6)},
        {'name':'Katia', 'birthday':DT.datetime(1999 , 12, 16)},
        {'name':'Dasha', 'birthday':DT.datetime(1989, 9, 22)}
          ]

WEEKDAYS = dict(Monday = [], 
                  Tuesday = [],
                  Wednesday = [],
                  Thursday = [],
                  Friday = [],
                  Saturday = [],
                  Sunday = [])


next_week = (DT.datetime.now() + DT.timedelta(days=7)).date()


def get_this_year_birthday(user):
    dt = user['birthday']
    new_dt = DT.datetime(DT.datetime.now().year, dt.month, dt.day)
    return new_dt


def get_weekday(user):
    return user['birthday'].strftime("%A")


def get_birthdays_per_week(users):
    for user in users:
        if get_this_year_birthday(user) > DT.datetime.now() and get_this_year_birthday(user).date() < next_week:
            if get_weekday(user) in ['Saturday', 'Sunday']:
                WEEKDAYS['Monday'].append(user['name'])
            else:
                WEEKDAYS[get_weekday(user)].append(user['name'])
    for day, value in WEEKDAYS.items():
        if len(value)>0:
            print('{:<15} : {:<100} '.format(day, ', '.join(value)))


if __name__ == '__main__':
    get_birthdays_per_week(users)