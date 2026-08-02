# Squelettes de prompts image

Remplacer chaque `{...}` par une donnée fournie par l’utilisateur. Ne jamais deviner un attribut physique.

## 1. Photo de profil, variante sobre corporate

```text
Professional corporate headshot of a {age range} {gender expression} person,
{hair description}, {facial hair}, {glasses}, wearing {wardrobe}.
Chest-up framing, subject facing camera, direct eye contact, calm confident expression,
subtle closed-mouth smile.
Soft key light at 45 degrees with gentle fill, no harsh shadows.
Plain light grey seamless studio background.
Shot on 85mm lens, f/4, natural skin texture, realistic colors, square 1:1 crop,
high resolution photograph.
Avoid: text, watermark, logo, heavy skin smoothing, oversaturation, distorted hands,
distorted glasses frames, busy background.
```

## 2. Photo de profil, variante expert accessible

```text
Natural professional portrait of a {age range} {gender expression} person,
{hair description}, {facial hair}, {glasses}, wearing {wardrobe}.
Shoulders-up framing, slight three-quarter angle, eyes to camera, warm approachable
expression, relaxed posture.
Soft daylight from a large window, gentle contrast.
Modern office interior fully blurred in the background, no readable text or signage.
Shot on 85mm lens, f/2.8, shallow depth of field, natural skin texture, square 1:1 crop,
high resolution photograph.
Avoid: text, watermark, logo, plastic skin, artificial bokeh shapes, cluttered background.
```

## 3. Photo de profil, variante exécutive

```text
Executive portrait of a {age range} {gender expression} person,
{hair description}, {facial hair}, {glasses}, wearing {wardrobe}.
Chest-up framing, straight to camera, composed and authoritative expression, no smile
or minimal smile.
Directional key light, controlled contrast, soft rim light separating subject from
background.
Dark neutral gradient background, deep grey to charcoal.
Shot on 85mm lens, f/4, editorial retouching, natural skin texture, square 1:1 crop,
high resolution photograph.
Avoid: text, watermark, logo, dramatic color grading, heavy vignette, distorted features.
```

## 4. Retouche d’une photo existante

À utiliser avec un outil acceptant une image d’entrée. Ce mode préserve la ressemblance.

```text
Edit this photograph without changing the person's face, identity, age, body shape or
skin tone.
Keep the original facial features and expression.
Replace the background with a plain neutral grey gradient, fully clean, no text and no
objects.
Even out the lighting on the face, reduce harsh shadows, keep natural skin texture.
Correct white balance, mild color correction, no beauty filter.
Recompose to a chest-up square 1:1 crop with the face occupying about 60 percent of the
image height.
Output a high resolution photograph.
```

## 5. Bannière LinkedIn 1584 x 396

```text
Abstract professional banner image, 4:1 ultra wide format, 1584x396 pixels.
Theme: {thème lié au positionnement, par exemple distributed systems, integration flows,
cloud architecture}.
Minimal geometric composition, subtle depth, {palette couleur}.
Left third intentionally empty and visually calm to leave room for the profile picture.
No text, no logo, no watermark, no human figure.
Clean modern corporate style, high resolution.
```

Ajouter le texte de la bannière avec un outil de mise en page plutôt que par génération, les modèles d’image restant peu fiables sur le rendu typographique.

## 6. Brief photographe équivalent

```text
Objectif : photo de profil LinkedIn pour un profil {positionnement}, audience {audience}.
Cadrage : plan buste, format carré exploitable, visage à environ 60 pour cent de la hauteur.
Expression : {neutre confiante, léger sourire, assurée}.
Lumière : source principale douce à 45 degrés, remplissage léger, pas d’ombre dure.
Arrière-plan : {uni clair, dégradé sombre, bureau flouté}, sans texte ni logo.
Optique : 85 mm, ouverture f/2.8 à f/4.
Tenue : {tenue réelle}, prévoir deux options.
Livrables : fichiers haute résolution non retouchés et une sélection retouchée légèrement,
sans lissage de peau.
```

## Paramètres par générateur

- Midjourney : ajouter `--ar 1:1` pour le profil et `--ar 4:1` pour la bannière, déplacer la liste `Avoid` vers le paramètre d’exclusion de l’outil.
- Stable Diffusion : déplacer la liste `Avoid` dans le champ de prompt négatif.
- DALL·E et Gemini : conserver les phrases naturelles, la liste `Avoid` reste exprimée en toutes lettres.
- Firefly : régler le ratio et le style dans l’interface, garder le prompt descriptif court.

Vérifier la syntaxe exacte dans la documentation de l’outil, les paramètres évoluent.
