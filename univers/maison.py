def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] = maisons[nom_maison] + points
        print("Changement effectué. ", nom_maison, " a maintenant ", maisons[nom_maison], " points. ")
    else:
        print("La maison est introuvable.")
def afficher_maison_gagnante(maisons):
    points_max = 0
    maison_gagnante = []

    for points in maisons.values():
        if points > points_max:
            points_max = points

    for i in maisons:
        if maisons[i] == points_max:
            maison_gagnante.append(i)

    if len(maison_gagnante) >= 2 :
            print("Il y a plusieurs maisons gagantes : ",maison_gagnante, ".")
    else:
            print("Il y a une maison gagnante : ",maison_gagnante[0], ".")

    return maison_gagnante
def repartition_maison(joueur, questions):
    dico_maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    














    questions = {
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            ["Fonces sans hésiter", "Cherches la meilleure stratégie","Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    }
