import numpy as np 
import matplotlib.pyplot as plt
from einops import rearrange, repeat
import math 

#Lists
x = list()
y = []
x = list((1,2,4,8))
y = [1,2, 4, 10, 20, 40]
print('About x: ')
print('type(x) - ', type(x))
print('x       - ', x)
print('len(x)  - ', len(x))
print(' ')
print('About y:')
print('type(y) - ', type(y))
print('y       - ', y)
print('len(y)  - ', len(y))

#indexing lists
x_1 = x[2]
y_1 = y[2:]
print('x[2] - ', x_1)
print('y[2] - ', y_1)

#Tuples
x = tuple((2,2))
y = (2,2)
print(type(x))
print(x)
print(type(y))
print(y)

#dict
dict = {}
dict['inception'] = {'int': 1, 'str': 'hello','list': [1,2]}
inception_str = dict['inception']['str']
print(inception_str)