import argparse
import os 
import json
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
    args = parser.parse_args()
    return args

def find_all_people(file_name, years_dict):
    file_name.encode('unicode_escape')
    read_file = pd.read_excel(file_name)
    # read_file.to_csv (r'result.csv', index = None, header=True)

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

    for spread_sh in args.files:
        print(spread_sh)
        find_all_people(spread_sh, disp_years_dict)
    

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()