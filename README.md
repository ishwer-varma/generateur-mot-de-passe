# Générateur de mots de passe sécurisé avec CI/CD

Ce projet Python permet de générer des mots de passe sécurisés en fonction de plusieurs critères (longueur, types de caractères).  
Il inclut des **tests automatisés** via `pytest` et une **intégration continue (CI/CD)** via GitHub Actions et GitLab CI.

---

## Fonctionnalités

- Génération de mots de passe aléatoires avec :
  - Longueur personnalisable
  - Lettres majuscules
  - Lettres minuscules
  - Chiffres
  - Caractères spéciaux
- Interface CLI (affiche un mot de passe généré si on exécute `password_generator.py`)
- Tests unitaires automatisés
- Intégration continue avec :
  - GitHub Actions (`.github/workflows/python-app.yml`)
  - GitLab CI (`.gitlab-ci.yml`)

---

## 🧪 Lancer le script principal

Pour générer un mot de passe sécurisé directement depuis le terminal, exécute le script Python avec la commande suivante :

```bash
python3 password_generator.py
```
## Lancer les tests

```bash
# Installer les dépendances
pip install -r requirements.txt

# Exécuter les tests
pytest