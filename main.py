from datetime import datetime, timedelta

birthday_list = [
    {"name": "Olena Shevchenko", "birthday": datetime(year=1990, month=12, day=27)},
    {"name": "Bill Gate", "birthday": datetime(year=1970, month=12, day=26)},
    {"name": "Maria Petrova", "birthday": datetime(year=1980, month=12, day=29)},
    {"name": "Bill X ", "birthday": datetime(year=1991, month=12, day=27)},
    {"name": "Iryna Zakarchuk", "birthday": datetime(year=1975, month=12, day=28)},
    {"name": " Olha Petrova", "birthday": datetime(year=1980, month=12, day=29)},
    {"name": "Ihor Savchuk", "birthday": datetime(year=1990, month=12, day=30)},
    {"name": "Oleksandr Shevchenko", "birthday": datetime(year=1986, month=12, day=20)},
    {"name": "Mykhaylo Mykayvol ", "birthday": datetime(year=1990, month=12, day=31)},
    {"name": "Oleksandra Mykhaivola ", "birthday": datetime(year=1990, month=12, day=28)},
]


def get_birthdays_per_week(users):
    birthdays_per_week = {}
    current_date = datetime.now()
    start = current_date + timedelta(days=1)
    end = start + timedelta(days=6)

    week_days = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    for user in users:
        user['birthday'] = user['birthday'].replace(year=current_date.year)

        if start < user['birthday'] < end:
            d_name = week_days.get(user['birthday'].weekday())

            if d_name == 'Saturday' or d_name == 'Sunday':
                d_name = 'Monday'

            if d_name not in birthdays_per_week:
                birthdays_per_week[d_name] = []
            birthdays_per_week[d_name].append(user['name'])

    for day in week_days.values():
        if day in birthdays_per_week.keys():
            t = ', '.join(birthdays_per_week[day])
            print(f'{day}: {t}')


if __name__ == '__main__':
    get_birthdays_per_week(birthday_list)
