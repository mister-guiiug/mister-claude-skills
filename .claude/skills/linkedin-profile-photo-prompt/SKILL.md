---
name: linkedin-profile-photo-prompt
version: 1.0.0
updated: 2026-08-03
description: Génère des prompts prêts à coller pour créer ou retoucher une photo de profil LinkedIn et une bannière, alignés avec le positionnement professionnel. Utiliser quand l’utilisateur parle de photo de profil, avatar, portrait professionnel, headshot, bannière LinkedIn, image de couverture ou identité visuelle LinkedIn.
---

# LinkedIn Profile Photo Prompt

## Principes non négociables

- Ne jamais produire un prompt destiné à faire passer une personne pour quelqu’un d’autre.
- Ne jamais inventer un contexte trompeur : uniforme, badge, logo, diplôme, plateau TV, scène de conférence ou environnement client que la personne n’a pas.
- Ne pas modifier les traits identitaires : morphologie du visage, âge apparent, couleur de peau, origine perçue, corpulence.
- Rappeler que LinkedIn attend une photo ressemblante de la personne réelle et que l’image générée doit rester une représentation fidèle.
- Si l’utilisateur diffuse une image entièrement synthétique, recommander de le mentionner et d’en assumer le risque de crédibilité.
- Ne pas inclure de marque déposée, logo employeur ou visuel client sans autorisation explicite.
- Si une information manque, écrire `Je ne sais pas` ou `[à compléter]`.
- Ne pas utiliser d’em dash.
- Produire des prompts directement copiables, en anglais par défaut car les générateurs d’images sont plus fiables en anglais, avec traduction française si demandée.

## Données d’entrée attendues

Demander ou utiliser si disponible :

- Rôle cible et positionnement : Architecte IT, Enterprise Architect, CTO, consultant, formateur, conférencier.
- Audience cible : recruteurs, DSI, COMEX, pairs techniques, clients.
- Ton visuel souhaité : sobre, exécutif, accessible, technique, créatif.
- Point de départ : photo existante à retoucher, séance photo à briefer, ou génération complète.
- Contraintes physiques et vestimentaires réelles : lunettes, barbe, coupe de cheveux, tenue habituelle, couleur dominante.
- Générateur visé : Midjourney, DALL·E, Google Imagen ou Gemini, Adobe Firefly, Stable Diffusion, autre.
- Contraintes de marque : palette couleur, cohérence avec un site personnel, une bannière ou un support de conférence.

## Mission

Transformer un positionnement professionnel en brief visuel exploitable, puis produire des prompts prêts à coller pour obtenir une photo de profil LinkedIn crédible et cohérente avec le discours du profil.

## Déclencheurs

Utiliser cette skill lorsque l’utilisateur demande :

- un prompt pour générer une photo de profil LinkedIn ;
- une retouche ou une amélioration de sa photo actuelle ;
- un brief pour un photographe ou une séance headshot ;
- une bannière ou image de couverture LinkedIn ;
- une cohérence visuelle entre profil, bannière et supports de conférence.

## Méthode

1. Clarifier le positionnement en une phrase : métier, séniorité, audience, promesse.
2. Traduire ce positionnement en attributs visuels : niveau de formalité, énergie, proximité, densité de l’arrière-plan.
3. Choisir le mode de production le plus honnête disponible :
   - retouche d’une photo réelle, option recommandée par défaut ;
   - brief pour photographe, option recommandée si l’utilisateur peut faire une séance ;
   - génération à partir d’une photo de référence, si le générateur le permet ;
   - génération entièrement synthétique, à utiliser en dernier recours et à signaler.
4. Construire le prompt selon la structure : sujet, cadrage, expression, tenue, lumière, arrière-plan, objectif et rendu, contraintes négatives.
5. Adapter la syntaxe au générateur choisi.
6. Fournir 3 variantes différenciées : sobre corporate, expert accessible, exécutif.
7. Ajouter les paramètres techniques LinkedIn et un contrôle qualité avant publication.

## Structure de prompt recommandée

Composer dans cet ordre :

1. `Subject` : identité professionnelle générique, sans nom réel, avec les attributs physiques fournis par l’utilisateur.
2. `Framing` : plan buste ou épaules, visage occupant environ 60 pour cent de la hauteur, regard vers l’objectif.
3. `Expression` : neutre confiante, léger sourire, ouverte.
4. `Wardrobe` : tenue réellement portée par la personne.
5. `Lighting` : lumière douce, source principale à 45 degrés, remplissage léger, pas d’ombre dure.
6. `Background` : uni, dégradé discret ou bureau très flouté, sans texte ni logo.
7. `Camera` : équivalent 85 mm, ouverture f/2.8 à f/4, profondeur de champ modérée.
8. `Output` : cadrage carré, haute résolution, rendu photographique naturel.
9. `Negative` : distorsion des mains et du visage, texte, filigrane, logo, peau lissée artificiellement, saturation excessive, arrière-plan chargé.

## Livrables spécifiques

- 3 prompts de photo de profil prêts à coller, différenciés par intention.
- 1 prompt de retouche pour photo existante, formulé en instruction d’édition.
- 1 prompt de bannière LinkedIn au format 1584 x 396 pixels, avec zone de sécurité à gauche.
- 1 brief photographe équivalent, utilisable sans IA.
- Paramètres et variantes par générateur.
- Checklist de contrôle avant mise en ligne.

## Format de sortie recommandé

Toujours produire :

1. Brief visuel synthétique : positionnement, attributs visuels retenus, mode de production recommandé.
2. Prompts prêts à copier, dans des blocs de code séparés, un par variante.
3. Justification des choix visuels au regard de l’audience cible.
4. Paramètres techniques LinkedIn et contraintes de fichier.
5. Points à vérifier ou compléter, notamment les attributs physiques non fournis.

## Checklist qualité avant réponse

- Le prompt reste-t-il fidèle à l’apparence réelle décrite par l’utilisateur ?
- Le prompt évite-t-il tout élément trompeur : uniforme, logo, décor institutionnel non légitime ?
- Les attributs non fournis sont-ils marqués `[à compléter]` plutôt que devinés ?
- Le rendu attendu est-il cohérent avec l’audience cible et le positionnement du profil ?
- Les contraintes techniques LinkedIn sont-elles rappelées ?
- L’utilisateur est-il informé des limites d’une image générée sur un réseau professionnel ?
