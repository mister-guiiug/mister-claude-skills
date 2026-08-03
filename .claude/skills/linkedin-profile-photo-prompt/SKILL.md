---
name: linkedin-profile-photo-prompt
version: 1.2.1
updated: 2026-08-03
description: Trie des photos candidates, diagnostique ce qui est corrigeable et génère des prompts prêts à coller pour une photo de profil LinkedIn et une bannière. Utiliser quand l’utilisateur parle de photo de profil, avatar, portrait professionnel, headshot, bannière LinkedIn, image de couverture, identité visuelle LinkedIn, ou quand il fournit une ou plusieurs photos à évaluer.
---

# LinkedIn Profile Photo Prompt

## Principes non négociables

- Vérifier en tout premier que le sujet de la photo est bien l’utilisateur. Si ce n’est pas le cas, demander de qui il s’agit et si cette personne a demandé ce travail. Sans réponse, se limiter à une analyse et ne produire aucun prompt de retouche ou de génération portant sur son visage.
- Ne jamais produire un prompt destiné à faire passer une personne pour quelqu’un d’autre.
- Ne jamais inventer un contexte trompeur : uniforme, badge, logo, diplôme, plateau TV, scène de conférence ou environnement client que la personne n’a pas.
- Ne pas modifier les traits identitaires : morphologie du visage, âge apparent, couleur de peau, origine perçue, corpulence.
- Ne jamais conserver dans une image destinée à la publication une personne tierce identifiable sans l’accord de cette personne. Par défaut, retirer les tiers du cadre et le dire.
- Ne jamais dépasser le niveau 2 de l’échelle de fabrication sans annoncer le risque et proposer la reprise photo.
- Rappeler que LinkedIn attend une photo ressemblante de la personne réelle et que l’image générée doit rester une représentation fidèle.
- Si l’utilisateur diffuse une image entièrement synthétique, recommander de le mentionner et d’en assumer le risque de crédibilité.
- Ne pas inclure de marque déposée, logo employeur ou visuel client sans autorisation explicite.
- Si une information manque, écrire `Je ne sais pas` ou `[à compléter]`.
- Ne pas utiliser d’em dash.
- Produire des prompts directement copiables, en anglais par défaut car les générateurs d’images sont plus fiables en anglais, avec traduction française si demandée.

## Données d’entrée attendues

Demander ou utiliser si disponible :

- Une ou plusieurs photos candidates. Plusieurs valent mieux qu’une, le tri fait une grande partie du travail.
- Dimensions et poids de chaque fichier, pour vérifier la résolution utile après recadrage carré.
- Rôle cible et positionnement : Architecte IT, Enterprise Architect, CTO, consultant, formateur, conférencier.
- Audience cible : recruteurs, DSI, COMEX, pairs techniques, clients.
- Ton visuel souhaité : sobre, exécutif, accessible, technique, créatif.
- Contraintes physiques et vestimentaires réelles : lunettes, barbe, coupe de cheveux, tenue habituelle, couleur dominante.
- Possibilité de reprendre une photo, oui ou non. Elle change la recommandation.
- Générateur visé : Midjourney, DALL·E, Google Imagen ou Gemini, Adobe Firefly, Stable Diffusion, autre.
- Contraintes de marque : palette couleur, cohérence avec un site personnel, une bannière ou un support de conférence.

## Mission

Choisir la meilleure photo disponible, établir ce qui est corrigeable et ce qui ne l’est pas, puis produire des prompts prêts à coller pour obtenir une photo de profil LinkedIn crédible et cohérente avec le positionnement.

## Déclencheurs

Utiliser cette skill lorsque l’utilisateur demande :

- un prompt pour générer une photo de profil LinkedIn ;
- une retouche ou une amélioration de sa photo actuelle ;
- de choisir la meilleure photo parmi plusieurs ;
- un avis sur une photo qu’il envisage d’utiliser ;
- un brief pour un photographe ou une séance headshot ;
- une bannière ou image de couverture LinkedIn ;
- une cohérence visuelle entre profil, bannière et supports de conférence.

## Méthode

1. Trier l’admissibilité de chaque photo fournie. Une photo inadmissible ne se retouche pas, elle s’écarte.
2. Diagnostiquer chaque photo admissible, en séparant les défauts corrigeables des défauts non corrigeables.
3. Si plusieurs photos sont fournies, les classer et annoncer la retenue avant de produire un prompt.
4. Choisir le mode de production, dans l’ordre de préférence de la section correspondante.
5. Situer l’intervention demandée sur l’échelle de fabrication et annoncer le risque associé.
6. Clarifier le positionnement en une phrase, puis le traduire en attributs visuels.
7. Construire le prompt selon la structure recommandée.
8. Adapter la syntaxe au générateur choisi.
9. Fournir les contrôles à effectuer sur le résultat, par ordre de probabilité d’échec.

## Tri d’admissibilité

À appliquer en premier, avant tout diagnostic technique. Un seul motif suffit à écarter.

| Motif | Décision |
| --- | --- |
| Le sujet principal n’est pas l’utilisateur | **Suspendre**, demander l’identité et l’accord de la personne, se limiter à l’analyse |
| Personne tierce identifiable, au premier plan ou en gros plan | Écarter, ou recadrage serré si le tiers est éloigné et supprimable |
| Torse nu, tenue de plage, tenue de sport | Écarter, sauf demande explicite de fabrication de tenue |
| Contexte festif, alcool visible, tenue de soirée | Écarter |
| Photo de groupe recadrée | Écarter |
| Enfant présent dans le cadre | Écarter |
| Visage partiellement masqué, lunettes de soleil | Écarter |
| Photo de plus de cinq ans ne correspondant plus à l’apparence actuelle | Écarter |

Toujours dire quel motif a conduit à écarter une photo. Ne jamais écarter en silence.

Indices d’une photo qui n’est pas celle de l’utilisateur : format exactement carré en 400 x 400, nom de fichier horodaté sans préfixe d’appareil, poids très faible, rendu studio sans rapport avec les autres photos fournies. Ces indices ne prouvent rien, ils justifient de poser la question.

## Diagnostic de la photo source

Produire cette grille pour chaque photo admissible.

| Point à examiner | Corrigeable |
| --- | --- |
| Arrière-plan chargé, lieu identifiable, objets | Oui |
| Personne tierce éloignée | Oui, par remplacement de fond et recadrage |
| Cadrage, orientation, sujet décentré | Oui |
| Bras du selfie visible au bord | Oui |
| Lumière plate, brillances, dominante de couleur | Oui |
| Zone brûlée sur le visage | Partiellement |
| Peau mouillée, gouttes | Partiellement |
| Logo ou impression sur le vêtement | Oui |
| Distorsion de proximité, objectif grand angle | Partiellement, voir la frontière ci-dessous |
| Angle de prise de vue, contre-plongée ou plongée forte | **Non** |
| Expression fermée, regard ailleurs, yeux fermés | **Non** |
| Cheveux mouillés ou coiffure inhabituelle | **Non**, sans modifier l’apparence |
| Résolution insuffisante | **Non** |

Un défaut non corrigeable dominant conduit à écarter la photo ou à recommander une reprise, quelle que soit la qualité du reste.

## Contrôle de résolution

Calculer le côté du plus grand recadrage carré possible, soit la plus petite des deux dimensions.

- Moins de 400 px : inutilisable, demander l’original.
- De 400 à 800 px : acceptable sans marge, signaler.
- Plus de 800 px : confortable.

Vérifier aussi le poids du fichier. Un fichier de quelques centaines de kilooctets pour une image de plus d’un mégapixel indique une recompression. Demander l’original du téléphone ou de l’appareil.

## Sélection parmi plusieurs photos

Quand plusieurs photos sont fournies, produire un classement avant tout prompt. C’est souvent la partie la plus utile de la réponse.

Colonnes à utiliser : tenue, tiers, angle, lumière, expression, résolution utile, verdict.

Règles de classement :

1. Une photo sans défaut non corrigeable passe devant une photo mieux exposée mais en contre-plongée.
2. Une tenue réelle passe devant une tenue à fabriquer.
3. À défauts corrigeables équivalents, l’expression départage. Elle ne se retouche pas.
4. Une photo non selfie passe devant un selfie de qualité comparable.
5. Annoncer explicitement la photo retenue et le motif, puis produire le prompt sur celle-là.

Une photo écartée peut rester utile comme référence, par exemple pour montrer l’expression à reproduire lors d’une reprise.

## Échelle de fabrication

Situer toute demande sur cette échelle et annoncer le niveau atteint.

| Niveau | Intervention | Risque de rendu |
| --- | --- | --- |
| 0 | Fond, lumière, recadrage, suppression de tiers | Nul |
| 1 | Tenue réelle conservée, retrait d’un logo ou d’une impression | Nul |
| 2 | Remplacement d’une tenue dont l’encolure est déjà couverte | Faible |
| 3 | Ajout d’une tenue sur peau nue | Élevé, la jonction cou et épaules échoue |
| 4 | Pose, membres ou cadre générés, extension de l’image | Très élevé, les mains échouent |

Au delà du niveau 2, toujours annoncer le risque, proposer le repli au niveau inférieur, et rappeler que la reprise photo donne un meilleur résultat pour un coût moindre.

## Frontière entre correction et modification

| Intervention | Statut |
| --- | --- |
| Correction de distorsion d’objectif pour restituer les proportions réelles | Autorisée, à vérifier image contre image |
| Amincissement, remodelage du nez, du menton ou de la mâchoire | Interdite |
| Lissage de peau, suppression des rides ou des grains de beauté | Interdite |
| Changement de coiffure, séchage de cheveux mouillés | Interdite, c’est une modification d’apparence |
| Ajout ou retrait de lunettes, de barbe | Interdite |
| Changement de tenue | Autorisée, selon l’échelle de fabrication |
| Génération d’une pose absente de la photo | Autorisée sur demande explicite, niveau 4 |

Après toute correction de perspective, demander à l’utilisateur de comparer avant et après. S’il ne se reconnaît pas, la correction est allée trop loin.

## Modes de production

Par ordre de préférence.

1. **Conservation.** La photo est admissible et ses défauts sont uniquement de niveau 0 ou 1. Fond, lumière, recadrage, c’est tout.
2. **Reprise au téléphone.** Cinq minutes, aucun coût, seule réponse valable face à un défaut non corrigeable. Protocole ci-dessous.
3. **Retouche avec remplacement de tenue.** Niveau 2, quand l’encolure est déjà couverte.
4. **Brief photographe.** Quand l’utilisateur peut faire une séance.
5. **Génération à partir d’une photo de référence.** Niveau 3 ou 4, avec les réserves annoncées.
6. **Génération entièrement synthétique.** Dernier recours, à signaler à l’audience.

### Protocole de reprise au téléphone

1. Appareil photo arrière, pas la caméra selfie. Retardateur de 10 secondes.
2. Téléphone à hauteur des yeux, jamais plus bas.
3. Reculer à 1,5 ou 2 mètres, puis zoomer à 2x. Cela supprime la distorsion de proximité.
4. Se placer face à une fenêtre sans soleil direct, ou en extérieur par ciel couvert.
5. Mur neutre derrière, à un mètre au moins, pour que le fond se détache.
6. Cadrer en plan buste, format carré ou 4:3, avec de la marge autour de la tête.
7. Faire 20 prises avec des expressions différentes, dont plusieurs avec un léger sourire fermé.

## Structure de prompt recommandée

Composer dans cet ordre :

1. `Identity` : consigne de préservation stricte, visage, expression, morphologie, coiffure.
2. `Subject` : attributs physiques fournis par l’utilisateur, sans nom réel.
3. `Wardrobe` : tenue réellement portée, ou tenue de remplacement avec le niveau de fabrication assumé.
4. `Framing` : plan buste, visage occupant environ 60 pour cent de la hauteur, regard vers l’objectif.
5. `Expression` : neutre confiante, léger sourire, ouverte.
6. `Lighting` : lumière douce, source principale à 45 degrés, remplissage léger, pas d’ombre dure.
7. `Background` : uni, dégradé discret ou bureau très flouté, sans texte, sans logo, sans tiers.
8. `Camera` : équivalent 85 mm, ouverture f/2.8 à f/4, profondeur de champ modérée.
9. `Output` : cadrage carré, haute résolution, rendu photographique naturel.
10. `Negative` : voir la liste consolidée dans `templates/image-prompt-template.md`.

## Livrables spécifiques

- Tri d’admissibilité, avec le motif de chaque photo écartée.
- Grille de diagnostic par photo admissible.
- Classement argumenté si plusieurs photos, avec la photo retenue.
- Niveau de fabrication atteint et risque annoncé.
- 3 prompts de photo de profil prêts à coller, différenciés par intention.
- 1 prompt de retouche pour photo existante, formulé en instruction d’édition.
- 1 prompt de bannière LinkedIn au format 1584 x 396 pixels, avec zone de sécurité à gauche.
- 1 brief photographe et 1 protocole de reprise au téléphone.
- Contrôles à effectuer sur le résultat, par ordre de probabilité d’échec.

## Format de sortie recommandé

Toujours produire :

1. Verdict et tri d’admissibilité.
2. Diagnostic, corrigeable contre non corrigeable.
3. Classement si plusieurs photos, avec la photo retenue et le motif.
4. Mode de production retenu et niveau de fabrication assumé.
5. Prompts prêts à copier, dans des blocs de code séparés, un par variante.
6. Justification des choix visuels au regard de l’audience cible.
7. Contrôles à effectuer, par ordre de probabilité d’échec.
8. Paramètres techniques LinkedIn et contraintes de fichier.
9. Points à vérifier ou compléter.

## Checklist qualité avant réponse

- Le sujet de la photo est-il bien l’utilisateur, et sinon la question a-t-elle été posée avant tout travail ?
- Le tri d’admissibilité a-t-il été fait avant tout travail technique ?
- Les personnes tierces ont-elles été traitées explicitement ?
- Les défauts non corrigeables sont-ils distingués des défauts corrigeables ?
- La résolution utile après recadrage carré a-t-elle été calculée ?
- Si plusieurs photos, le classement précède-t-il le prompt ?
- Le niveau de fabrication est-il annoncé, avec son risque et le repli possible ?
- Le prompt reste-t-il fidèle à l’apparence réelle décrite par l’utilisateur ?
- Le prompt évite-t-il tout élément trompeur, uniforme, logo, décor non légitime ?
- Les attributs non fournis sont-ils marqués `[à compléter]` plutôt que devinés ?
- Les contrôles sur le résultat sont-ils ordonnés par probabilité d’échec ?
- L’utilisateur est-il informé des limites d’une image générée sur un réseau professionnel ?
