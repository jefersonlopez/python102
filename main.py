import random

'''
# conjuntos

set_comuntries = {'col', 'mex', 'bol'}
print(set_comuntries)
set_from_string = set('hola')
print(set_from_string)
set_from_tuples = set(('a', 'b', 'c', 'a'))
print(set_from_tuples)
set_from_list = set([2, 5, 5, 6, 4, 6, 1])
print(set_from_list)

#crud

#add
set_comuntries.add('pe')
print(set_comuntries)

#update
set_comuntries.update(('cos', 'gua'))
print(set_comuntries)

#remove

set_comuntries.remove('col')
print(set_comuntries)

set_comuntries.discard('arg')
print(set_comuntries)

set_comuntries.clear()
print(set_comuntries)


#operaciones de conjuntos
set_a = {'col', 'mex', 'bol'}
set_b = {'per', 'bol'}

print(set_a)
print(set_b)

set_c = set_a.union(set_b)
print(set_c)
set_c = set_a.intersection(set_b)
print(set_c)

set_c = set_a.difference(set_b)
print(set_c)

set_c = set_a.symmetric_difference(set_b)
print(set_c)

#list comprehensions 

numbers = []
for element in range(1,12):
    numbers.append(element)

print(numbers)

numbers_2 = [element for element in range(1,15)]
print(numbers_2)

numbers_3 = [element for element in range(1,15) if element % 2 == 0]
print(numbers_3)


#dictionary comprehension

dict = {}
for i in range(1,6):
    dict[i] = i*2
print(dict)

dict_2 = {i : i*2 for i in range(1,7)}
print(dict_2)

countries = ['col', 'mex', 'bol', 'per']
population = {}
for country in countries:
    population[country] = random.randint(1,100)

print(population)

population_2 = {country : random.randint(1,100) for country in countries}
print(population_2)

names = ['nico', 'juan', 'santi']
ages = [5, 6, 7]
print(list(zip(names, ages)))

new_dict = {names:ages for (names,ages) in zip(names, ages)} 
print(new_dict)

countries = ['col', 'mex', 'bol', 'per']
population_2 = {country : random.randint(1,100) for country in countries}
print(population_2)

result = {country : population for (country, population) in population_2.items() if population > 20}
print(result)
cont = 0
text = 'Hola, soy jeferson'
count = []
unique = {c : 0 for c in text if c in 'aeiou'}
print(unique)
for c in text:
    if c in 'aeiou':
        unique[c] += 1
print(unique)

vocal = {key : 0 for key in 'aeiou'}
print(vocal)



from pkg.mod1 import func_1, func_2
print(func_1())
'''
import pkg
print(pkg.mod1.func_2())
 