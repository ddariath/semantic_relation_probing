import pandas as pd
import re


def hyper(data):
    l = len(data)
    first_pattern = '[A], [B] и [C] - это [MASK].'
    # second_pattern = '[MASK], например [A], [B] или [C].'
    second_pattern = 'Такие [MASK], как [A], [B] или [C].'
    res_1 = []
    res_2 = []
    for i in range(l - 2):
        pattern_1 = re.sub('\[A]', data[i].title(), first_pattern)
        pattern_2 = re.sub('\[A]', data[i], second_pattern)
        for j in range(i + 1, l - 1):
            pattern_1 = re.sub('\[B]', data[j], pattern_1)
            pattern_2 = re.sub('\[B]', data[j], pattern_2)
            for f in range(j + 1, l):
                s1 = re.sub('\[C]', data[f], pattern_1)
                s2 = re.sub('\[C]', data[f], pattern_2)
                res_1.append(s1)
                res_2.append(s2)
    return res_1, res_2


def hypon(data):
    l = len(data)
    pattern = '[A], [MASK] и [C].'
    res = []
    for i in range(l - 1):
        new_pattern = re.sub('\[A]', data[i].title(), pattern)
        for j in range(i + 1, l):
            s = re.sub('\[C]', data[j], new_pattern)
            res.append(s)
    return res


def compare(pattern, data, val1, val2, attr):
    res_1 = []
    res_2 = []
    res_3 = []
    l = len(data)
    # сразу формируем предложения со скрытым value и attribute

    for i in range(l - 1):

        pattern_val = re.sub('\[attribute]', '[MASK]', pattern)  # attribute masked
        pattern_attr = re.sub('\[value]', '[MASK]', pattern)  # value masked

        pattern_val_1 = re.sub('\[value]', val1, pattern_val)
        pattern_val_2 = re.sub('\[value]', val2, pattern_val)

        pattern_attr = re.sub('\[attribute]', attr, pattern_attr)

        pattern_val_1 = re.sub('\[A]', data[i], pattern_val_1)
        pattern_val_2 = re.sub('\[A]', data[i], pattern_val_2)
        pattern_attr = re.sub('\[A]', data[i], pattern_attr)
        for j in range(i + 1, l):
            s1 = re.sub('\[B]', data[j], pattern_val_1)
            s2 = re.sub('\[B]', data[j], pattern_val_2)
            s3 = re.sub('\[B]', data[j], pattern_attr)
            res_1.append(s1)  # Чтобы понять, что больше, Железногорск или Энгельс, необходимо знать их [mask].
            res_2.append(s2)  # Чтобы понять, что меньше, Королёв или Одинцово, необходимо знать их [mask].
            res_3.append(s3)  # Чтобы понять, что [mask], Королёв или Одинцово, необходимо знать их площадь.
    return res_1, res_2, res_3


def single(pattern1, pattern2, data, attr, value1, value2):
    # [A] большой, значит у него большая [attr]
    res_1 = []
    res_2 = []
    res_3 = []
    res_4 = []
    l = len(data)
    for i in range(l):
        pattern_val_1 = re.sub('\[attribute]', '[MASK]', pattern1)
        pattern_val_2 = re.sub('\[attribute]', '[MASK]', pattern2)
        pattern_val_1 = re.sub('\[value]', value1, pattern_val_1)
        pattern_val_2 = re.sub('\[value]', value2, pattern_val_2)
        pattern_attr_1 = re.sub('\[value]', '[MASK]', pattern1)
        pattern_attr_2 = re.sub('\[value]', '[MASK]', pattern2)
        pattern_attr_1 = re.sub('\[attribute]', attr, pattern_attr_1)
        pattern_attr_2 = re.sub('\[attribute]', attr, pattern_attr_2)
        s1 = re.sub('\[A]', data[i].title(), pattern_val_1)
        s2 = re.sub('\[A]', data[i].title(), pattern_val_2)
        s3 = re.sub('\[A]', data[i].title(), pattern_attr_1)
        s4 = re.sub('\[A]', data[i].title(), pattern_attr_2)
        res_1.append(s1)
        res_2.append(s2)
        res_3.append(s3)
        res_4.append(s4)
    return res_1, res_2, res_3, res_4


cities_pd = pd.read_csv('./data/cities.csv')
cities = cities_pd['itemLabel'].tolist()[:30]

hyper_cities = hyper(cities)
cities_list_hyper_1 = hyper_cities[0]  # Железногорск, Набережные Челны и Салават - это [mask].
cities_list_hyper_2 = hyper_cities[1]  # [mask], например Железногорск, Набережные Челны или Салават.
cities_list_hypon = hypon(cities)  # Железногорск, [mask] и Одинцово.

pattern_comp_1 = 'Чтобы понять, что [value], [A] или [B], необходимо знать их [attribute].'
pattern_comp_2 = 'Надо знать [attribute], чтобы понять что [value], [A] или [B].'
pattern_comp_3 = 'Что [value] и, соответственно, имеет больше [attribute], [A] или [B]?'
pattern_comp_4 = 'Что [value] и, соответственно, имеет меньше [attribute], [A] или [B]?'

compare_cities_1 = compare(pattern_comp_1, cities, 'больше', 'меньше', 'площадь')
cities_list_comp_big_1 = compare_cities_1[0]
# Чтобы понять, что больше, Железногорск или Одинцово, необходимо знать их [mask].
cities_list_comp_small_1 = compare_cities_1[1]
# Чтобы понять, что меньше, Железногорск или Одинцово, необходимо знать их [mask].
cities_list_comp_attr_1 = compare_cities_1[2]
# Чтобы понять, что [mask], Железногорск или Одинцово, необходимо знать их площадь.
compare_cities_2 = compare(pattern_comp_2, cities, 'больше', 'меньше', 'площадь')
cities_list_comp_big_2 = compare_cities_2[0]  # Надо знать [mask], чтобы понять что больше, Железногорск или Одинцово.
cities_list_comp_small_2 = compare_cities_2[1]  # Надо знать [mask], чтобы понять что меньше, Железногорск или Одинцово.
cities_list_comp_attr_2 = compare_cities_2[2]  # Надо знать площадь, чтобы понять что [mask], Железногорск или Одинцово.
compare_cities_3 = compare(pattern_comp_3, cities, 'больше', 'меньше', 'площадь')
compare_cities_4 = compare(pattern_comp_4, cities, 'больше', 'меньше', 'площадь')
cities_list_comp_big_quest = compare_cities_3[0]
# Что больше и, соответственно, имеет больше [mask], Железногорск или Одинцово?
cities_list_comp_small_quest = compare_cities_4[1]
# Что меньше и, соответственно, имеет меньше [mask], Железногорск или Одинцово?
cities_list_comp_attr_quest = compare_cities_3[2] + compare_cities_4[2]
# Что [mask] и, соответственно, имеет больше площадь, Железногорск или Одинцово?

pattern_single_cities_big = 'Город [A] [value], а значит у него большая [attribute].'
pattern_single_cities_small = 'Город [A] [value], а значит у него маленькая [attribute].'

single_cities = single(pattern_single_cities_big, pattern_single_cities_small, cities,
                       'площадь', 'большой', 'маленький')
cities_list_single_big_val = single_cities[0]  # Город Набережные Челны большой, а значит у него большая [MASK].
cities_list_single_small_val = single_cities[1]  # Город Железногорск маленький, а значит у него маленькая [MASK].
cities_list_single_big_attr = single_cities[2]  # Город Волжский [MASK], а значит у него большая площадь.
cities_list_single_small_attr = single_cities[3]  # Город Энгельс [MASK], а значит у него маленькая площадь.

