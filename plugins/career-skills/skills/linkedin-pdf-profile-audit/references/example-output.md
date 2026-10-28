# Exemple de sortie

Exemple fictif produit à des fins d’illustration. Le profil, les entreprises et les données ne correspondent à aucune personne réelle.

Persona retenu, auto-audit. En évaluation de candidature, les sections 4 et 6 seraient remplacées par les forces démontrées, les zones non démontrées et les questions d’entretien.

## 1. Ce que l’export permet de voir, et ce qu’il ne permet pas

Sections lues dans le PDF, 4 pages : en-tête, contact, compétences principales, résumé, 4 expériences, formation, 2 certifications.

Non visibles dans l’export, à me transmettre avant de conclure :

- Photo de profil et bannière.
- Section Sélection ou Featured.
- Recommandations reçues.
- Activité et publications récentes.
- Compétences au delà des 3 affichées.
- URL personnalisée du profil.
- Mention Open to work active ou non.

## 2. Inventaire et chronologie

| Section | État |
| --- | --- |
| Titre | Présent |
| Résumé | Présent, 2 phrases |
| Expériences | 4 postes, dont **2 sans description** |
| Formation | Présente |
| Certifications | 2, dont une sans date |
| Compétences principales | 3 affichées |

Chronologie reconstituée :

| Période | Poste | Observation |
| --- | --- | --- |
| 2013 à 2017 | Ingénieur systèmes, Entreprise A | Description présente |
| 2017 à 2019 | Ingénieur intégration, Entreprise A | **Aucune description** |
| **2019 à 2020** | **Aucun poste renseigné** | **Trou de 9 mois, non expliqué** |
| 2020 à ce jour | Architecte IT, Entreprise B | Description présente, 4 lignes |

Le trou de 9 mois est un constat, pas une interprétation. Formation, congé, transition, recherche, je ne peux pas le savoir. Dis-moi ce qu’il recouvre et je proposerai une formulation.

## 3. Constats classés par priorité

### P1, bloquants, correction rapide

| # | Constat | Élément concerné | Effet |
| --- | --- | --- | --- |
| 1 | Le titre reprend un intitulé interne, `Architecte N3 Pôle Socles` | Titre | Incompréhensible hors de l’entreprise, invisible en recherche |
| 2 | Deux expériences sur quatre n’ont aucune description | Postes 2017 à 2019 et Entreprise A | Quatre ans de parcours sans aucune preuve |
| 3 | Le résumé ouvre sur une phrase générique | Résumé, ligne 1 | Les premières lignes seules sont visibles avant le repli |
| 4 | Aucune métrique dans l’ensemble du profil | Toutes sections | Aucune preuve d’impact pour un profil senior |

### P2, crédibilité, correction rapide

| # | Constat | Élément concerné |
| --- | --- | --- |
| 5 | Trou chronologique de 9 mois non expliqué | 2019 à 2020 |
| 6 | Une certification sans date ni organisme | Certifications |
| 7 | La compétence `Gouvernance` n’apparaît dans aucune expérience | Compétences principales |

### P3 et P4

- P3, les descriptions des postes 1 et 4 emploient trois fois la même tournure d’ouverture.
- P4, le lieu indiqué est une ville sans région, peu lisible pour un recruteur étranger.

## 4. Reformulations

### P1 numéro 1, titre

Avant :

```text
Architecte N3 Pôle Socles
```

Après, 3 variantes :

```text
Architecte IT, plateformes d'intégration et API management
```

```text
Architecte IT, socles d'intégration en grande entreprise
```

```text
Architecte IT, je fais disparaître des socles historiques sans arrêter la production
```

### P1 numéro 3, ouverture du résumé

Avant :

```text
Passionné d'informatique depuis toujours, je mets mes compétences au service
des projets de mon entreprise.
```

Après :

```text
Je travaille sur les socles d'intégration historiques à fort risque d'exploitation,
et je conduis leur remplacement sans interruption de service.
```

### P1 numéro 2, expérience sans description

Le PDF ne contient aucune matière sur ce poste. Je ne peux pas la produire. Structure à remplir :

```text
[Contexte en une ligne : périmètre, taille, contrainte principale]
- [Décision prise, avec l'alternative écartée]
- [Résultat mesuré, avec unité et période de référence]
- [Périmètre : équipes, applications, utilisateurs]
```

Si tu me décris ce poste librement, même sans structure, `achievement-extractor` produira ces bullets.

## 5. Questions ouvertes

- Que recouvre la période de 9 mois entre 2019 et 2020 ?
- La certification sans date est-elle toujours valide ?
- Quel rôle vises-tu, l’audit est resté générique faute de cible.
- As-tu 3 offres qui t’intéressent réellement, pour calibrer le vocabulaire ?

## 6. Plan de correction

| Ordre | Action | Durée |
| --- | --- | --- |
| 1 | Remplacer le titre, variante 2 | 2 minutes |
| 2 | Réécrire la première phrase du résumé | 5 minutes |
| 3 | Me décrire les deux postes sans description | 20 minutes |
| 4 | Compléter la certification et retirer la compétence non prouvée | 5 minutes |
| 5 | Traiter le trou chronologique une fois sa nature connue | 5 minutes |

**Première action aujourd’hui** : remplacer le titre. C’est le seul changement de deux minutes qui modifie la visibilité en recherche.

## 7. Orientation

La première priorité qui demande de la matière est l’absence de descriptions. Enchaîner avec `achievement-extractor` sur les deux postes concernés, puis revenir avec `linkedin-profile-optimizer` pour la mise en forme finale.
