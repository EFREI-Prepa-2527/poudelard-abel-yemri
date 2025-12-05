def demander_texte(message):
    while True:
        texte = input(message).strip()
        if texte:
            return texte
        else:
            print("Invalide, veuillez entrer un texte non vide.")

def demander_nombre(message, min_val=None, max_val=None):
    while True:
        saisir = input(message)
        try:
            saisir = int(saisir)
            if (min_val is None or saisir>=min_val) and (max_val is None or saisir<= max_val):
                return saisir
            else:
                print("Le nombre doit être compris entre ", min_val, " et ", max_val, ".")
        except:
            print("Veuillez entrer un entier")
