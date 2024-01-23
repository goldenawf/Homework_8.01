from datetime import date, timedelta


def get_birthdays_per_week(users):
    current_date = date.today()

    birthdays_by_week = {}

    for user in users:
        name = user['name']
        birthday = user['birthday']
        start_of_week = birthday - timedelta(days=birthday.weekday())

        if start_of_week not in birthdays_by_week:
            birthdays_by_week[start_of_week] = []

        birthdays_by_week[start_of_week].append({'name': name, 'birthday': birthday})

    for start_of_week, users_in_week in birthdays_by_week.items():
        end_of_week = start_of_week + timedelta(days=6)

        if any(user['birthday'].weekday() >= 5 for user in users_in_week):
            start_of_week += timedelta(days=1)
            end_of_week += timedelta(days=1)

        if start_of_week <= current_date <= end_of_week:
            users_in_week_names = [user['name'] for user in users_in_week]
            print(f"{start_of_week.strftime('%A')}: {', '.join(users_in_week_names)}")


users = [
    {'name': 'User1', 'birthday': date(2022, 1, 15)},
    {'name': 'User2', 'birthday': date(2022, 1, 16)},
    {'name': 'User3', 'birthday': date(2022, 1, 17)},
    {'name': 'User4', 'birthday': date(2022, 1, 18)},
    {'name': 'User5', 'birthday': date(2022, 1, 19)},
    {'name': 'User6', 'birthday': date(2022, 1, 20)},
    {'name': 'User7', 'birthday': date(2022, 1, 21)},
    {'name': 'User8', 'birthday': date(2022, 1, 22)},
    {'name': 'User9', 'birthday': date(2022, 1, 23)},
    {'name': 'User10', 'birthday': date(2022, 1, 24)},
    {'name': 'User11', 'birthday': date(2022, 1, 25)},
    {'name': 'User12', 'birthday': date(2022, 1, 26)},
    {'name': 'User13', 'birthday': date(2022, 1, 27)},
    {'name': 'User14', 'birthday': date(2022, 1, 28)},
    {'name': 'User15', 'birthday': date(2022, 1, 29)},
    {'name': 'User16', 'birthday': date(2022, 1, 30)},
    {'name': 'User17', 'birthday': date(2022, 1, 31)},
    {'name': 'User18', 'birthday': date(2022, 2, 1)},
    {'name': 'User19', 'birthday': date(2022, 2, 2)},
    {'name': 'User20', 'birthday': date(2022, 2, 3)},
    ]


get_birthdays_per_week(users)
