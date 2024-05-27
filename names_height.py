from main import compare, single
import random
import os
import pandas as pd

my_cwd = os.getcwd() + '/data'
new_dir = 'names_height'
path = os.path.join(my_cwd, new_dir)
os.mkdir(path)


names_pd = pd.read_csv('./data/names.csv')
names = names_pd['itemLabel'].tolist()


pattern_comp_1 = 'Чтобы понять, кто [value], [A] или [B], необходимо знать их [attribute].'
pattern_comp_2 = 'Надо знать [attribute], чтобы понять кто [value], [A] или [B].'
pattern_comp_3 = 'Кто [value] и, соответственно, имеет больше [attribute], [A] или [B]?'
pattern_comp_4 = 'Кто [value] и, соответственно, имеет меньше [attribute], [A] или [B]?'

compare_1 = compare(pattern_comp_1, names, 'выше', 'ниже', 'рост')
list_comp_big_1 = compare_1[0]
list_comp_small_1 = compare_1[1]
list_comp_attr_1 = compare_1[2]

compare_2 = compare(pattern_comp_2, names, 'выше', 'ниже', 'рост')
list_comp_big_2 = compare_2[0]
list_comp_small_2 = compare_2[1]
list_comp_attr_2 = compare_2[2]

compare_3 = compare(pattern_comp_3, names, 'выше', 'ниже', 'рост')
compare_4 = compare(pattern_comp_4, names, 'выше', 'ниже', 'рост')
list_comp_big_quest = compare_3[0]
list_comp_small_quest = compare_4[1]
list_comp_attr_quest = compare_3[2] + compare_4[2]

res_2 = random.sample(list_comp_big_1, 5) + random.sample(list_comp_big_2, 5) + random.sample(
    list_comp_small_1, 5) + random.sample(list_comp_small_2, 5) + random.sample(list_comp_big_quest, 5) + random.sample(
    list_comp_small_quest, 5)
with open(path + '/names2_comp_attrmasked.txt', 'a', encoding='utf-8') as f:
    for line in res_2:
        f.write(line + '\n')

res_3 = random.sample(list_comp_attr_1, 8) + random.sample(list_comp_attr_2, 8) + random.sample(list_comp_attr_quest, 8)
with open(path + '/names2_comp_valmasked.txt', 'a', encoding='utf-8') as f:
    for line in res_3:
        f.write(line + '\n')

pattern_single_big = '[A] [value], а значит у него большой [attribute].'
pattern_single_small = '[A] [value], а значит у него маленький [attribute].'

single = single(pattern_single_big, pattern_single_small, names, 'рост', 'высокий', 'низкий')
list_single_big_val = single[0]
list_single_small_val = single[1]
list_single_big_attr = single[2]
list_single_small_attr = single[3]

res_4 = random.sample(list_single_big_val, 10) + random.sample(list_single_small_val, 10)
with open(path + '/names2_single_attrmasked.txt', 'a', encoding='utf-8') as f:
    for line in res_4:
        f.write(line + '\n')

res_5 = random.sample(list_single_big_attr, 10) + random.sample(list_single_small_attr, 10)
with open(path + '/names2_single_valmasked.txt', 'a', encoding='utf-8') as f:
    for line in res_5:
        f.write(line + '\n')
