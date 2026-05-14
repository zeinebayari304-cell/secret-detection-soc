# Rapport d’incident SOC

## Incident
Exposition de secrets dans un dépôt GitHub.

## Gravité
CRITICAL

## Source de détection
GitHub Actions + GitLeaks

## Description
Lors d’un push vers GitHub, le pipeline de sécurité a détecté la présence de secrets dans le code source.

Les secrets détectés peuvent inclure :
- une clé AWS,
- un mot de passe de base de données,
- une clé API.

## Impact potentiel
Si ces secrets étaient réels, un attaquant pourrait :
- accéder à des services cloud,
- se connecter à une base de données,
- voler des données sensibles,
- utiliser les ressources de l’entreprise.

## Réponse SOC
Le système a :
- détecté le secret,
- généré une alerte,
- bloqué le pipeline,
- demandé une correction du code.

## Correction appliquée
Les secrets ont été supprimés du fichier `config.py` et remplacés par des références à des variables d’environnement.

## Recommandations
- Ne jamais stocker de secrets dans le code.
- Utiliser GitHub Secrets.
- Utiliser des variables d’environnement.
- Scanner automatiquement chaque push.
- Former les développeurs aux bonnes pratiques DevSecOps. 