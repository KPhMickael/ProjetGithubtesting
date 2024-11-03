class NoteInvalide(Exception):
    """Exception levée lorsque la note fournie est invalide."""
    pass

class Eleve:
    """Classe pour gérer les notes d'un élève."""
    
    def __init__(self):
        """Initialise une liste vide pour stocker les notes et la moyenne."""
        self.notes = []
        self.moyenne = 0

    def ajouter_note(self, note):
        """Ajoute une note à l'élève et met à jour la moyenne.

        Args:
            note (float): La note à ajouter. Doit être entre 0 et 20.

        Raises:
            NoteInvalide: Si la note est en dehors de l'intervalle autorisé.
        """
        if note < 0 or note > 20:
            raise NoteInvalide("La note doit être entre 0 et 20.")
        self.notes.append(note)
        self.moyenne = sum(self.notes) / len(self.notes)


import pytest

@pytest.fixture
def eleve():
    """Fixture pour créer une instance d'Eleve pour les tests."""
    return Eleve()

@pytest.mark.parametrize("note,expected_moyenne", [
    (15, 15),
    (10, 12.5),  # Après l'ajout de 15 puis 10
])
def test_ajouter_note_valide(eleve, note, expected_moyenne):
    """Test l'ajout de notes valides et vérifie la moyenne."""
    eleve.ajouter_note(15)  # Ajout initial
    eleve.ajouter_note(note)  # Ajout de la note paramétrée
    assert eleve.notes == [15, note]
    assert eleve.moyenne == expected_moyenne

@pytest.mark.parametrize("note", [25, -1])  # Notes invalides à tester
def test_ajouter_note_invalide(eleve, note):
    """Test l'ajout d'une note invalide."""
    with pytest.raises(NoteInvalide, match="La note doit être entre 0 et 20."):
        eleve.ajouter_note(note)

def test_moyenne_apres_plusieurs_notes(eleve):
    """Test la moyenne après l'ajout de plusieurs notes."""
    eleve.ajouter_note(10)
    eleve.ajouter_note(15)
    eleve.ajouter_note(20)
    assert eleve.moyenne == (10 + 15 + 20) / 3

def test_ajouter_une_seule_note(eleve):
    """Test l'ajout d'une seule note."""
    eleve.ajouter_note(18)
    assert eleve.moyenne == 18

if __name__ == "__main__":
    pytest.main()
