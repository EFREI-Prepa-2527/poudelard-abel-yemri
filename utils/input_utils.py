def demander_texte(message):
    while True:
        texte = input(message).strip()
        if texte:
            return texte
        else:
            print("Invalide, veuillez entrer un texte non vide.")
def demander_nombre(message, min_val=None, max_val=None):
    while True:
        texte = input(message)

        if len(texte) == 0:
            print("Veuillez entrer un nombre.")
            continue

        negatif = False
        if texte[0] == '-':
            negatif = True
            texte_sans_signe = texte[1:]
        else:
            texte_sans_signe = texte

        est_entier = True
        for c in texte_sans_signe:
            if c < '0' or c > '9':
                est_entier = False
                break

        if not est_entier or texte_sans_signe == "":
            print("Veuillez rentrer un nombre entier valide")
            continue

        nombre = 0
        for c in texte_sans_signe:
            nombre = nombre * 10 + (ord(c) - ord('0'))

        if negatif:
            nombre = -nombre

        if (min_val is not None and min_val > nombre) or (max_val is not None and max_val < nombre):
            print("Veuillez rentrer un nombre compris entre ", min_val, " et ", max_val, ".")
            continue

        return nombre
def demander_choix(message, options):
    for i in range(len(options)):
        print(i+1, ". ", options[i], sep ="")

    choix = demander_nombre(message, 1, len(options))

    return options[choix - 1]







