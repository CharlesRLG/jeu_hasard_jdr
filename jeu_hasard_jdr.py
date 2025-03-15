import random

lootMiseA = [100,20,50,-4,3,0,-1,0,0,-5]
lootMiseB = []
lootMiseC = []
choixRamdom = random.randint(0,9)
gains = []

def sommeGain (listeGain):
    _sommeGain = 0
    for i in listeGain:
        _sommeGain = _sommeGain + i
    return _sommeGain

choix_de_la_mise = int(input("Combien voulez vous miser ? (1 PO, 10 PO, 100 PO) "))

print("")
print(f"vous avez misé {choix_de_la_mise} PO")
print("")

if choix_de_la_mise == 1:
    if choixRamdom != 9:
        while choixRamdom != lootMiseA[7] or choixRamdom != lootMiseA[8]:
            gain = lootMiseA[choixRamdom]
            choixRamdom = random.randint(0,8)
            gains.append(gain)
            
    else: 
        print("Perdu ! veux tu rejouer ?")
    #print(len(gains))
    #print (sommeGain(gains))
    sommeTotale = sommeGain(gains)
    pieceOr = (sommeTotale / 20)
    pieceArgent = sommeTotale % 20

    print("Vous avez gagnez:")
    print("- {0:6.0f}".format(pieceOr) + " Pièce d'Or")
    print("- {0:6.0f}".format(pieceArgent) + " Pièce d'Argent")
    print("")
    print("Voulez-vous rejouer ?")

elif choix_de_la_mise == 10:
    print ("Vous avez misé 10")

else:
    print("Vous avez misé 100")