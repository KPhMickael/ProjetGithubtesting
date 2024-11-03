class NoteInvalide(Exception):
    pass

class Eleve:
    def __init__(self):
        self.notes=[]
        self.moyenne=0

    def ajouter_note(self,note):
        if note<0 or note>20: 
            raise NoteInvalide("La note doit être entre 0 et 20.")
        self.notes.append(note)
        self.moyenne=sum(self.notes)/len(self.notes)

