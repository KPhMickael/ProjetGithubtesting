class NoteInvalide(Exception):
    """Exception levée lorsque la note fournie est invalide."""
    pass


class Eleve:
    """Représente un élève et gère ses notes.

    Attributes:
        notes (list): Une liste des notes de l'élève.
        moyenne (float): La moyenne des notes de l'élève.
    """
    def __init__(self):
        """Initialise un nouvel élève avec une liste de notes vide et une moyenne de 0."""
        self.notes = []
        self.moyenne = 0

    def ajouter_note(self, note):
        """Ajoute une note à l'élève et met à jour la moyenne.

        Args:
            note (float): La note à ajouter, doit être comprise entre 0 et 20.

        Raises:
            NoteInvalide: Si la note est inférieure à 0 ou supérieure à 20.
        """
        if note < 0 or note > 20:
            raise NoteInvalide("La note doit être entre 0 et 20.")
        self.notes.append(note)
        self.moyenne = sum(self.notes) / len(self.notes)

