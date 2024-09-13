# Convertisseur Binaire et Hexadécimal

## Description

Ce script Python a été réaliser dans le but d'apprendre les conversions entre différents systèmes de numérotation (binaire et hexadécimal) afin de mieux comprendre les concepts de **reverse engineering** et de **langage d'assemblage (ASM)**. Il permet de convertir un ou plusieurs caractères en leurs représentations **binaire** et **hexadécimale**, tout en expliquant les étapes détaillées de chaque conversion.

## Fonctionnalités

- Conversion d'un caractère en :
  - Code ASCII (décimal)
  - Binaire
  - Hexadécimal
- Explication détaillée des étapes de conversion
- Prise en charge des caractères ASCII standards et étendus
- Affichage clair et lisible des étapes de calcul

## Objectif

Ce script a été réalisé dans le cadre de mon apprentissage du **reverse engineering** et du **langage d'assemblage**.

## Utilisation

### Prérequis

Assurez-vous d'avoir Python 3 installé sur votre machine.

### Lancer le script

1. Clonez ou téléchargez ce projet.
2. Exécutez le script `binhex-learn.py` avec Python :

   ```bash
   python bi-he.py
   ```

3. Entrez un mot ou une lettre lorsque vous y êtes invité, et le script affichera les étapes de conversion pour chaque caractère.

### Exemple de sortie

Si vous entrez la lettre `a`, vous obtiendrez une sortie similaire à celle-ci :

```
=== Convertisseur Binaire et Hexadécimal ===
Entrez un mot ou une lettre : a

==================================================
Caractère                : 'a'
Code ASCII décimal       : 97
==================================================

Conversion en binaire :
Le nombre binaire est 1100001
  1 ÷  2 =   0 avec un reste de 1
  3 ÷  2 =   1 avec un reste de 1
  6 ÷  2 =   3 avec un reste de 0
 12 ÷  2 =   6 avec un reste de 0
 24 ÷  2 =  12 avec un reste de 0
 48 ÷  2 =  24 avec un reste de 0
 97 ÷  2 =  48 avec un reste de 1

Représentation binaire sur 8 bits : 01100001

Conversion en hexadécimal :
Le nombre hexadécimal est 61
  6 ÷ 16 =   0 avec un reste de  6 (6)
 97 ÷ 16 =   6 avec un reste de  1 (1)

Représentation hexadécimale sur 2 chiffres : 61
```

## Améliorations futures

- Conversion inverse : binaire/hexadécimal vers texte

