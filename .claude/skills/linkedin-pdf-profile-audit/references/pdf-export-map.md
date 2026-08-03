# Repères sur l’export PDF LinkedIn

## Comment obtenir l’export

Depuis la page d’un profil, le menu d’actions supplémentaires propose une sauvegarde au format PDF. Le fichier obtenu porte souvent le nom `Profile.pdf` ou `Profil-<prenom>.pdf`. Le libellé exact du menu évolue, vérifier dans l’interface courante.

Il existe aussi une exportation complète des données du compte, réservée à son propre profil, qui produit des fichiers séparés et plus détaillés. Elle est plus riche mais moins lisible pour un audit. Si l’utilisateur la fournit, la traiter comme une source complémentaire.

## Un format fixe, en deux zones

La mise en page ne varie pas. C’est ce qui rend l’audit fiable.

**Zone 1, colonne latérale, fond sombre, tiers gauche de la page**

| Bloc | Français | Anglais |
| --- | --- | --- |
| Contact | Coordonnées | Contact |
| Compétences | Principales compétences | Top Skills |
| Langues | Langues | Languages |
| Certifications | Certifications | Certifications |
| Publications | Publications | Publications |
| Distinctions | Distinctions | Honors-Awards |

**Zone 2, colonne principale, deux tiers droits**

| Bloc | Français | Anglais |
| --- | --- | --- |
| Identité | Nom, titre, localisation | Nom, titre, localisation |
| Résumé | Résumé | Summary |
| Expériences | Expérience | Experience |
| Formation | Formation | Education |
| Pied de page | Page X sur Y | Page X of Y |

Structure d’une entrée d’expérience, toujours dans cet ordre :

```text
Entreprise
Intitulé du poste
Date de début - date de fin (durée calculée)
Lieu
Description, si elle existe
```

## Les deux règles de lecture qui en découlent

1. **Un bloc n’apparaît que s’il a du contenu.** Sur une extraction vérifiée complète, l’absence de `Résumé` signifie que la section est vide sur le profil. Même raisonnement pour `Certifications`, `Langues`, `Publications` et `Distinctions`. C’est un constat, pas un angle mort.
2. **L’ordre est stable.** Le `Résumé` se place entre la localisation et `Expérience`. Si l’extraction enchaîne la localisation et `Expérience`, l’absence est confirmée.

Ces deux règles ne valent que sur une extraction complète. D’où le contrôle préalable.

## Ce que l’export ne contient jamais

| Élément | Pourquoi cela compte |
| --- | --- |
| Photo de profil et bannière | Premier élément vu par un lecteur |
| Section Sélection ou Featured | Emplacement des preuves mises en avant |
| Recommandations | Preuve sociale, souvent décisive pour un profil senior |
| Activité et publications LinkedIn | Signal de visibilité et de régularité |
| Compétences au delà des principales | Couverture réelle des mots-clés de recherche |
| Validations de compétences | Crédibilité des compétences déclarées |
| Mention Open to work, paramètres de visibilité | Conditionnent l’efficacité du profil |

L’URL du profil figure dans le bloc `Coordonnées`, elle n’est donc pas un angle mort. Une URL avec suffixe numérique ou caractère accentué se constate directement.

## Ce que l’export révèle mieux que le profil en ligne

- La chronologie complète se lit d’un seul tenant, les trous et chevauchements deviennent évidents.
- Les descriptions d’expérience apparaissent en entier, sans repli ni troncature.
- La répétition de formulations d’un poste à l’autre saute aux yeux.
- Le déséquilibre entre expériences récentes et anciennes est immédiatement visible.
- Les chevauchements entre formation et emploi, souvent une alternance non déclarée, apparaissent au premier coup d’oeil.

## Extraction, points techniques

Si la lecture directe du PDF échoue :

- La mise en page en deux colonnes mélange l’ordre du texte sur une extraction linéaire. Une extraction conservant les coordonnées x et y permet de reconstituer les zones. Le seuil de séparation se situe autour de la limite du bandeau sombre, environ un tiers de la largeur de page.
- Les polices sont des sous-ensembles à identifiants de glyphes. Les chaînes apparaissent en hexadécimal, une table de correspondance vers unicode est nécessaire pour les décoder.
- Le contenu est réparti dans plusieurs flux compressés, à décompresser avant analyse.
- Les translations de repère décalent les coordonnées, il faut suivre l’empilement pour situer un fragment dans la bonne zone.

Ne jamais conclure à une section absente sans avoir vérifié que ces points ont été traités.

## Signaux à repérer en priorité

1. Résumé absent ou réduit à une phrase.
2. Expériences sans description, en particulier sur le poste le plus qualifiant.
3. Titre composé d’un intitulé interne ou d’un nom de service.
4. Trou chronologique supérieur à six mois.
5. Absence de poste en cours, la dernière expérience étant terminée.
6. Chevauchement entre une formation et un emploi, souvent une alternance non déclarée.
7. Aucune métrique dans l’ensemble du profil.
8. Compétences déclarées sans aucune trace dans les expériences.
9. URL par défaut avec suffixe numérique.
10. Publications ou distinctions sans lien avec le positionnement.
