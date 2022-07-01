from datetime import datetime


def getDay(date):
    date = str(date).replace('.', '').replace('-', ' ').split()
    date = [int(i) for i in date]
    year, month, day = date
    current_day = datetime(year, month, day)
    print(datetime.now())
    return current_day.strftime('%A').upper()


