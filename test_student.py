import pytest

@pytest.fixture
def eleve():
    """Fixture pour créer une instance d'Eleve pour les tests."""
    return Eleve()

def test_ajouter_note_valide(eleve):
    """Test l'ajout d'une note valide."""
    eleve.ajouter_note(15)
    assert eleve.notes == [15]
    assert eleve.moyenne == 15

    eleve.ajouter_note(10)
    assert eleve.notes == [15, 10]
    assert eleve.moyenne == 12.5

def test_ajouter_note_invalide(eleve):
    """Test l'ajout d'une note invalide."""
    with pytest.raises(NoteInvalide, match="La note doit être entre 0 et 20."):
        eleve.ajouter_note(25)

    with pytest.raises(NoteInvalide, match="La note doit être entre 0 et 20."):
        eleve.ajouter_note(-1)

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