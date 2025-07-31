a=int(input("Введите число "))
if a>0:
    first="Положительное"
else:
    first="Отрицательное"
if a%2==0:
    second="четное"
else:
    second="нечетное"
if a==0:
    print ("Нулевое число")
else:
    print (first+ " " + second  + " число")