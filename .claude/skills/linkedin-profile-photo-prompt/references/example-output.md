# Exemple de sortie

Exemple fictif produit à des fins d’illustration. Les attributs physiques utilisés sont ceux d’un profil fictif.

## Brief visuel

- Positionnement : architecte IT, socles d’intégration, grande entreprise.
- Audience : recruteurs, DSI, architectes.
- Attributs visuels retenus : formalité moyenne à élevée, arrière-plan neutre, expression posée.
- Mode de production recommandé : retouche d’une photo existante. L’utilisateur dispose d’une photo récente, c’est l’option la plus fidèle et la plus rapide.

## Prompt de retouche, option recommandée

```text
Edit this photograph without changing the person's face, identity, age, body shape or
skin tone. Keep the original facial features and expression.
Replace the background with a plain neutral grey gradient, fully clean, no text and no
objects.
Even out the lighting on the face, reduce harsh shadows, keep natural skin texture.
Correct white balance, mild color correction, no beauty filter.
Recompose to a chest-up square 1:1 crop with the face occupying about 60 percent of the
image height.
Output a high resolution photograph.
```

## Variante sobre corporate

```text
Professional corporate headshot of a 40 to 45 year old man, short brown hair,
short trimmed beard, thin metal glasses, wearing a plain navy shirt.
Chest-up framing, subject facing camera, direct eye contact, calm confident expression,
subtle closed-mouth smile.
Soft key light at 45 degrees with gentle fill, no harsh shadows.
Plain light grey seamless studio background.
Shot on 85mm lens, f/4, natural skin texture, realistic colors, square 1:1 crop,
high resolution photograph.
Avoid: text, watermark, logo, heavy skin smoothing, oversaturation, distorted hands,
distorted glasses frames, busy background.
```

## Variante expert accessible

```text
Natural professional portrait of a 40 to 45 year old man, short brown hair,
short trimmed beard, thin metal glasses, wearing a plain navy shirt.
Shoulders-up framing, slight three-quarter angle, eyes to camera, warm approachable
expression, relaxed posture.
Soft daylight from a large window, gentle contrast.
Modern office interior fully blurred in the background, no readable text or signage.
Shot on 85mm lens, f/2.8, shallow depth of field, natural skin texture, square 1:1 crop,
high resolution photograph.
Avoid: text, watermark, logo, plastic skin, artificial bokeh shapes, cluttered background.
```

## Bannière

```text
Abstract professional banner image, 4:1 ultra wide format, 1584x396 pixels.
Theme: integration flows between distributed systems, minimal geometric composition,
subtle depth, deep blue and slate grey palette.
Left third intentionally empty and visually calm to leave room for the profile picture.
No text, no logo, no watermark, no human figure.
Clean modern corporate style, high resolution.
```

Le texte éventuel de la bannière est à ajouter avec un outil de mise en page, pas par génération.

## Justification des choix

- Formalité moyenne à élevée, l’audience inclut des recruteurs et des DSI.
- Arrière-plan neutre plutôt que bureau, le rendu reste lisible en miniature, format sous lequel la photo est le plus souvent vue.
- Aucun élément de décor technique, une salle serveur en arrière-plan serait un contexte que l’utilisateur ne fréquente pas.

## Contraintes techniques rappelées

- Format carré, affichage circulaire, ne rien placer dans les coins.
- Vérifier les limites de taille et de format en vigueur dans l’aide LinkedIn avant publication.
- Tester le rendu en miniature et sur fond sombre.

## Points à vérifier ou compléter

- Couleur réelle de la tenue portée en contexte professionnel, `[à compléter]` si différente.
- Décision de l’utilisateur sur la mention du caractère généré si l’image n’est pas une retouche.
