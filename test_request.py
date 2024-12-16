import requests

# URL de base de l'API
url_base = 'http://127.0.0.1:8000'

# Test du endpoint d'accueil
response = requests.get(f"{url_base}/")
print("Réponse du endpoint d'accueil:", response.text)
# Données d'exemple pour la prédiction
donnees_predire = {
    "Credit_amount": 5000,
    "Age": 55,
    "Duration": 24,
    "Purpose": 2
   
}

# Test du endpoint de prédiction
response = requests.post(f"{url_base}/predict", json=donnees_predire)  # Removed the trailing slash
print("Réponse du endpoint de prédiction:", response.text)


