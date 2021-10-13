tafel = int(input("Welke tafel wilt u weten. (1/10)"))

def de_tafels(tafel:int):
    for a in range(1,11):
        print(a,"x",tafel,"=",a*tafel)

de_tafels(tafel)
