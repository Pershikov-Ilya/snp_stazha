from datetime import datetime, timedelta


def date_in_future(days):
    if isinstance(days, int):
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
    else:
        future_date = datetime.now()

    return future_date.strftime('%d-%m-%Y %H:%M:%S')


print(date_in_future([]))
print(date_in_future(2))
print(date_in_future("fghdfgh"))
print(date_in_future(365))
print(date_in_future(3.4))