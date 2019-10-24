import copy
a = (1,2,3)
b = copy.copy(a)
c = copy.deepcopy(a)

print(id(a),id(),id(c))