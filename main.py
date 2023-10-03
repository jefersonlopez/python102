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
'''

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