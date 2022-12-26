from datetime import datetime, timedelta

users_birthday = [
    {"name": "Olena Shevchenko", "birthday": datetime(year=1990, month=12, day=27)},
    {"name": "Bill Gate", "birthday": datetime(year=1970, month=12, day=26)},
    {"name": "Maria Petrova", "birthday": datetime(year=1980, month=11, day=6)},
    {"name": "Bill X ", "birthday": datetime(year=1991, month=11, day=6)},
    {"name": "Iryna Zakarchuk", "birthday": datetime(year=1975, month=12, day=28)},
    {"name": " Olha Petrova", "birthday": datetime(year=1980, month=12, day=29)},
    {"name": "Ihor Savchuk", "birthday": datetime(year=1990, month=12, day=30)},
    {"name": "Oleksandr Shevchenko", "birthday": datetime(year=1986, month=11, day=20)},
    {"name": "Mykhaylo Mykayvol ", "birthday": datetime(year=1990, month=12, day=31)},
    {"name": "Oleksandra Mykhaivola ", "birthday": datetime(year=1990, month=11, day=17)},
]



def find_interval():
    if datetime.now().weekday() == 5:  # if today is Saturday
        interval = timedelta(days=6)
    elif datetime.now().weekday() == 6:  # if today is Sunday
        interval = timedelta(days=5)
    else:  #  if there is  working day
        interval = timedelta(days=7)
    return interval



def get_birthdays_per_week(users):
    celebrating_birthbays = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }

    interval = find_interval()
    future_daytime = datetime.now() + interval

    for person in users:
        this_year_birthday = datetime(year=datetime.now().year, month=person.get("birthday").month,
                                      day=person.get("birthday").day)

        if datetime.now() <= this_year_birthday <= future_daytime:
            weekday_string = this_year_birthday.strftime("%A")
            if weekday_string in ["Saturday", "Sunday"]:
                weekday_string = "Monday"
            celebrating_birthbays.get(weekday_string).append(person.get("name"))
    print_birthday_people(celebrating_birthbays)


def print_birthday_people(celebrating_birthbays: dict):
    for key, value in celebrating_birthbays.items():
        if value:
            print(f"{key}: {', '.join(value)}")


if __name__ == "__main__":
    get_birthdays_per_week(users_birthday)
