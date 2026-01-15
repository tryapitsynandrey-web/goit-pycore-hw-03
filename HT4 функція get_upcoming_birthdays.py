from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_date:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result

users = [
    {"name": "John Doe", "birthday": "1985.01.11"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Michael Brown", "birthday": "1988.01.10"},
    {"name": "Emily Johnson", "birthday": "1992.01.25"},
    {"name": "David Wilson", "birthday": "1980.01.26"},
    {"name": "Sarah Taylor", "birthday": "1995.01.28"},
    {"name": "Daniel Anderson", "birthday": "1987.01.29"},
    {"name": "Olivia Thomas", "birthday": "1991.01.09"},
    {"name": "Robert Jackson", "birthday": "1979.02.01"},
    {"name": "Sophia White", "birthday": "1993.02.02"},
    {"name": "James Harris", "birthday": "1984.02.03"},
    {"name": "Emma Martin", "birthday": "1996.02.04"},
    {"name": "William Thompson", "birthday": "1982.02.05"},
    {"name": "Ava Garcia", "birthday": "1994.02.06"},
    {"name": "Alexander Martinez", "birthday": "1989.02.07"},
    {"name": "Mia Robinson", "birthday": "1997.02.08"},
    {"name": "Ethan Clark", "birthday": "1986.02.09"},
    {"name": "Isabella Lewis", "birthday": "1998.02.10"},
    {"name": "Noah Walker", "birthday": "1990.02.11"},
    {"name": "Charlotte Hall", "birthday": "1983.02.12"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:")
for user in upcoming_birthdays:
    print(f"{user['name']:20} {user['congratulation_date']}")
