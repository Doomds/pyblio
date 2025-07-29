class Livre:
    def __init__(self, isbn, date_achat, titre, auteur, editeur, categorie):
        self.isbn = isbn
        self.date_achat = date_achat
        self.titre = titre
        self.auteur = auteur
        self.editeur = editeur
        self.categorie = categorie
    
    def __str__(self):
        return f"""ISBN: {self.isbn}
        \nDate d'achat: {self.date_achat}
        \nTitre: {self.titre}
        \nAuteur: {self.auteur}
        \nEditeur: {self.editeur}
        \ncategorie: {self.categorie}
        \n=================================="""