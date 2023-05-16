def create_dict(file_path):
    book_dict = {}
    with open(file_path, 'r') as f:
        str_list = f.readlines()
    number = -1
    for string in str_list:
        string = string.rstrip()
        if number == 0:
            number -= 1
        elif number == -1:
            book_dict[string] = []
            number = -2
            name = string
        elif number == -2:
            number = int(string)
        else:
            ingridient = string.split(' | ')
            book_dict[name] += [{'ingredient_name': ingridient[0], 'quantity': int(ingridient[1]), 'measure': ingridient[2]}]
            number -= 1

    return book_dict


def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    cook_book = create_dict('book.txt')
    for name in dishes:
        cook = cook_book[name]
        for dishe in cook:
            if shop_dict.get(dishe['ingredient_name']) == None:
                shop_dict[dishe['ingredient_name']] = {'quantity': person_count * dishe['quantity'], 'measure': dishe['measure']}
            else:
                shop_dict[dishe['ingredient_name']]['quantity'] += person_count * dishe['quantity']

    return shop_dict


print(create_dict('book.txt'))
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))