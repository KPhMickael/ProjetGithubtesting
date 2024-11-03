class NoteInvalide(Exception):
    # Exception personnalisée pour signaler qu'une note est invalide
    pass


class Eleve:
    def __init__(self):
        # Initialise une liste vide pour stocker les notes de l'élève
        self.notes = []
        # Initialise la moyenne à 0, qui sera calculée après l'ajout de notes
        self.moyenne = 0

    def ajouter_note(self, note):
        # Vérifie que la note est entre 0 et 20 ; si non, lève une exception
        if note < 0 or note > 20:
            raise NoteInvalide("La note doit être entre 0 et 20.")

        # Ajoute la note validée à la liste des notes de l'élève
        self.notes.append(note)
        
        # Calcule la moyenne actuelle en fonction de toutes les notes ajoutées
        self.moyenne = sum(self.notes) / len(self.notes)
