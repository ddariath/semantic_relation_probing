import pandas as pd
import os
from main import hyper, hypon, single
import random

my_cwd = os.getcwd() + '/data/bigdata'


def get_data(list_of_files, stop_symbs):
    alls = []
    res = []
    for file in list_of_files:
        path = os.path.join(my_cwd, file)
        data_pd = pd.read_csv(path)
        data = data_pd['itemLabel'].tolist()
        alls.extend(data)
    for item in alls:
        if any(chr.isdigit() for chr in item) is False and any(symb in item for symb in stop_symbs) is False:
            res.append(item)
    return res


# ГОРОДА
pattern_single_cities_big = 'Город [A] [value], а значит у него большая [attribute].'
pattern_single_cities_small = 'Город [A] [value], а значит у него маленькая [attribute].'

cities_data = get_data(['more_cities_ru.csv', 'more_cities.csv'], './, ')
hyper_cities = hyper(cities_data[:100])
hypon_cities = hypon(cities_data[:100])
single_cities = single(pattern_single_cities_big, pattern_single_cities_small, cities_data,
                       'площадь', 'большой', 'маленький')
with open(my_cwd + '/more_cities_txt.txt', 'a', encoding='utf-8') as f:
    for line in random.sample(hyper_cities[0], 1000) + random.sample(hyper_cities[1], 1000):
        f.write(f'{line};cities;hyperonym;города\n')
    for line in random.sample(hypon_cities, 1000):
        f.write(f'{line};cities;hyponym;Москва\n')
    for line in single_cities[0] + single_cities[1]:
        f.write(f'{line};cities;attribute;площадь\n')
    for line in single_cities[2]:
        f.write(f'{line};cities;value;большой\n')
    for line in single_cities[3]:
        f.write(f'{line};cities;value;маленький\n')

# ЛЮДИ
pattern_single_big = '[A] [value], а значит у него большое [attribute].'
pattern_single_small = '[A] [value], а значит у него маленькое [attribute].'

people_data = get_data(['more_people.csv'], './,')
hyper_people = hyper(people_data)
hypon_people = hypon(people_data)
single_people = single(pattern_single_big, pattern_single_small, people_data, 'состояние', 'богатый', 'бедный')
with open(my_cwd + '/more_people_txt.txt', 'a', encoding='utf-8') as f:
    for line in random.sample(hyper_people[0], 1000) + random.sample(hyper_people[1], 1000):
        f.write(f'{line};people;hyperonym;люди|имена\n')
    for line in random.sample(hypon_people, 1000):
        f.write(f'{line};people;hyponym;Иван\n')
    for line in single_people[0] + single_people[1]:
        f.write(f'{line};people;attribute;состояние\n')
    for line in single_people[2]:
        f.write(f'{line};people;value;богатый\n')
    for line in single_people[3]:
        f.write(f'{line};people;value;бедный\n')

# МЕТАЛЛЫ
pattern_single_big = '[A] [value], а значит у него большой [attribute].'
pattern_single_small = '[A] [value], а значит у него маленький [attribute].'

metals_data = get_data(['more_metals.csv'], './, ')
hyper_metals = hyper(metals_data)
hypon_metals = hypon(metals_data)
single_metals = single(pattern_single_big, pattern_single_small, metals_data, 'вес', 'тяжелый', 'легкий')
with open(my_cwd + '/more_metals_txt.txt', 'a', encoding='utf-8') as f:
    for line in random.sample(hyper_metals[0], 1000) + random.sample(hyper_metals[1], 1000):
        f.write(f'{line};metals;hyperonym;металлы|элементы\n')
    for line in random.sample(hypon_metals, 1000):
        f.write(f'{line};metals;hyponym;медь\n')
    for line in single_metals[0] + single_metals[1]:
        f.write(f'{line};metals;attribute;вес\n')
    for line in single_metals[2]:
        f.write(f'{line};metals;value;тяжелый\n')
    for line in single_metals[3]:
        f.write(f'{line};metals;value;легкий\n')

# ИМЕНА
pattern_single_big = '[A] [value], а значит у него большое [attribute].'
pattern_single_small = '[A] [value], а значит у него маленькое [attribute].'
pattern_single_big2 = '[A] [value], а значит у него большой [attribute].'
pattern_single_small2 = '[A] [value], а значит у него маленький [attribute].'

names_data = get_data(['more_names.csv'], './, ')
hyper_names = hyper(names_data)
hypon_names = hypon(names_data)
single_names = single(pattern_single_big, pattern_single_small, names_data, 'состояние', 'богатый', 'бедный')
single_names2 = single(pattern_single_big, pattern_single_small, names_data, 'рост', 'высокий', 'низкий')
with open(my_cwd + '/more_names_txt.txt', 'a', encoding='utf-8') as f:
    for line in random.sample(hyper_names[0], 1000) + random.sample(hyper_names[1], 1000):
        f.write(f'{line};names;hyperonym;имена|люди\n')
    for line in random.sample(hypon_names, 1000):
        f.write(f'{line};names;hyponym;Иван\n')
    for line in single_names[0] + single_names[1]:
        f.write(f'{line};names;attribute;состояние\n')
    for line in single_names[2]:
        f.write(f'{line};names;value;богатый\n')
    for line in single_names[3]:
        f.write(f'{line};names;value;бедный\n')
    for line in single_names2[0] + single_names2[1]:
        f.write(f'{line};names2;attribute;рост\n')
    for line in single_names2[2]:
        f.write(f'{line};names2;value;высокий\n')
    for line in single_names2[3]:
        f.write(f'{line};names2;value;низкий\n')