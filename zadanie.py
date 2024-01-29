from datetime import datetime, timedelta


def get_birthdays_per_week(users_list):
    today = datetime.now()
    end_of_next_week = today + timedelta(days=14)

    birthdays_in_next_week = {}

    for user in users_list:
        name = user['name']
        birth_date = user['birthday']

        birth_date = birth_date.replace(year=today.year)

        if today <= birth_date <= end_of_next_week:
            day_of_week = birth_date.strftime("%A")

            if day_of_week in ['Saturday', 'Sunday']:
                day_of_week = 'Monday'

            if day_of_week not in birthdays_in_next_week:
                birthdays_in_next_week[day_of_week] = [name]
            else:
                birthdays_in_next_week[day_of_week].append(name)

    return birthdays_in_next_week


users_list = [
    {'name': 'Jan', 'birthday': datetime(1900, 1, 27)},
    {'name': 'Anna', 'birthday': datetime(1900, 2, 15)},
    {'name': 'Kamil', 'birthday': datetime(1900, 1, 20)},
    {'name': 'User1', 'birthday': datetime(2022, 1, 15, 0, 0)},
    {'name': 'User2', 'birthday': datetime(2022, 1, 16, 0, 0)},
    {'name': 'User3', 'birthday': datetime(2022, 1, 17, 0, 0)},
    {'name': 'User4', 'birthday': datetime(2022, 1, 18, 0, 0)},
    {'name': 'User5', 'birthday': datetime(2022, 1, 19, 0, 0)},
    {'name': 'User6', 'birthday': datetime(2022, 1, 20, 0, 0)},
    {'name': 'User7', 'birthday': datetime(2022, 1, 21, 0, 0)},
    {'name': 'User8', 'birthday': datetime(2022, 1, 22, 0, 0)},
    {'name': 'User9', 'birthday': datetime(2022, 1, 23, 0, 0)},
    {'name': 'User10', 'birthday': datetime(2022, 1, 24, 0, 0)},
    {'name': 'User11', 'birthday': datetime(2022, 1, 25, 0, 0)},
    {'name': 'User12', 'birthday': datetime(2022, 1, 26, 0, 0)},
    {'name': 'User13', 'birthday': datetime(2022, 1, 27, 0, 0)},
    {'name': 'User14', 'birthday': datetime(2022, 1, 28, 0, 0)},
    {'name': 'User15', 'birthday': datetime(2022, 1, 29, 0, 0)},
    {'name': 'User16', 'birthday': datetime(2022, 1, 30, 0, 0)},
    {'name': 'User17', 'birthday': datetime(2022, 1, 31, 0, 0)},
    {'name': 'User18', 'birthday': datetime(2022, 2, 1, 0, 0)},
    {'name': 'User19', 'birthday': datetime(2022, 2, 2, 0, 0)},
    {'name': 'User20', 'birthday': datetime(2022, 2, 3, 0, 0)}
]


birthdays_next_week_result = get_birthdays_per_week(users_list)

for day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    users_in_day = birthdays_next_week_result.get(day_of_week, [])
    users_str = ', '.join(users_in_day)
    if users_str:
        print(f"{day_of_week}: {users_str}")

