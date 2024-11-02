class Eleve:
    def __init__(self):
        self.notes = []  # Liste pour stocker les notes
        self.moyenne = 0  # La moyenne commence à 0

    def ajouter_note(self, note):
        # Vérifie que la note est entre 0 et 20
        if note < 0 or note > 20:
            raise NoteInvalide("La note doit être entre 0 et 20.")
        
        # Ajoute la note et met à jour la moyenne
        self.notes.append(note)
        self.moyenne = sum(self.notes) / len(self.notes)

class NoteInvalide(Exception):
    pass  # Exception si la note n'est pas valide
