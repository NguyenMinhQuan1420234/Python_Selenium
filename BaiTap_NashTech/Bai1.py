#Xay dung tam giac so
# start 2, delta = 3, rows = 5 | start = 221, delta = 2, rows = 4
# 2                                 # 5
# 5 8                               # 7 9
# 2 5 8                             # 2 4 6
# 2 5 8 2                           # 8 1 3 5
# 5 8 2 5 8                         #

start = int(input("Nhap start: "))
delta = int(input("Nhap bien so: "))
rows = int(input("Nhap so hang: "))

list = []
digit = 0
sum = 0



for i in range ( 0, rows) :
    for j in range ( i+1 ):
        if start < 10:
            print(start, end= ' ')
            start+=delta
        else:
            while start > 0 or sum >= 10: # xu ly so >= 10
                digit = start % 10
                sum+=digit
                start = int(start / 10)
                if sum >= 10:
                    start = sum
                    sum = 0
            print(sum, end= ' ')
            start = sum + delta
            sum = 0
        
    print('')

# print(*list)







# for i in range(0,rows):
#     if start < 10:
#         list.append(start)
#         start = start + delta
#         print(*list)
#     if start >= 10:
#         while start >= 1:
#             sodu = int(start % 10)
#             start = int(start / 10)
#             total = total + sodu
#         start = total 
#         list.append(start)
#         start = start + delta 
#         print(*list)

# So = 56
# sum = int(So %10)
# So = int(So/10)
# print(sum , ' ' , So)
# sum = sum + So%10
# print(sum)