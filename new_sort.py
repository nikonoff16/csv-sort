import argparse
import os 
import json
import re
import csv
from datetime import datetime
import xlwt
try: 
   import pandas as pd
except ModuleNotFoundError:
   import sys 
   print("Для работы программы требуются библиотеки pandas и xlrd")
   print("Установите их командой 'pip install pandas xlrd'")
   print("В Unix-подобных системах эта команда будет такой: 'pip3 install pandas xlrd'")
   sys.exit(1)

def transit_args(curr_dir):
    """
    Обрабатываем аргументы командной строки отдельной функцией
    Аргумент curr_dir передает как дефолтные значения список подходящих файлов
    из текущей директории. Если пользователь желает сам указать файлы в другой локации,
    ему следует указать аргумент --files и указать файлы с их адресами.
    """
    parser = argparse.ArgumentParser(description="Скрипт для анализа прикрепленных к участку людей и помощи в планировании диспансеризации")
    parser.add_argument('-f', '--files', nargs='+', default=curr_dir, help='через пробел укажите файлы с относительными или абсолютными адресами')                                                
    parser.add_argument("-v", "--verbose", action="store_true", help="Вывести в консоль результаты работы")
    parser.add_argument("-m", "--months", action="store_true", help="Распланировать ВД и ПО по месяцам")
    parser.add_argument("-csv","--to_csv", action="store_true", help="Вывести итоговые списки в формате csv (planned option)")
    parser.add_argument("-win", "--windows_symb", action="store_true", help="Не использовать UTF-8 (planned option)")
    parser.add_argument("-d", "--debug", action="store_true", help="Выключить скрытие ошибок обработки исходных файлов")
    args = parser.parse_args()

    return args

def find_all_people(file_name, years_dict):
    """
    Функция принимает строку - имя файла в формате excel и словарь со списками для разных видов ВД
    Возвращает словарь с объектами типа DataFrame в качестве значений
    """
    file_name.encode('unicode_escape')
    read_file = pd.read_excel(file_name)
    result = {}
    birth_date = 'дата рождения'
    year_col = 'year'
    # делаем заголовки менее разнообразными (хотя всех проблем это не решает)
    read_file.columns = read_file.columns.str.strip().str.lower()

    # создаем служебную колонку для удобной сортировки по годам
    read_file[year_col] = read_file[birth_date]
    # TODO: научить читать даты в формате float64. Пока читаем только строки. Документ следует подготовить
    for num in range(1910, 2020):
        pat = r'\d{2}.\d{2}.' + str(num)
        read_file[year_col] = read_file[year_col].str.replace(pat, str(num))  # Прописываем сюда год в формате ГГГГ

    # сортируем таблицу, собственно
    for category in years_dict.keys():
        dist_years = read_file.loc[read_file[year_col].isin(years_dict[category])]  # выбираем все подходящие года
        dist_years = dist_years.drop(columns=year_col)  # удаляем служебную колонку
        # name = category + '.csv'
        # dist_years.to_csv(name, index=None, header=True)
        result[category] = dist_years

    return result

def distribute_all_people(name, lst_csv, by_months):
    """
    Не функцция, а говна кусок. Переделать

    """
    lst_csv.to_excel(name + ".xls")
    return None



def main():
    """
    Точка входа в программу. 
    """

    # Находим в текущей директории подходящие файлы
    fs = os.listdir()
    curr_dir = []
    for document in fs:
        if '.xls' == document[-4:] or '.xlsx' == document[-5:]:
            curr_dir.append(document)
    args = transit_args(curr_dir)  # Передаем найденные файлы как дефолтный параметр

    # Подгружаем информацию о видах диспансеризации и их годах
    with open("years_of_disp.json", "r") as read_file:
        disp_years_dict = json.load(read_file)

    # Сортируем файлы по категориям
    for spread_sh in args.files:
        print(spread_sh)
        if args.debug:
            dict_of_year_data = find_all_people(spread_sh, disp_years_dict)
        else:
            try:
                dict_of_year_data = find_all_people(spread_sh, disp_years_dict)
            except Exception:
                print("Файл", spread_sh, "не удалось обработать, он будет пропущен.")
                print("Для выяснения причин запустите программу с аргументами  -f", spread_sh, "--debug")
                continue

        # формируем имя для директории и префикс для файлов
        distr_num_pattern = r"\d+"                          # Производим поиск номера участка в названии
        distr_number = re.search(distr_num_pattern, spread_sh)
        if distr_number:
            cs_name = distr_number.group()                  # Если находим - передаем его в префикс имени
        else:
            cs_name = str(args.files.index(spread_sh) + 1)        # Если нет - генерируем из его из позиции в списке
        
        # создаем директорию и помещаем туда результаты работы файла
        try:
            os.mkdir(path=cs_name + '_distr')
        except OSError:
            print("Подкаталог не может быть создан. Видимо, имена файлам даны не последовательно.")
            print("Исправьте проблему с именами (расставьте в названиях уникальные номера учатсков")
            print("или удалите их вовсе),и запустите скрипт снова.")
            sys.exit(1)
        for vd_type in dict_of_year_data.keys():
            name = cs_name + '_distr' + '/' + cs_name + '_' + vd_type  # + '.csv'
            distribute_all_people(name, dict_of_year_data[vd_type], args.months)
        

    

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()