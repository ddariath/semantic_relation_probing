from main import cities_list_hyper_1, cities_list_hyper_2
from main import cities_list_hypon
from main import cities_list_comp_big_1, cities_list_comp_small_1, cities_list_comp_big_2, cities_list_comp_small_2, \
    cities_list_comp_big_quest, cities_list_comp_small_quest
from main import cities_list_comp_attr_1, cities_list_comp_attr_2, cities_list_comp_attr_quest
from main import cities_list_single_big_val, cities_list_single_small_val, cities_list_single_small_attr, \
    cities_list_single_big_attr
import random

my_cwd = os.getcwd() + '/data'
new_dir = 'cities'
path = os.path.join(my_cwd, new_dir)
os.mkdir(path)

res = random.sample(cities_list_hyper_1, 10) + random.sample(cities_list_hyper_2, 10)
with open(path + '/city_file.txt', 'a', encoding='utf-8') as f:
    for line in res:
        f.write(line + '\n')

with open(path + '/city_hypon.txt', 'a', encoding='utf-8') as f:
    for line in random.sample(cities_list_hypon, 10):
        f.write(line + '\n')

res_2 = random.sample(cities_list_comp_big_1, 5) + random.sample(cities_list_comp_big_2, 5) + random.sample(
    cities_list_comp_small_1, 5) + random.sample(cities_list_comp_small_2, 5) + random.sample(
    cities_list_comp_big_quest, 5) + random.sample(cities_list_comp_small_quest, 5)
with open(path + '/city_comp_attrmasked.txt', 'a', encoding='utf-8') as f:
    for line in res_2:
        f.write(line + '\n')

res_3 = random.sample(cities_list_comp_attr_1, 8) + random.sample(
    cities_list_comp_attr_2, 8) + random.sample(cities_list_comp_attr_quest, 8)
with open(path + '/city_comp_valmasked.txt', 'a', encoding='utf-8') as f:
    for line in res_3:
        f.write(line + '\n')

res_4 = random.sample(cities_list_single_big_val, 10) + random.sample(cities_list_single_small_val, 10)
with open(path + '/city_single_attrmasked.txt', 'a', encoding='utf-8') as f:
    for line in res_4:
        f.write(line + '\n')

res_5 = random.sample(cities_list_single_big_attr, 10) + random.sample(cities_list_single_small_attr, 10)
with open(path + '/city_single_valmasked.txt', 'a', encoding='utf-8') as f:
    for line in res_5:
        f.write(line + '\n')
