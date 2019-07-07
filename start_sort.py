import sys
import json
import distribute_all_people
import find_all_people

with open("years_of_disp.json", "r") as read_file:
    disp_years_dict = json.load(read_file)

# Собственно работа программы.
if __name__ == "__main__":
    csv_path = sys.argv[1:]     # Сохраняем список файлов из аргументов командной строки в список
    if not csv_path:            # Если список пуст, то даем знать об ошибке.
        print("Программа запущена без указания имен файлов, которые нужно обработать! ")
    else:
        month = True  # Значение по умолчанию - выдавать списки с помесячным распределением граждан
        users_will = input('''По умолчанию программа выдаст списки граждан с распределением по месяцам
         Если вам нужно вывести лишь список подлежащих обследованиям граждан за год, введите "Да": ''')
        if users_will in ["Да", "Да ", "да", "да ", "ДА", "ДА ", "д", "д ", "Д", "Д ", "Yes", "Y", "yes", "y"]:
            month = False
            print("\nПрограмма выдаст списки без разбивки по месяцам.")
        print("\nПрограмма выдаст списки с распределением по месяцам.")
        for table in csv_path:
            cs_name = str(csv_path.index(table) + 1)

            with open(table, "r") as f_obj:
                dict_of_year_data = find_all_people.find_all_people(f_obj, disp_years_dict)

            for vd_type in dict_of_year_data.keys():
                distribute_all_people.distribute_all_people(cs_name + "_" + vd_type + ".csv",
                                                            dict_of_year_data[vd_type], by_months=month)
    print("\nРабота программы завершена. Готовые списки пронумерованы в соответствии с порядком ввода при запуске.")
    print("Они расположены в директории, где находится эта программа. По всем вопросам обращаться к Осипову В.Ю.")
