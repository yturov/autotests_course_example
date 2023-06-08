# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
with open('test_file/task1_data.txt', mode='r', encoding='utf-8') as f_start:
    with open('test_file/task1_answer.txt', mode='w', encoding='utf-8') as f_finish:
        for line in f_start:
            line_without_digits = "".join(i for i in line if not i.isdigit())
            f_finish.write(line_without_digits)
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
