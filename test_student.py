import pytest
from student import Eleve, NoteInvalide

def test_ajouter_note_valide():
    """Test l'ajout d'une note valide."""
    eleve = Eleve()
    eleve.ajouter_note(15.0)
    assert eleve.moyenne == 15.0  # Vérifie que la moyenne est correcte après l'ajout
    assert len(eleve.notes) == 1  # Vérifie qu'une note a bien été ajoutée

def test_ajouter_plusieurs_notes():
    """Test l'ajout de plusieurs notes et le calcul de la moyenne."""
    eleve = Eleve()
    eleve.ajouter_note(10.0)
    eleve.ajouter_note(12.0)
    eleve.ajouter_note(14.0)
    assert eleve.moyenne == 12.0  # Vérifie que la moyenne est correcte après plusieurs ajouts
    assert len(eleve.notes) == 3  # Vérifie que 3 notes ont été ajoutées

def test_ajouter_note_invalide_inférieure():
    """Test l'ajout d'une note invalide inférieure à 0."""
    eleve = Eleve()
    with pytest.raises(NoteInvalide):
        eleve.ajouter_note(-1.0)  # Doit lever une exception NoteInvalide

def test_ajouter_note_invalide_supérieure():
    """Test l'ajout d'une note invalide supérieure à 20."""
    eleve = Eleve()
    with pytest.raises(NoteInvalide):
        eleve.ajouter_note(21.0)  # Doit lever une exception NoteInvalide

def test_obtenir_moyenne_avant_ajout_de_notes():
    """Test la moyenne avant l'ajout de toute note."""
    eleve = Eleve()
    assert eleve.moyenne == 0.0  # La moyenne doit être 0.0 au début

