from abc import abstractproperty


def naam_leeftijd():
    naam = 'a'
    leeftijd = 'b'
    while naam != 'stop' and leeftijd != "stop":
        naam = input("wat is je naam?: ")
        if naam == 'stop':
            break
        leeftijd = input("wat is je leeftijd?: ")
        if leeftijd == 'stop':
            break
        print("Hallo",naam,",je leeftijd is", leeftijd,"jaar")
naam_leeftijd()