N=int(input("Введите кол-во чисел "))
zero=0
for i in range (N):
    a=int(input("Введите число "))
    if a == 0:
        zero+=1
print (zero)