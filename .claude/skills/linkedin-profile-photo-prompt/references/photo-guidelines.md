# Repères de production visuelle

## Formats LinkedIn

Valeurs communément documentées, à revérifier dans l’aide LinkedIn avant publication :

- Photo de profil : image carrée, minimum conseillé 400 x 400 pixels, affichage en cercle.
- Bannière de profil : 1584 x 396 pixels, ratio 4 pour 1.
- Formats de fichier usuels : JPG et PNG.

Conséquences pratiques :

- La photo est vue en miniature dans le fil et les résultats de recherche, donc le visage doit rester lisible à très petite taille.
- Le recadrage circulaire coupe les angles, ne rien placer d’important dans les coins.
- Sur la bannière, la photo de profil recouvre la partie gauche sur desktop et la position varie selon les appareils, donc garder une zone de sécurité à gauche et centrer le message utile à droite.

## Contrôle de résolution

Le côté du plus grand recadrage carré possible est égal à la plus petite des deux dimensions du fichier.

| Côté après recadrage carré | Verdict |
| --- | --- |
| Moins de 400 px | Inutilisable, demander l’original |
| 400 à 800 px | Acceptable sans marge, signaler |
| Plus de 800 px | Confortable |

Vérifier aussi le poids. Quelques centaines de kilooctets pour plus d’un mégapixel indiquent une recompression, typique d’un fichier passé par une messagerie. Demander l’original.

## Corrigeable ou non

| Défaut | Corrigeable |
| --- | --- |
| Arrière-plan chargé, lieu identifiable | Oui |
| Tiers éloigné en arrière-plan | Oui |
| Cadrage, orientation, sujet décentré | Oui |
| Bras du selfie visible au bord | Oui |
| Lumière plate, brillances, dominante de couleur | Oui |
| Logo ou impression sur le vêtement | Oui |
| Zone brûlée sur le visage | Partiellement |
| Peau mouillée, gouttes | Partiellement |
| Distorsion de proximité | Partiellement |
| Angle de prise de vue, contre-plongée | Non |
| Expression fermée, yeux fermés | Non |
| Cheveux mouillés, coiffure inhabituelle | Non |
| Résolution insuffisante | Non |

La règle de décision est simple. Un défaut non corrigeable dominant rend la photo inutilisable, même si tout le reste est bon. Une photo techniquement médiocre mais sans défaut non corrigeable reste récupérable.

## Attributs visuels par intention

| Intention | Formalité | Arrière-plan | Expression | Usage |
| --- | --- | --- | --- | --- |
| Sobre corporate | Élevée | Uni clair ou gris neutre | Neutre confiante | Candidature, grands comptes |
| Expert accessible | Moyenne | Bureau flouté, lumière naturelle | Léger sourire | Contenu, communauté, pairs |
| Exécutif | Élevée | Sombre, contrasté, dégradé | Assurée, menton légèrement bas | COMEX, conseil, conférence |

## Contraste entre tenue et fond

| Tenue | Fond à utiliser |
| --- | --- |
| Foncée, marine, noire | Gris clair |
| Blanche, très claire | Gris moyen à soutenu |
| Grise ou moyenne | Gris clair ou gris soutenu, éviter le gris moyen |

Un vêtement et un fond de valeur proche annulent la silhouette en miniature.

## Erreurs fréquentes

- Photo de groupe recadrée.
- Selfie en contre-plongée.
- Arrière-plan chargé ou reconnaissable comme un lieu privé.
- Filtre de smartphone visible.
- Photo de plus de cinq ans qui ne correspond plus à l’apparence actuelle.
- Photo verticale recadrée trop serrée qui coupe le haut du crâne.
- Tiers laissé en arrière-plan par inattention.

## Points de défaillance des générateurs, par fréquence

1. Les mains et les doigts, dès qu’une pose est générée.
2. La jonction cou et épaules, dès qu’un vêtement est ajouté sur une peau nue.
3. Le col structuré d’une chemise, pointes asymétriques ou col décollé.
4. La teinte des mains et des avant-bras, désaccordée avec le visage.
5. La patte de boutonnage, dédoublée ou désaxée.
6. La cohérence de lumière entre un tissu généré et un visage réel.
7. Les montures de lunettes, déformées ou asymétriques.

## Alternatives à la génération complète

1. Conservation, avec fond, lumière et recadrage seulement. Toujours à privilégier.
2. Reprise au téléphone, protocole dans le `SKILL.md`. Cinq minutes, aucun coût.
3. Retouche avec remplacement de tenue, quand l’encolure est déjà couverte.
4. Brief pour photographe.
5. Génération à partir d’une photo de référence.
6. Génération entièrement synthétique, en dernier recours, avec mention explicite.

## Différences de syntaxe entre générateurs

- Midjourney : prompt descriptif court, paramètres en fin de ligne comme le ratio d’image, pas de prompt négatif natif mais un paramètre dédié à l’exclusion.
- DALL·E et Gemini : phrases naturelles complètes, les contraintes négatives se formulent en langage explicite.
- Stable Diffusion : prompt positif et prompt négatif séparés, poids possibles sur les termes.
- Adobe Firefly : orienté usage commercial, options de style et de cadrage dans l’interface plutôt que dans le prompt.

Vérifier les paramètres exacts dans la documentation de l’outil utilisé, la syntaxe évolue fréquemment.
