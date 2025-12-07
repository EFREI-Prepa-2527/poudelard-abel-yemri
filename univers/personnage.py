def initialiser_personnage(nom, prenom, attributs):
    personnage = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortilèges": [],
        "Attributs": attributs
    }
    return personnage
def afficher_personnage(joueur):
    print("Profil du personnage :")

    for cle, valeur in joueur.items():
        #cas 1 : là yem c'est pr voir si c'est un dictionnaire en gros
        if type(valeur)  == dict:
            print("{} :".format(cle))
            for sous_cle, sous_valeur in valeur.items():
                print("- {} : {}".format(sous_cle, sous_valeur))
        #cas 2 : là pr voir si c'est une liste
        elif type(valeur) == list:
            liste_en_texte = []
            for element in valeur:
                liste_en_texte.append(str(element))
            contenu = ", ".join(liste_en_texte)
            print("{} : {}".format(cle, contenu))
        #et là si c'est aucun des deux genre un texte ou un nombre comme pr le nom ou l'argent
        else:
            print("{} : {}".format(cle, valeur))

def modifier_argent(joueur, montant):





