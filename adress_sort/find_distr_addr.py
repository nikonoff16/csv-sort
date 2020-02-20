import json

try:
    with open("distrs.json", "r") as read_json:
        district = json.load(read_json)
        for key, value in district.items():
                district[key] = set(value)

except FileNotFoundError:
    district = {}  # здесь храним учатски

stop_mark = False

while not stop_mark:
    user_input = input("Введите запись в формате 'участок(цифрой) улица дом(или диапазон через дефис)': ").split()
    if len(user_input) >= 3:
        key = user_input[0].lower()
        value = set()
        if '-' in user_input[2]:
            rng = user_input[2].split('-')
            for num in range(int(rng[0]), int(rng[1])+1):
                value.add(user_input[1] + ' ' + str(num))
        else:
            for num in user_input[2:]:
                value.add(user_input[1] + ' ' + num)
        
        if key in district.keys():
            district[key] = district[key].union(value)
            print(district)
        else:
            district[key] = value
            print(district)
        with open("distrs.json", "w") as write_json:
            lst_dist = district.copy()
            for key, value in lst_dist.items():
                lst_dist[key] = list(value)
            json.dump(lst_dist, write_json, indent=4, ensure_ascii=False)
    elif user_input[0] == "exit":
        stop_mark = True
    else:
        print("Строка не соответствует параметрам. Повторите ввод.")

