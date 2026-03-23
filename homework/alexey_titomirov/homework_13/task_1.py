import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(eugene_file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


count_string = 1
for data_line in read_file():
    if count_string == 1:
        data_line_date = datetime.fromisoformat(data_line[3:29])
        print(data_line_date + timedelta(weeks=1))
        count_string += 1
    elif count_string == 2:
        data_line_date = datetime.fromisoformat(data_line[3:29])
        weekday = data_line_date.strftime('%A')
        print(weekday)
        count_string += 1
    elif count_string == 3:
        data_line_date = datetime.fromisoformat(data_line[3:29])
        today = datetime.now()
        days_ago = (today - data_line_date).days
        print(days_ago)
