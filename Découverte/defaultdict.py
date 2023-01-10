#python3
# source : https://www.codingame.com/playgrounds/500/advanced-python-features

from collections import defaultdict

my_dict = defaultdict(lambda: 'Default Value')
my_dict['a'] = 42

print(my_dict['a'])
print(my_dict['b'])