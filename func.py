import functools
import random

'''
def my_print():
    print('this is my print')

def func(arg1=1, arg2=1, arg3=1):
    sal1 = arg1*2
    sal2 = arg2*4
    sal3 = arg3*6
    return sal1, sal2, sal3

a = func(arg3=6, arg2= 4)

print(a)
#print(b)
#print(c)
name = 'jeferson'
last_name = 'lopez'
full_name = lambda name, last_name : f'full name: {name} {last_name}'
#text = full_name(name, last_name)
print(full_name(name, last_name))

high_ord_func = lambda x , func : x + func(x)

print(high_ord_func(3, lambda x : x + 1))
print(high_ord_func(3, lambda y : y ** 2))


numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]
print(numbers_1+numbers_2)
numbers_3 = list(map(lambda x, y : x + y, numbers_1, numbers_2))
print(numbers_3)

items = [
    {
        'product' : 'shirt',
        'price' : 1200
    },
    {
        'product' : 'suit',
        'price' : 2300
    },
    {
        'product' : 'pants',
        'price' : 800
    }
]
lista = []
for item in items:
    lista.append(item['price'])

print('nueva lista\n',items)

new_dict = items
print('new dict 2',new_dict)

#print(list(map(lambda item : item['price'], items)))

def add_taxes (dict):
    new_dict = dict.copy()
    new_dict['taxes'] = new_dict['price'] * 0.19
    return new_dict

new_items = list(map(add_taxes, items))
print('nueva lista\n',items)
print('nueva lista con taxes\n',new_items)


numbers = [2,6,4,8,5,3,4,6,7,23,4,6,4,456,45,2354,342,345,]

pair = list(filter(lambda x : x % 2 == 0, numbers))
print(pair)

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(matches)
print(len(matches))

new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

print(new_list)
print(len(new_list))

print(matches)
print(len(matches))


numbers = [2,6,4,8,5,3,4,6,7,23,4,6,4,456,45,2354,342,345,]

result = functools.reduce(lambda counter, item : counter + item , numbers)
print(result)
print(type(result))

'''
