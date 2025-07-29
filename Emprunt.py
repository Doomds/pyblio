class Emprunt:
    def __init__(self, date_pret, id_abonne, date_retour_prevue, date_retour_reelle, duree_pret_reelle):
        self.date_pret = date_pret
        self.id_abonne = id_abonne
        self.date_retour_prevue = date_retour_prevue
        self.date_retour_reelle = date_retour_reelle
        self.duree_pret_reelle = duree_pret_reelle