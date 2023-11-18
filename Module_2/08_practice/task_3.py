import copy


def replace_product_name(template, product_name):
    if type(template) is str:
        return template.replace('-space-', product_name)
    elif type(template) is dict:
        new_template = {}
        for key, value in template.items():
            new_template[key] = replace_product_name(value, product_name)
        return new_template
    else:
        return template


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам -space- недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на -space-',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

sites_list = []
for i in range(int(input("Сколько сайтов: "))):
    new_site = copy.deepcopy(site)
    product_name = input("Введите название продукта для нового сайта: ")
    new_site = replace_product_name(new_site, product_name)
    sites_list.append((product_name, new_site))
    for j in sites_list:
        print(f"Сайт для {j[0]}: ")
        print(j[1])
