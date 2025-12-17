def initialiser_personnage(nom, prenom, attributs):
    joueur = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortilèges": [],
        "Attributs": attributs
    }
    return joueur
def afficher_personnage(joueur):
    print("Profil du personnage :")
    for cle, valeur in joueur.items():
        if type(valeur)  == dict:
            print("{} :".format(cle))
            for sous_cle, sous_valeur in valeur.items():
                print("- {} : {}".format(sous_cle, sous_valeur))
        elif type(valeur) == list:
            liste_en_texte = []
            for element in valeur:
                liste_en_texte.append(str(element))
            contenu = ", ".join(liste_en_texte)
            print("{} : {}".format(cle, contenu))
        else:
            print("{} : {}".format(cle, valeur))
def modifier_argent(joueur, montant):
    joueur["Argent"] = joueur["Argent"] + montant
    return joueur["Argent"]
def ajouter_objet(joueur, cle, objet):
    if cle in joueur:
        joueur[cle].append(objet)
    return joueur
