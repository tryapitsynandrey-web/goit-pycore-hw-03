from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - given_date).days
    except ValueError:
        raise ValueError("Дата повинна бути у форматі 'YYYY-MM-DD'")
print(get_days_from_today("2021-10-09"))