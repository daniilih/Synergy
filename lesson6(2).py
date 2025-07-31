a=int(input("Введите число "))
decim=0
for i in range (1,a+1):
    if a % i == 0:
        decim+=1
print (decim)