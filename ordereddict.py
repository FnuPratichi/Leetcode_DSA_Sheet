from collections import OrderedDict
my_list = [('a',1),('z',3),('a',2),('c',0)]
my_ordered_dict = OrderedDict(my_list)
print(my_ordered_dict)

new_list = [('k',10)]
new_ordered_dict = OrderedDict(new_list)
print(new_ordered_dict)

new_ordered_dict.update(my_ordered_dict)
print(new_ordered_dict)