# Задача 1

import os
def fillcook(addres = "~/Users/andreymikshta/Desktop/Netology/HW/7"):
    cookbook = {} # то, что мы хотим вернуть в конце
    file = open("recepies.txt", encoding='utf-8')
    dishes = file.read().split('\n' * 2) # список строк-блоков для каждого блюда
    file.close()

    def get_ing(stro): # хотим вспомогательной функцией уметь возвращать из блока текста -> (название блюда, словарь ингредиентов)
        subdish = stro.split('\n') # по формату делим блок текста по переносам строки
        # print(subdish)
        dish = []
        for i in range(int(subdish[1])): # вторая строка = число строк, идущих в блоке далее
            spis = subdish[2 + i].split(' | ') # строки далее поделены через данный разделитель, сделаем из них список
            dish.append({'ingredient_name': spis[0], 'quantity': int(spis[1]), 'measure': spis[2]})
            # print(dish)
        return subdish[0], dish
    

    for el in dishes: # применим к каждому блоку нашу функцию, распакуем её значения и заполним пустой до того момента словарь
        key, value = get_ing(el)
        cookbook[key] = value
    # и вернём его
    return cookbook

# проверим задание
cook_book = fillcook('recepies.txt') # создадим/скачаем заранее файл, где будут в том формате находиться данные для кулинарной книги

print("Вывод для задачи 1:")
print(cook_book)


print('\n')

# Задача 2

def get_shop_list_by_dishes(dishes, person_count): # хотим вернуть словарь ингредиентов
    shopdict = {} # наш желаемый для вывода словарь

    for dish in dishes: #пойдём по строкам-блюдам из списка блюд
        for dishdict in cook_book[dish]: # заглянем по этому блюду во внешний словарь, глобальную переменную
            # это список словарей, в каждом из которых есть ingredient_name, quantity, measure
            # возьмём имя ингредиента по ключу
            ingred = dishdict['ingredient_name'] 
            if ingred in shopdict: # если в нашем желаемом словаре был такой ключ, то к значению добавим столько, сколько по рецепту нужно, домноженное на число персон
                shopdict[ingred]['quantity'] += dishdict['quantity'] * person_count
            else: # если в желаемом словаре не было такого ключа, то создадим по ключу словарь
                shopdict[ingred] = {}
                shopdict[ingred]['quantity'] = dishdict['quantity'] * person_count
                shopdict[ingred]['measure'] = dishdict['measure']
            
    return shopdict

print("Вывод для задачи 2:")
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print()
# Задача 3

list_files = ['1.txt', '2.txt', '3.txt']
def sortfiles(list_files): # пойдём по списку файлов 
    # научимся работать с одним:
    def file_info(addr):
        file = open(addr, encoding='utf-8')
        lines = file.readlines()
        length = len(lines)
        return length, addr, lines  # передадим в кортеже (длину (чтобы по ней отсортировать), имя файла, список строк)

    # этот список нам в будущем поможет с выводом
    final_list = []
    for elem in list_files:
        final_list.append(file_info(elem)) # будем пошагово добавлять кортежи в список

    final_list.sort() # отсортируем, что требуется в задаче

    # пойдём на финишную прямую: откроем файл на запись со стиранием предыдущих данных 
    file = open('finalfile.txt', 'w', encoding='utf-8')
    for elem in final_list:
        # формат требует сначала имя файла, потом длину, поэтому в другом порядке их напечатаем в файл
        file.write(elem[1] + '\n' + str(elem[0]) + '\n')
        # 3й элемент кортежа - список, поэтому по циклу его напечатаем
        for stroka in elem[2]:
            file.write(stroka) # т.к. readlines() возвращает строки с \n на конце, то дополнительные \n ставить не нужно
        file.write('\n') # но у последней строки не будет переноса, посему искусственно его запишем в файл
    file.close()
    for element in final_list:
        print(element)

sortfiles(['1.txt', '2.txt', '3.txt']) # не забудем заранее скачать файлы перед выполнением команды

