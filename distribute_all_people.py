import csv


def distribute_all_people(name, lst_csv, by_months=True):
    """
    Функция переводит подготовленные двухуровневые списки в csv-формат. На настоящий момент единственная
    возможная опция - распределение по месяцам (для составления плана работы на год).
    :param name: строка, которая будет именем нового файла
    :param lst_csv: двухуровневый список из форматированных под cvs строк
    :param by_months: вывести список подлежащих исследованию, распределенный на группы по месяцам.
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
                if line == 0 and by_months:
                    spamwriter.writerow(lst_csv[line])
                    spamwriter.writerow(['Январь'])
                elif (line // eleven_month_quantity) == 11 and (line % eleven_month_quantity == 0) and by_months:
                    spamwriter.writerow(['Декабрь'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 10 and (line % eleven_month_quantity == 0) and by_months:
                    spamwriter.writerow(['Ноябрь'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 9 and (line % eleven_month_quantity == 0) and by_months:
                    spamwriter.writerow(['Октябрь'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 8 and (line % eleven_month_quantity == 0) and by_months:
                    spamwriter.writerow(['Сентябрь'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 7 and (line % eleven_month_quantity == 0) and by_months:
                    spamwriter.writerow(['Август'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 6 and (line % eleven_month_quantity == 0) and by_months:
                    spamwriter.writerow(['Июль'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 5 and (line % eleven_month_quantity == 0) and by_months:
                    spamwriter.writerow(['Июнь'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 4 and (line % eleven_month_quantity == 0) and by_months:
                    spamwriter.writerow(['Май'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 3 and (line % eleven_month_quantity == 0) and by_months:
                    spamwriter.writerow(['Апрель'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 2 and (line % eleven_month_quantity == 0) and by_months:
                    spamwriter.writerow(['Март'])
                    spamwriter.writerow(lst_csv[line])
                elif (line // eleven_month_quantity) == 1 and (line % eleven_month_quantity == 0) and by_months:
                    spamwriter.writerow(['Февраль'])
                    spamwriter.writerow(lst_csv[line])
                else:
                    spamwriter.writerow(lst_csv[line])
