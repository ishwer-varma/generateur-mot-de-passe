import random
import string

# Fonction pour générer un mot de passe
def generer_mdp(longueur=12, majuscule=True, minuscule=True, chiffre=True, caractere_special=True):
    # Vérification si la longueur est inférieure à 4, dans ce cas, une exception est levée
    if longueur < 4:
        raise ValueError("La longueur du mot de passe doit être d'au moins 4 caractères.")
    
    # Initialisation de l'ensemble des caractères qui seront utilisés dans le mot de passe
    ensemble_caracteres = ''
    
    # Si l'option majuscule est activée, on ajoute les lettres majuscules à l'ensemble des caractères
    if majuscule:
        ensemble_caracteres += string.ascii_uppercase
    
    # Si l'option minuscule est activée, on ajoute les lettres minuscules à l'ensemble des caractères
    if minuscule:
        ensemble_caracteres += string.ascii_lowercase
    
    # Si l'option chiffre est activée, on ajoute les chiffres (0-9) à l'ensemble des caractères
    if chiffre:
        ensemble_caracteres += string.digits
    
    # Si l'option caractère spécial est activée, on ajoute les symboles spéciaux (comme !, ?, $, etc.) à l'ensemble des caractères
    if caractere_special:
        ensemble_caracteres += string.punctuation

    # Si aucun type de caractère n'est sélectionné, une exception est levée
    if not ensemble_caracteres:
        raise ValueError("Au moins un type de caractère doit être sélectionné.")
    
    # Génération du mot de passe en sélectionnant aléatoirement des caractères dans l'ensemble
    mot_de_passe = ''.join(random.choice(ensemble_caracteres) for _ in range(longueur))
    
    # Retourner le mot de passe généré
    return mot_de_passe

# Exécution principale du script
if __name__ == "__main__":
    # Appel de la fonction pour générer un mot de passe de 12 caractères avec tous les types de caractères activés
    mot_de_passe = generer_mdp(longueur=12, majuscule=True, minuscule=True, chiffre=True, caractere_special=True)
    
    # Affichage du mot de passe généré
    print("Mot de passe généré :", mot_de_passe)
