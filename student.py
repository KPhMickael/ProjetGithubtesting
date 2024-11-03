class NoteInvalide(Exception):
    pass


class Eleve:


    def __init__(self):
        self.notes = []
        self.moyenne = 0

    def ajouter_note(self, note):
        # Vérifie si la note est dans la plage autorisée
        if note < 0 or note > 20:
            raise NoteInvalide("La note doit être entre 0 et 20.")

        # Ajoute la note et recalcule la moyenne
        self.notes.append(note)
        self.moyenne = sum(self.notes) / len(self.notes)

