from datetime import datetime
import datetime
import os


base_path = os.path.dirname(__file__)
dir_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(dir_path, 'eugene_okulik', 'hw_13', 'data.txt')
# print(file_path)


def open_file(file_path):
    with open (file_path, 'r', encoding = 'utf-8') as file_name:
        for line in file_name.readlines():
            yield line


# for data_line in open_file(file_path):
#     with open ('read.txt', 'a', encoding= 'utf-8') as new_file:
#         new_file.write(data_line)

file_read_path = os.path.join(base_path, 'read.txt')
data_file = open_file(file_read_path)

list_date = []

for line in data_file:
    line = line.split(' ')
    date_line = ' '.join(line[1:3])
    list_date.append(date_line)

time1, time2, time3 = list_date
now = datetime.datetime.now()
time_format = '%Y-%m-%d %H:%M:%S.%f'


def convert_time_format(time_input, time_format):
    time_obj = datetime.datetime.strptime(time_input, time_format)
    return time_obj


task_time_1 = convert_time_format(time1, time_format) + datetime.timedelta(weeks=1)
print(task_time_1)
task_time_2 = convert_time_format(time2, time_format).strftime('%A')
print('День недели: ' + task_time_2)
task_time_3 = now - convert_time_format(time3, time_format)
print(task_time_3.days)
