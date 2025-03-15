import random

lootMiseA = [100,20,5,4,3,2,1,0,0,0]
lootMiseB = []
lootMiseC = []
choixRamdom = random.randint(0,9)


choix_de_la_mise = int(input("Combien voulez vous miser ? (1 PO, 10 PO, 100 PO) "))

print("")
print(f"vous avez misé {choix_de_la_mise} PO")
print("")

if choix_de_la_mise == 1:
    if choixRamdom != 9:
        while choixRamdom != lootMiseA[7] or choixRamdom != lootMiseA[8]:
            gain = lootMiseA[choixRamdom]
            print(gain)
            choixRamdom = random.randint(0,8)

    else: 
        print("Perdu ! veux tu rejouer ?")


elif choix_de_la_mise == 10:
    print ("Vous avez misé 10")

else:
    print("Vous avez misé 100")