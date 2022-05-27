# *args and **kwargs

from ast import arg


def func1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


def func2(arg1=None, arg2=None, arg3=None):
    print(arg1, arg2, arg3)


args = [1, 2, 3]
kwargs = {"arg2": 2, "arg1": 5, "arg3": 3}

func2(**kwargs)

lst = [[1,2],[3,4],[5,6],[-1,0],[2,3],[-5,4]]

def sort_func(x):
    return x[0] + x[1]

lst.sort(key = lambda x: x[1] + x[0])
print(lst)

tup = (1,2,3,4,5)
a , *b ,c = tup
print (a, b, c)

# x, y = map(int, input("Enter multiple values: ").split())
# print(type(x),type(y))
# print(f"so x = {int(x)} , y = {int(y)}")
# x , y = y, x
# print(x, y)
# z = [[i*j for i in range(5)] for j in range (5)]
# print(z)
# word = " hello you are piece of shit "
# print(len(word))
# x = {char: word.count(char) for char in set(word)}
# print(x)
# name = ["Tim", "Jack","Schooby","Lance"]
# age = [21, 18,23,44]
# color = ["black","white","yellow","brown"]
# print(list(zip(name,age,color)))
# for name, age in zip(name,age):
#     if age >= 23:
#         print(name)