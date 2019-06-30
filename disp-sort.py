import csv, re


#TODO - перенести определения списков в .json файл, настроить функцию на принятие значений по умолчанию.
def find_all_people(file_obj):  # Индекс нужен для того, чтобы программа сама находила нужные поля в таблице.
    """
    Функция возвращает два списка - первый - диспансеризация раз в три года, второй - раз в два года.
    Она сама находит в списках столбик с датами рождения и проверяет каждую строку по этому столбику. 
    """
    reader = csv.reader(file_obj)

    # Пока нет нужды создавать отдельные внешние переменные для этих списков:
    # Программа просто не будет нужна так долго.
    #TODO - актуализировать списки, добавить список профосмотров.
    three_years_vd = {
             '1998', '1995', '1992', '1989', '1986', '1983', '1980', '1977',
             '1974', '1971', '1968', '1965', '1962', '1959', '1956', '1953',
             '1950', '1947', '1944', '1941', '1938', '1935', '1932', '1929',
             '1926', '1923', '1920'
             }
    two_years_vd = {
             '1970', '1969', '1967', '1966', '1964', '1963', '1961', '1960',
             '1958', '1957', '1955', '1954', '1952', '1951', '1949', '1948',
             '1946'
             }
    general_vd = []  # Список ВД раз в 3 года
    suppl_vd = []    # Список ВД раз в 2 года
    index = 5       # Будущий указатель индекса даты в ряде
    first_string = 0 # Переменная, нужная для создания заголовков и верного нахождения индекса даты

    # Цикл ищет всех подлежащих диспансеризации в таблице. 
    for row in reader:
        """"Первый блок вставляет строку с заголовками в оба списка и определяет индекс даты в ряде"""
        if first_string == 0:
            general_vd.append(row)
            suppl_vd.append(row)
            first_string += 1
            continue  # Нужно только здесь, чтобы не вызвать ошибку ошибку типа переменной index.
        # elif first_string == 1:
        #     text_search_for = (r"\d{2}.\d{2}.\d{4}")
        #     for foo in row:
        #         print("Here I am")
        #         if re.search(text_search_for, foo) and (len(foo) == 10):
        #             index = row.index(foo)
        #             print(index)
        #     first_string += 1
    
        """Второй блок осуществяет уже поиск по годам и запись в новые таблицы"""
        
        if row[index][6:] in three_years_vd:  # обращение по срезу - указание на год в полученной записи
            # print(row)
            general_vd.append(row)
        elif row[index][6:] in two_years_vd:
            # print(row)
            suppl_vd.append(row)
      
    
    return general_vd, suppl_vd

def distribute_all_people(name, lst_csv):
    if (len(lst_csv) - 1) % 11 == 0:
        eleven_month_quantity = (len(lst_csv) - 1) // 12
        december_quantity = (len(lst_csv) - 1) // 12 + (len(lst_csv) - 1) % 12
    else:
        eleven_month_quantity = (len(lst_csv) - 1) // 11
        december_quantity = (len(lst_csv) - 1) % 11
    print(eleven_month_quantity, december_quantity)

    with open(name, "w", newline='') as vd:
            spamwriter = csv.writer(vd)
            for line in range(len(lst_csv)):
                # spamwriter.writerow(line)
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



# Собственно работа программы.    
if __name__ == "__main__":
    csv_path = ["test.csv",]
    for table in csv_path:
        cs_name = str(csv_path.index(table) + 1)
    
        with open(table, "r") as f_obj:
            thr_vd, tw_vd = find_all_people(f_obj)

        distribute_all_people(cs_name + "_gen_vd.csv", thr_vd)
        distribute_all_people(cs_name + "_suppl_vd.csv", tw_vd)
        #TODO - дописать вывод списка профосмотров

     
    
