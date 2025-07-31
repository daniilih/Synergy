mininv= int(input("Минимальная сумма инвестиций "))
Mike=int(input("У Майкла "))
Ivan=int(input("У Ивана "))
if Mike >= mininv and Ivan >= mininv:
    print("2")
elif (Mike >= mininv and Ivan < mininv):
    print ("Mike")
elif (Mike < mininv and Ivan>=mininv):
    print ("Ivan")
elif (Mike + Ivan >= mininv):
    print ("1")
else:
    print ("0")