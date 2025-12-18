from utils.input_utils import demander_choix
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
        "Gryffondor": joueur["Attributs"]["courage"]*2,
        "Serpentard": joueur["Attributs"]["ambition"]*2,
        "Poufsouffle": joueur["Attributs"]["loyauté"]*2,
        "Serdaigle": joueur["Attributs"]["intelligence"]*2
    }

    for question_actuelle in questions:
        texte_question = question_actuelle[0]
        choix_possibles = question_actuelle[1]
        maisons_associees = question_actuelle[2]

        choix = demander_choix(texte_question, options = choix_possibles)
        actualiser_points_maison(dico_maisons, maisons_associees[choix-1], 3)

    points_max = -1
    nom_maison_gagnante = ''

    print("Résumé des scores :")
    for nom_maison, score in dico_maisons.items():
        print("{} : {} points".format(nom_maison, score))
        if score > points_max:
            points_max = score
            nom_maison_gagnante = nom_maison

    return nom_maison_gagnante

