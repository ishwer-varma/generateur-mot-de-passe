# -*- coding: utf-8 -*-
import string
from password_generator import generer_mdp  # Importation de la fonction générer_mdp

# Test de la longueur du mot de passe généré
def test_longueur():
    # Génère un mot de passe de 16 caractères
    mot_de_passe = generer_mdp(longueur=16)
    # Vérifie que la longueur du mot de passe généré est bien de 16 caractères
    assert len(mot_de_passe) == 16

# Test de la présence de majuscules dans le mot de passe
def test_majuscules():
    # Génère un mot de passe de 20 caractères avec uniquement des majuscules
    mot_de_passe = generer_mdp(longueur=20, majuscule=True, minuscule=False, chiffre=False, caractere_special=False)
    # Vérifie qu'au moins un caractère du mot de passe est une majuscule
    assert any(c in string.ascii_uppercase for c in mot_de_passe)

# Test de la présence de minuscules dans le mot de passe
def test_minuscules():
    # Génère un mot de passe de 20 caractères avec uniquement des minuscules
    mot_de_passe = generer_mdp(longueur=20, majuscule=False, minuscule=True, chiffre=False, caractere_special=False)
    # Vérifie qu'au moins un caractère du mot de passe est une minuscule
    assert any(c in string.ascii_lowercase for c in mot_de_passe)

# Test de la présence de chiffres dans le mot de passe
def test_chiffres():
    # Génère un mot de passe de 20 caractères avec uniquement des chiffres
    mot_de_passe = generer_mdp(longueur=20, majuscule=False, minuscule=False, chiffre=True, caractere_special=False)
    # Vérifie qu'au moins un caractère du mot de passe est un chiffre
    assert any(c in string.digits for c in mot_de_passe)

# Test de la présence de caractères spéciaux dans le mot de passe
def test_caracteres_speciaux():
    # Génère un mot de passe de 20 caractères avec uniquement des caractères spéciaux
    mot_de_passe = generer_mdp(longueur=20, majuscule=False, minuscule=False, chiffre=False, caractere_special=True)
    # Vérifie qu'au moins un caractère du mot de passe est un caractère spécial
    assert any(c in string.punctuation for c in mot_de_passe)

# Test de la longueur invalide du mot de passe (doit lever une erreur)
def test_longueur_invalide():
    try:
        # Essaye de générer un mot de passe avec une longueur de 2, ce qui est trop court
        generer_mdp(longueur=2)
        # Si aucune exception n'est levée, échoue le test
        assert False, "Erreur attendue : longueur trop courte"
    except ValueError:
        # Si une exception de type ValueError est levée, le test passe
        assert True

# Test de l'absence de sélection de type de caractère (doit lever une erreur)
def test_aucun_type_selectionne():
    try:
        # Essaye de générer un mot de passe sans aucun type de caractère sélectionné
        generer_mdp(longueur=10, majuscule=False, minuscule=False, chiffre=False, caractere_special=False)
        # Si aucune exception n'est levée, échoue le test
        assert False, "Erreur attendue : aucun type de caractère sélectionné"
    except ValueError:
        # Si une exception de type ValueError est levée, le test passe
        assert True
