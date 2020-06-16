import copy
a = (1,2,3,[3,34,4])
b = copy.copy(a)
c = copy.deepcopy(a)

print(id(a))
print(id(b))
print(id(c))    # a为不可变数据类型，两者都为指向、引用， 为可变时，c 改变为重新指向一个地址空间。
