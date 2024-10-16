def custom_write(file_name: str, strings: list):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i, string in enumerate(strings, start=1):
        pos_file = file.tell()  # текущая позиция
        file.write(f'\n {string}') # Строки из strings
        strings_positions[(i, pos_file)] = string  # Добавляем информацию о строке в словарь
    file.close()

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
