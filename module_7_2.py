def custom_write(file_name, strings):
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')
    for idx, string in enumerate(strings, start=1): # start=1 начало нумерации строк на вывод
        # не забыть - enumerate выдает индекс элемента в strings
        byte_position = file.tell()
        file.write(string + '\n')
        strings_positions[(idx, byte_position)] = string  # idx - индекс строки (номер)

    return strings_positions


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)

    # Вывод результата на консоль
    for elem in result.items():
        print(elem)
