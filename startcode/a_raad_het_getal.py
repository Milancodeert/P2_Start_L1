import random
def is_geheim_getal(gok, geheim_nummer):
    if gok == geheim_nummer:
        print("Correct")
        return True
    else:
        print("Fout")
        return False


def raad_het_getal(bovengrens):
    geheim_nummer = random.randint(1,bovengrens)
    einde_spel = False
    while not einde_spel:
        gok = int(input("geef een getal "))
        geraden = is_geheim_getal(gok, geheim_nummer)
        if geraden == True:
            einde_spel = True

raad_het_getal()



# Schrijf een functie raad_het_getal, die op basis van een bovengrens het raadspel zal spelen.
