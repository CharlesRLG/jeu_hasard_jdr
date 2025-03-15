import random

lootMiseA = [10,20,50,0,3,0,0,0,0,0]
lootMiseB = [1000,200,30,1,1,1,1,0,0,1]
lootMiseC = [10000,1,1000,1,500,1,1,0,0,1]
choixRamdom = random.randint(0,9)
gains = []

def sommeGain (listeGain):
    _sommeGain = 0
    for i in listeGain:
        _sommeGain = _sommeGain + i
    return _sommeGain

print("")
choix_de_la_mise = int(input("Combien voulez vous miser ? (1 PO, 10 PO, 100 PO) "))

print("")
print(f"vous avez misé {choix_de_la_mise} PO")
print("")

if choix_de_la_mise == 1:
    if choixRamdom != 9:
        while choixRamdom != lootMiseA[7]:
            gain = lootMiseA[choixRamdom]
            choixRamdom = random.randint(0,8)
            gains.append(gain)
            
    else: 
        print("Perdu ! Voulez-vous rejouer ?")
        
    print(f"Nombre de relance avant l'arret du jeu : {len(gains)}")
    print(f"Totale des gains en PA : {sommeGain(gains)}")
    sommeTotale = sommeGain(gains)
    pieceOr = (sommeTotale / 20)
    pieceArgent = sommeTotale % 20
    print("")
    print("Vous avez gagnez:")
    print("- {0:6.0f}".format(pieceOr) + " Pièce d'Or")
    print("- {0:6.0f}".format(pieceArgent) + " Pièce d'Argent")
    print("")
    print("Voulez-vous rejouer ?")

elif choix_de_la_mise == 10:
    if choixRamdom != 9:
        while choixRamdom != lootMiseB[7] or choixRamdom != lootMiseB[8]:
            gain = lootMiseB[choixRamdom]
            choixRamdom = random.randint(0,8)
            gains.append(gain)
            
    else: 
        print("Perdu ! Voulez-vous rejouer ?")

    print(f"Nombre de relance avant l'arret du jeu : {len(gains)}")
    print(f"Totale des gains en PA : {sommeGain(gains)}")
    sommeTotale = sommeGain(gains)
    pieceOr = (sommeTotale / 20)
    pieceArgent = sommeTotale % 20
    print("")
    print("Vous avez gagnez:")
    print("- {0:6.0f}".format(pieceOr) + " Pièce d'Or")
    print("- {0:6.0f}".format(pieceArgent) + " Pièce d'Argent")
    print("")
    print("Voulez-vous rejouer ?")

else:
    if choixRamdom != 9:
        while choixRamdom != lootMiseC[7] or choixRamdom != lootMiseC[8]:
            gain = lootMiseC[choixRamdom]
            choixRamdom = random.randint(0,8)
            gains.append(gain)
            
    else: 
        print("Perdu ! Voulez-vous rejouer ?")

    print(f"Nombre de relance avant l'arret du jeu : {len(gains)}")
    print(f"Totale des gains en PA : {sommeGain(gains)}")
    sommeTotale = sommeGain(gains)
    pieceOr = (sommeTotale / 20)
    pieceArgent = sommeTotale % 20
    print("")
    print("Vous avez gagnez:")
    print("- {0:6.0f}".format(pieceOr) + " Pièce d'Or")
    print("- {0:6.0f}".format(pieceArgent) + " Pièce d'Argent")
    print("")
    print("Voulez-vous rejouer ?")