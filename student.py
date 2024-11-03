class NoteInvalide(Exception):
    """Exception levée lorsque la note n'est pas valide (hors des limites de 0 à 20)."""
    pass


class Eleve:
    """Classe représentant un élève avec une liste de notes et une moyenne calculée."""

    def __init__(self):
        """Initialise un élève sans note et une moyenne de 0."""
        self.notes = []
        self.moyenne = 0

    def ajouter_note(self, note):
        """
        Ajoute une note à la liste des notes de l'élève si elle est valide
        (entre 0 et 20), et met à jour la moyenne.

        Parameters:
        note (float) : La note à ajouter.

        Raises:
        NoteInvalide : Si la note est hors des limites de 0 à 20.
        """
        # Vérifie si la note est dans la plage autorisée
        if note < 0 or note > 20:
            raise NoteInvalide("La note doit être entre 0 et 20.")

        # Ajoute la note et recalcule la moyenne
        self.notes.append(note)
        self.moyenne = sum(self.notes) / len(self.notes)

