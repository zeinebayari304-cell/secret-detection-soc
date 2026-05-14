# Détection des secrets exposés dans un projet GitHub avec alerte SOC

## Objectif
Ce projet met en place une solution DevSecOps permettant de détecter automatiquement les secrets exposés dans un dépôt GitHub.

Un secret peut être :
- un mot de passe,
- une clé API,
- une clé AWS,
- un token GitHub.

Lorsqu’un secret est détecté, le pipeline GitHub Actions échoue et une alerte SOC est générée.

## Architecture

```text
Développeur
   ↓
Push GitHub
   ↓
GitHub Actions
   ↓
GitLeaks Scan
   ↓
Secret détecté ?
   ↓
Oui → Alerte SOC + Pipeline bloqué
Non → Pipeline validé
   ↓
Dashboard SOC 