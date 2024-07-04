import datetime


date2 = 'Jan 15, 2023 - 12:05:33'


def converse_date():
    python_date = datetime.datetime.strptime(date2, '%b %d, %Y - %H:%M:%S')
    print(python_date)
    print(python_date.strftime('%B'))
    print(python_date.strftime('%d.%m.%Y, %H:%M'))


converse_date()
