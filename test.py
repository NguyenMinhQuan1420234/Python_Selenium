# x, y = map(int, input("Enter multiple values: ").split())
# print(type(x),type(y))
# print(f"so x = {int(x)} , y = {int(y)}")
# x , y = y, x
# print(x, y)
z = [[i*j for i in range(5)] for j in range (5)]
print(z)
word = " hello you are piece of shit "
print(len(word))
x = {char: word.count(char) for char in set(word)}
print(x)
name = ["Tim", "Jack","Schooby","Lance"]
age = [21, 18,23,44]
color = ["black","white","yellow","brown"]
print(list(zip(name,age,color)))
for name, age in zip(name,age):
    if age >= 23:
        print(name)