import os
import time


directory = os.getcwd()
print(directory)

for root, dirs, files in os.walk(directory):  # для обхода каталога, путь к которому указывает переменная directory
    for file in files:
        filepath = os.path.join(root, file)  # для формирования полного пути к файлам
        filetime = os.path.getmtime(filepath)  # для получения и
        # отображения времени последнего изменения файла.
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  #
        filesize = os.path.getsize(filepath)  # для получения размера файла
        parent_dir = os.path.dirname(filepath)  # для получения родительской директории файла
        print(f'Обнаружен файл: {file}, Путь: {filepath}, '
              f'Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
