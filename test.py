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