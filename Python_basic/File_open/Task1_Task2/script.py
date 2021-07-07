from pprint import pprint

FILE_NAME = 'recipes.txt'


def get_ingredient_from_line(line):
    splited_ingredient_line = line.split('|')
    ingredient_name = splited_ingredient_line[0].strip()
    quantity = int(splited_ingredient_line[1].strip())
    measure = splited_ingredient_line[2].strip()
    return {
        'ingredient_name': ingredient_name,
        'quantity': quantity,
        'measure': measure
    }


def get_info_from_file(file):
    cook_book = {}
    with open(file, encoding='utf-8') as file:
        for line in file:
            dish = line.strip()
            cook_book[dish] = []
            ingredients_amount = int(file.readline())
            for _ in range(ingredients_amount):
                ingredient_line = file.readline()
                ingredient = get_ingredient_from_line(ingredient_line)
                cook_book[dish].append(ingredient)
            empty_line = file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient_info in ingredients:
                ingredient_name = ingredient_info['ingredient_name']
                measure = ingredient_info['measure']
                quantity = ingredient_info['quantity'] * person_count
                shop_list[ingredient_name] = {
                    'measure': measure,
                    'quantity': quantity
                }
    return shop_list


if __name__ == '__main__':
    cook_book = get_info_from_file(FILE_NAME)
    shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
