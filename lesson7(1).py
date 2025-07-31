a=str(input("Введите слово "))
b=0
for i in range (len(a)):
    if a[i] == a[-1-i]:
        pass
    else:
        b=1
if b==0:
    print("yes")
else:
    print("no")