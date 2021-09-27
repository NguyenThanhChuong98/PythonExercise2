from datetime import datetime

get_date = datetime.now()


def extract(x):
    year = lambda x: x.year
    month = lambda x: x.month
    day = lambda x: x.day
    t = lambda x: x.time()
    print(year(x))
    print(month(x))
    print(day(x))
    print(t(x))


extract(get_date)
