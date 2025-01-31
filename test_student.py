"""Tests unitaires pour la classe Eleve."""

import pytest
from student import Eleve, NoteInvalide

@pytest.fixture
def eleve():
    """Fixture pour créer une instance d'Eleve pour les tests."""
    return Eleve()

@pytest.mark.parametrize("note", [0, 10, 20])
def test_ajouter_une_seule_note(eleve, note):
    """Test l'ajout d'une seule note valide et la mise à jour correcte de la moyenne."""
    eleve.ajouter_note(note)
    assert eleve.notes == [note]
    assert eleve.moyenne == note

@pytest.mark.parametrize("notes, expected_moyenne", [
    ([10, 15, 20], 15),
    ([5, 10, 15], 10),
])
def test_moyenne_apres_plusieurs_notes(eleve, notes, expected_moyenne):
    """Test la moyenne après l'ajout de plusieurs notes."""
    for note in notes:
        eleve.ajouter_note(note)
    assert eleve.moyenne == expected_moyenne

@pytest.mark.parametrize("note", [25, -1, 30, -5])
def test_ajouter_note_invalide(eleve, note):
    """Test l'ajout d'une note invalide."""
    with pytest.raises(NoteInvalide, match="La note doit être entre 0 et 20."):
        eleve.ajouter_note(note)
