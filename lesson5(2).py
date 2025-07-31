a=str(input("Введите слово "))
letter = ["a","e","i","o","u"]
sogl=0
glas=0
letter_a=0
letter_e=0
letter_i=0
letter_o=0
letter_u=0
for j in range(len(a)):
    if a[j] == "a":
        letter_a+=1
        glas+=1
    elif a[j] == "e":
        letter_e+=1
        glas+=1
    elif a[j] == "i":
        letter_i+=1
        glas+=1
    elif a[j] == "o":
        letter_o+=1
        glas+=1
    elif a[j] == "u":
        letter_u+=1
        glas+=1
    else:
        sogl+=1
print ("Глассных = ", glas, "Согласных = ", sogl)
if letter_a != 0 and letter_e != 0 and letter_i != 0 and letter_o != 0 and letter_u != 0 :
    print ("Букв a =", letter_a, "Букв e =", letter_e, "Букв i =", letter_i, "Букв o =", letter_o, "Букв u =", letter_u )
else:
    print ("False")