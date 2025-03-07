"""Module de gestion des élèves et de leurs notes.

Ce module contient la classe Eleve, 
qui permet de gérer les notes des élèves et de calculer leurs moyennes. 
Il lève une exception NoteInvalide si une 
note donnée est en dehors de la plage valide (0-20).
"""

class NoteInvalide(Exception):
    """Exception levée lorsqu'une note est invalide (hors plage 0-20)."""
    # Aucune logique nécessaire ici, la classe hérite de Exception

class Eleve:
    """Représente un élève et gère ses notes."""

    def __init__(self):
        """Initialise un nouvel élève avec une liste
        de notes vide et une moyenne de 0."""
        self.notes = []
        self.moyenne = 0.0

    def ajouter_note(self, note):
        """Ajoute une note à l'élève et met à jour la moyenne.

        Args:
            note (float): La note à ajouter, doit être comprise entre 0 et 20.

        Raises:
            NoteInvalide: Si la note est inférieure à 0 ou supérieure à 20.
        """
        if not 0 <= note <= 20:
            raise NoteInvalide("La note doit être entre 0 et 20.")

        self.notes.append(note)
        self.moyenne = sum(self.notes) / len(self.notes)

    def obtenir_moyenne(self):
        """Retourne la moyenne des notes de l'élève."""
        return self.moyenne
