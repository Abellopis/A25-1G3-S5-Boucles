from sys import float_repr_style


def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)

    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """

    alerte = False

    # Vérification température
    if temp < 18:
        print("Température trop basse")
        alerte = True
    elif temp > 27:
        print("Température trop élevée")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        print("Humidité basse")
        alerte = True
    elif humidite >= 50:
        print("Humidité trop élevée")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        print("Trop de poussière")
        alerte = True

    # Retour final
    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"


if __name__ == "__main__":
    #TODO : Créer 3 listes
    liste_ordi1 = ["1", "2", "3"]
    liste_ordi2 = []
    liste_ordi3 = []

    #TODO : pour 3 ordinateurs
        #TODO : Demander temp, poussiere, humidite
        #TODO : Mettre 3 valeurs dans leurs listes
    temp = float(input("Entrer la température : "))
    poussiere = input("Enter le niveau de poussière : ")
    humidite = float(input("Entrer l'humidité : "))

    liste_ordi1.append(temp)
    liste_ordi2.append(poussiere)
    liste_ordi3.append(humidite)


    #TODO : Pour les 3 ordis
        #TODO : utiliser la fonction et afficher le résultat
    print(environnement_optimal(temp, poussiere, humidite))

