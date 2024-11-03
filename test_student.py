import pytest

# Assurez-vous que les classes Eleve et NoteInvalide sont définies avant ce code.

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

@pytest.mark.parametrize("notes,expected_moyenne", [
    ([10, 15, 20], (10 + 15 + 20) / 3),  # Test avec plusieurs notes
    ([5, 10, 15], (5 + 10 + 15) / 3),    # Autre test avec plusieurs notes
])
def test_moyenne_apres_plusieurs_notes(eleve, notes, expected_moyenne):
    """Test la moyenne après l'ajout de plusieurs notes."""
    for note in notes:
        eleve.ajouter_note(note)
    assert eleve.moyenne == expected_moyenne

@pytest.mark.parametrize("note", [18, 12, 0])  # Tests avec différentes notes valides
def test_ajouter_une_seule_note(eleve, note):
    """Test l'ajout d'une seule note."""
    eleve.ajouter_note(note)
    assert eleve.moyenne == note

if __name__ == "__main__":
    pytest.main()
