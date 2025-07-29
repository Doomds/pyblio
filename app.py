from Livre import Livre
from Emprunt import Emprunt
from Abonne import Abonne

livre1 = Livre("9782075100649", "29/7/2025", "Le sorcier de la montagne de feu", "Steve Jackson & Ian Livingstone", "Gallimard Jeunesse", "Défis fantastiques")

print(livre1)

emprunt1 = Emprunt("01/08/2025", "1", "15/08/2025", None, None)

print(emprunt1)

abonne1 = Abonne("1", "Doe", "John", "Rue de la trouille 62", "0478/68.95.44", "john.doe@trouille.com", "01/06/2025")

print(abonne1)