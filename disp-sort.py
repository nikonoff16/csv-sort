import csv
import json
import sys
import re
# just another comment for deleting this time you're reading this


def find_all_people(file_obj, years_dict):   # Индекс нужен чтобы программа сама находила нужные поля в таблице.
    """
    Функция принимает csv-таблицу и словарь списков с годами для каждого вида осмотра, предусмотренного
    законом о проведении диспансеризации (редакции мая 2019 года).
    Возвращает она словарь из двойных списков, отсортированных по признаку принадлежности года рождения к
    той или иной категории.
    """
    reader = csv.reader(file_obj)

    # Берем данные из json-конфига
    result = {}  # В этом словаре будут храниться результаты работы программы, он же и будет выводом функции
    for category in years_dict.keys():
        result[category] = []

    # Настройка служебных переменных.
    index = 0               # Будущий указатель индекса даты в ряде
    first_string = 0        # Переменная, нужная для создания заголовков и верного нахождения индекса даты

    # Цикл ищет всех подлежащих диспансеризации в таблице. 
    for row in reader:
        # Первый блок вставляет строку с заголовками в оба списка и определяет индекс даты в ряде
        if first_string == 0:
            for category in years_dict.keys():
                result[category].append(row)        # Вставляет строку заголовка в каждый из новых списков
            first_string += 1
            continue  # Нужно только здесь, чтобы не вызвать ошибку ошибку типа переменной index.

        # Блок поиска столбца даты.
        elif first_string == 1:                     # Проверяем только на второй строке текста
            text_search_for = r"\d{2}.\d{2}.\d{4}"  # регулярка для поиска даты по четкому шаблону
            for foo in row:
                is_matching = re.search(text_search_for, foo)
                if is_matching and len(foo) == 10:  # На всякий случай проверяем еще и длину строки
                    index = row.index(foo)          # Меняем индекс 0 на найденный интекс даты.
                    break                           # Прерываем поиск, когда находим.
            first_string += 1                       # Делаем этот блок недостпным для исполнения впредь.
    
        # Второй блок осуществяет уже поиск по годам и запись в новые таблицы
        for category in years_dict.keys():      # Раскидываем по новым спискам данные
            if row[index][6:] in years_dict[category]:
                result[category].append(row)

    return result


def distribute_all_people(name, lst_csv):
    """
    Функция переводит подготовленные двухуровневые списки в csv-формат. На настоящий момент единственная
    возможная опция - распределение по месяцам (для составления плана работы на год).
    :param name: строка, которая будет именем нового файла
    :param lst_csv: двухуровневый список из форматированных под cvs строк
    :return: отсутствует. Функция создает и модифицирует файл, не имея непосредственного вывода
    """

    # Если количество элементов списка делится на 11 нацело, то делим на 12 (получаем перегруженный декабрь по итогу)
    if (len(lst_csv) - 1) % 11 == 0:
        eleven_month_quantity = (len(lst_csv) - 1) // 12
    # Если нацело на 11 не делится, то получаем меньшее количество записей на декабрь.
    else:
        eleven_month_quantity = (len(lst_csv) - 1) // 11

    with open(name, "w", newline='') as vd:
            spamwriter = csv.writer(vd)
            for line in range(len(lst_csv)):
                # Вставляем новый заголовок, а затем и очередную строку таблицы, только если кратное от
                # номера линии и среднего для этой таблицы находится в диапазоне 1-11.
                # Прочие случаи описаны в исключениях.
                if line == 0:
                    spamwriter.writerow(lst_csv[line])
                    spamwriter.writerow(['Январь'])
                elif (line // eleven_month_quantity) == 11 and (line % eleven_month_quantity == 0):
                    spamwriter.writerow(['Декабрь'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 10 and (line % eleven_month_quantity == 0):
                    spamwriter.writerow(['Ноябрь'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 9 and (line % eleven_month_quantity == 0):
                    spamwriter.writerow(['Октябрь'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 8 and (line % eleven_month_quantity == 0):
                    spamwriter.writerow(['Сентябрь'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 7 and (line % eleven_month_quantity == 0):
                    spamwriter.writerow(['Август'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 6 and (line % eleven_month_quantity == 0):
                    spamwriter.writerow(['Июль'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 5 and (line % eleven_month_quantity == 0):
                    spamwriter.writerow(['Июнь'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 4 and (line % eleven_month_quantity == 0):
                    spamwriter.writerow(['Май'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 3 and (line % eleven_month_quantity == 0):
                    spamwriter.writerow(['Апрель'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 2 and (line % eleven_month_quantity == 0):
                    spamwriter.writerow(['Март'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 1 and (line % eleven_month_quantity == 0):
                    spamwriter.writerow(['Февраль'])
                    spamwriter.writerow(lst_csv[line])
                else:
                    spamwriter.writerow(lst_csv[line])


with open("years_of_disp.json", "r") as read_file:
    disp_years_dict = json.load(read_file)

# Собственно работа программы.    
if __name__ == "__main__":
    csv_path = sys.argv[1:]     # Сохраняем список файлов из аргументов командной строки в список
    if not csv_path:            # Если список пуст, то даем знать об ошибке.
        print("Программа запущена без указания имен файлов, которые нужно обработать! ")
    else:
        for table in csv_path:
            cs_name = str(csv_path.index(table) + 1)

            with open(table, "r") as f_obj:
                dict_of_year_data = find_all_people(f_obj, disp_years_dict)

            for vd_type in dict_of_year_data.keys():
                distribute_all_people(cs_name + "_" + vd_type + ".csv", dict_of_year_data[vd_type])


