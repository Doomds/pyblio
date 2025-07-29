class Abonne:
    def __init__(self, id, nom, prenom, adresse, tel, email, date_adhesion):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.tel = tel
        self.email = email
        self. date_adhesion = date_adhesion
    
    def __str__(self):
        return f"""ID: {self.id}
        \nNom: {self.nom}
        \nPrénom: {self.prenom}
        \nAdresse: {self.adresse}
        \nTel: {self.tel}
        \nEmail: {self.email}
        \nDate d'adhésion: {self.date_adhesion}
        \n=================================="""