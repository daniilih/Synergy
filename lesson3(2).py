answer=["AUSTRALOPITHECUS", "HOMO HABILIS", "HOMO ERECTUS", "HOMO NEARDERTHALENSIS", "HOMO SAPIENS SAPIENS"]
studanswer=input("Первый этап развития человека ")
i=0
while studanswer == answer[i] and i<4:
    studanswer=input("Следующий этап развития человека ")
    i+=1
if i!=4:
    print ("Неверно")
    print (answer[0], answer[1], answer[2], answer[3], answer[4], sep="=>")
if i==4:
    print ("Верно")
    print (answer[0], answer[1], answer[2], answer[3], answer[4], sep="=>")

