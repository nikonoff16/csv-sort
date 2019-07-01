import csv, json, re


def find_all_people(file_obj, years_dict):   # Индекс нужен чтобы программа сама находила нужные поля в таблице.
    """
    Функция возвращает два списка - первый - диспансеризация раз в три года, второй - раз в два года.
    Она сама находит в списках столбик с датами рождения и проверяет каждую строку по этому столбику. 
    """
    reader = csv.reader(file_obj)

    # Берем данные из json-конфига
    three_years_vd = years_dict['three_years_vd']
    two_years_vd = years_dict['two_years_vd']
    prof_osm = years_dict['prof_osm']
    general_vd = []         # Список ВД раз в 3 года®
    suppl_vd = []           # Список ВД раз в 2 года
    prof_vd = []            # Список подлежащих профосмотру
    index = 5               # Будущий указатель индекса даты в ряде
    first_string = 0        # Переменная, нужная для создания заголовков и верного нахождения индекса даты

    # Цикл ищет всех подлежащих диспансеризации в таблице. 
    for row in reader:
        """"Первый блок вставляет строку с заголовками в оба списка и определяет индекс даты в ряде"""
        if first_string == 0:
            general_vd.append(row)
            suppl_vd.append(row)
            prof_vd.append(row)
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
        elif row[index][6:] in prof_osm:
            prof_vd.append(row)
    
    return general_vd, suppl_vd, prof_vd


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


with open("years_of_disp.json", "r") as read_file:
    disp_years_dict = json.load(read_file)

# Собственно работа программы.    
if __name__ == "__main__":
    csv_path = ["test.csv",]  #TODO: сделать ввод файлов через аргументы командной строки.
    for table in csv_path:
        cs_name = str(csv_path.index(table) + 1)

        with open(table, "r") as f_obj:
            thr_vd, tw_vd, prof_vd = find_all_people(f_obj, disp_years_dict)

        distribute_all_people(cs_name + "_gen_vd.csv", thr_vd)
        distribute_all_people(cs_name + "_suppl_vd.csv", tw_vd)
        distribute_all_people(cs_name + "_prof_vd.csv", prof_vd)

