import json
import sys

a = sys.argv[1]
b = sys.argv[2]

if a == 'tests.json':
    filename1 = open(a, encoding='utf-8')
    data = json.load(filename1)
    filename2 = open(b, encoding='utf-8')
    data2 = json.load(filename2)
else:
    filename1 = open(b, encoding='utf-8')
    data = json.load(filename1)
    filename2 = open(a, encoding='utf-8')
    data2 = json.load(filename2)



def list_maker(data, list_data = []):
    '''
    Создание промежуточного списка для изятия из него значений.
    :param data: values.json. Содержимое этого файла распаковывается и представляется в виде листа
    :param list_data: Пустой лист для далньнейшего заполнения
    :return: Функция меняющая существующий объект

    Creating an intermediate list to extract values from it
    :param data: values.json. The contents of this file are unpacked and presented as a list
    :param list_data: Blank list for further filling
    :return: A function that changes an existing object
    '''
    if type(data) == dict:
        for k, j in data.items():
            if k == 'id' :
                list_data.append([k, j])
            elif k == 'title':
                list_data[-1].extend([k, j])
            elif k == 'value':
                list_data[-1].extend([k, j])
            else:
                list_maker(j)
    elif type(data) == list:
        for i in data:
            list_maker(i)
    return list_data

def changing(data, data2):
    '''
    Изменение файла tests.json с изменением полей values и сохранением нового файла.
    :param data: tests.json
    :param data2: Лист, результат выполнения list_maker. Из него беруться значения value.
    :return: Функция меняет объект data

    Modifying the tests.json file, changing the values fields and saving the new file
    :param data: tests.json
    :param data2: List, the result of executing list_maker. Values are taken from it
    :return: The function changes the data object
    '''
    if type(data) == dict:
        for k, j in data.items():
            if k == 'id':
                key = j
            if k == 'value':
                for i in range(len(data2)):
                    for l in data2[i]:
                        if l == key:
                            data['value'] = data2[i][3]
            else:
                changing(j, data2)
    elif type(data) == list:
        for i in data:
            changing(i, data2)


d2 = list_maker(data2)
datares = changing(data, d2)

#Recording data
filename = 'report.json'

with open (filename, 'w', encoding = "utf-8") as f:
    json.dump(data, f, ensure_ascii = False, indent= 2)