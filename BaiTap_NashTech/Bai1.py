#Xay dung tam giac so
# start 2, delta = 3, rows = 5 | start = 221, delta = 2, rows = 4
# 2
# 2 5 
# 2 5 8
# 2 5 8 2
# 2 5 8 2 5

start = int(input("Nhap start: "))
delta = int(input("Nhap bien so: "))
rows = int(input("Nhap so hang: "))

list = []
sodu = 0
total = 0
start_sub = start

for i in range(0,rows):
    if start < 10:
        list.append(start)
        start = start + delta
        print(*list)
    if start >= 10:
        while start >= 1:
            sodu = int(start % 10)
            start = int(start / 10)
            total = total + sodu
        start = total 
        list.append(start)
        start = start + delta 
        print(*list)

# So = 56
# sum = int(So %10)
# So = int(So/10)
# print(sum , ' ' , So)
# sum = sum + So%10
# print(sum)