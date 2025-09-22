import pytest # importer le module pytest pour faire nos test unitaires
from ExDebug1 import environnement_optimal # importer la fonction dans un autre fichier

# test unitaire pour la fonction test_environnement_optimal
def test_environnement_optimal():
    #Arrange # préparer des variables d'entrées et le résulat attendu
    temprature = 30
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Environnement non optimal"

    #Act # Appeler la fonction à tester
    resultat_obtenu = environnement_optimal(temprature,poussiere,humidite)

    #Assert # Vérifier le résultat
    assert resultat_attendu == resultat_obtenu
