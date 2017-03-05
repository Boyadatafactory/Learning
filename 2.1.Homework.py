with open('2.1.food.txt') as f:
    cook_book = f.read().split()
    print(cook_book)

cook_book = {
       'омлет': [
           {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
           {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
        ],
       'стейк': [
           {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
           {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
           {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
        ],
       'салат': [
           {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
           {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
           {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
           {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'гр.'}
        ],
        }

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
         for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
               shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
               shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))

def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюдо в расчете на 1 человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()