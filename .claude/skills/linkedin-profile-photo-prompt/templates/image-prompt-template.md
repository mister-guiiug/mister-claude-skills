# Squelettes de prompts image

Remplacer chaque `{...}` par une donnée fournie par l’utilisateur. Ne jamais deviner un attribut physique.

Les prompts sont classés par niveau de fabrication. Toujours partir du niveau le plus bas possible.

## Bloc de préservation d’identité

À placer en tête de tout prompt d’édition.

```text
Preserve the person's identity exactly: same face, same facial features, same expression,
same smile, same eyes, same eyebrows, same facial hair, same skin tone, same age, same
body shape, same hairstyle. Do not beautify, do not slim, do not reshape anything.
```

## Bloc négatif consolidé

À placer en fin de tout prompt. Retirer les termes sans objet.

```text
Avoid: text, watermark, logo, brand, printed graphic, pattern, plastic skin, heavy skin
smoothing, beauty filter, oversaturation, dramatic color grading, busy background, other
people, background objects, visible arm, low camera angle, upward shooting angle, visible
nostrils, ceiling in frame, wet skin sheen, water droplets, distorted features, distorted
glasses frames, floating collar, asymmetric collar, misaligned button placket, unnatural
neck to shoulder transition, visible tan line, mismatched skin tone between face and
hands, extra fingers, missing fingers, merged fingers, deformed hands, extra limbs.
```

## Niveau 0 et 1, conservation

Fond, lumière, recadrage, retrait de tiers et d’un logo. Aucune fabrication.

```text
Edit this photograph.
{bloc de préservation d'identité}

Keep the existing {description de la tenue réelle} exactly as it is, same color, same
fabric, same folds. Remove any printed graphic or logo from the garment, leaving plain
fabric.

Remove all other people from the image. Remove {éléments d'arrière-plan à retirer}.
Replace the entire background with a plain neutral {light grey ou mid grey} gradient,
clean, no texture, no text, no objects.

Even out the lighting on the face, reduce harsh shadows and specular highlights, keep
natural skin texture and pores. Correct white balance, neutralise any color cast, no
beauty filter.

Recompose to a chest-up square 1:1 crop, face centered horizontally, eyes on the upper
third line, face occupying about 60 percent of the image height.

Output a high resolution photograph.
{bloc négatif}
```

## Niveau 2, remplacement de tenue

À utiliser seulement quand l’encolure est déjà couverte de tissu. Reprendre le prompt de niveau 0 et remplacer le bloc tenue.

Pull col rond :

```text
Replace the {tenue d'origine} with a plain dark navy crew neck sweater, fine knit, matte
fabric, no logo, no pattern, no text. Keep the exact same shoulder line, the same body
posture and the same neckline position. Natural fabric folds. Fabric lighting must match
the existing light on the face.
```

Polo :

```text
Replace the {tenue d'origine} with a plain black polo shirt, matte fabric, soft collar,
two-button placket closed, no logo, no pattern, no text. Keep the exact same shoulder line
and body posture. Natural fabric folds. Fabric lighting must match the existing light on
the face.
```

Chemise. Elle ouvre l’encolure, donc elle exige de générer une petite zone de peau.

```text
Replace the {tenue d'origine} with a plain {light blue, white, navy blue} button-down
shirt, cotton poplin, matte fabric, no sheen, no logo, no pattern, no text, no pocket.
Long sleeves. Structured collar sitting flat and symmetrical on both sides. Top button
open, second button closed. Straight vertical button placket, centered. Keep the exact
same shoulder line and body posture.

Generate the small area of neck and upper chest exposed by the open collar, matching the
person's existing skin tone, texture and lighting exactly. No tan line, no color
discontinuity.
```

Si le tissu rendu paraît satiné, ajouter `heavy cotton texture, visible weave`.

## Niveau 3, ajout de tenue sur peau nue

Risque élevé. Annoncer le risque et proposer le repli avant de produire ce prompt.

```text
Edit this photograph.
{bloc de préservation d'identité}

Dress the person in a plain {tenue} , matte fabric, no logo, no pattern, no text. The
neckline sits naturally at the base of the neck. Shoulders, chest and arms fully covered.
Natural fabric folds following the actual body posture and the existing shoulder line.

Remove all water droplets and wet sheen from the neck, shoulders and upper chest before
applying the garment. Reduce specular highlights on the skin so the clothing and the skin
share the same finish.

Fabric lighting must match the existing light on the face.

{bloc fond, lumière, recadrage du niveau 0}
{bloc négatif}
```

Contrôle prioritaire : la jonction cou et épaules, à 200 pour cent.

## Niveau 4, pose générée et extension du cadre

Risque très élevé. Le visage rétrécit dans le cadre, ce qui dégrade la lisibilité en vignette, usage principal d’une photo de profil. Toujours proposer le repli au niveau inférieur.

```text
Edit and extend this photograph.
{bloc de préservation d'identité, avec same head position and same head angle}

{bloc tenue du niveau 2 ou 3}

Extend the image downward to a waist-up composition. Generate the torso and both arms in
a natural crossed-arms pose: forearms crossed at mid torso, right forearm resting over the
left, hands relaxed, fingers together and naturally curved, no clenched fists. Shoulders
relaxed and level, body kept in the same orientation as the original.

Both hands must be anatomically correct: five fingers each, correct proportions, no extra
or missing fingers, no merged fingers, no distortion. Hands partially tucked under the
opposite arm is acceptable and preferred.

Skin tone of the hands and forearms must match the face exactly.

{bloc fond du niveau 0}

Compose as a waist-up square 1:1 crop, subject centered, eyes on the upper third line,
generated pose fully visible in the lower third.

Output a high resolution photograph.
{bloc négatif}
```

Contrôles prioritaires : les mains, puis la jonction entre la photo d’origine et la partie générée.

## Génération à partir d’une photo de référence, 3 variantes

Sobre corporate :

```text
Professional corporate headshot of a {age range} {gender expression} person,
{hair description}, {facial hair}, {glasses}, wearing {wardrobe}.
Chest-up framing, camera at eye level, subject facing camera, direct eye contact, calm
confident expression, subtle closed-mouth smile.
Soft key light at 45 degrees with gentle fill, no harsh shadows.
Plain light grey seamless studio background.
Shot on 85mm lens, f/4, natural skin texture, realistic colors, square 1:1 crop,
high resolution photograph.
{bloc négatif}
```

Expert accessible :

```text
Natural professional portrait of a {age range} {gender expression} person,
{hair description}, {facial hair}, {glasses}, wearing {wardrobe}.
Shoulders-up framing, slight three-quarter angle, eyes to camera, warm approachable
expression, relaxed posture.
Soft daylight from a large window, gentle contrast.
Modern office interior fully blurred in the background, no readable text or signage.
Shot on 85mm lens, f/2.8, shallow depth of field, natural skin texture, square 1:1 crop,
high resolution photograph.
{bloc négatif}
```

Exécutif :

```text
Executive portrait of a {age range} {gender expression} person,
{hair description}, {facial hair}, {glasses}, wearing {wardrobe}.
Chest-up framing, straight to camera, composed and authoritative expression, minimal smile.
Directional key light, controlled contrast, soft rim light separating subject from
background.
Dark neutral gradient background, deep grey to charcoal.
Shot on 85mm lens, f/4, editorial retouching, natural skin texture, square 1:1 crop,
high resolution photograph.
{bloc négatif}
```

Sur la variante exécutive, une tenue foncée sur fond charbon annule la séparation. Le rim light la compense partiellement, une tenue plus claire donne un meilleur résultat.

## Correction de perspective

À isoler, jamais à fondre dans un autre prompt, pour rester vérifiable.

```text
Apply a subtle wide-angle lens distortion correction to restore natural facial proportions
for an 85mm equivalent perspective.
Do not restyle, slim, reshape or beautify the face. Do not change the nose shape beyond
the geometric correction. Preserve identity exactly.
```

Comparer avant et après. Si l’utilisateur ne se reconnaît pas, ne pas conserver.

## Bannière LinkedIn 1584 x 396

```text
Abstract professional banner image, 4:1 ultra wide format, 1584x396 pixels.
Theme: {thème lié au positionnement}.
Minimal geometric composition, subtle depth, {palette couleur}.
Left third intentionally empty and visually calm to leave room for the profile picture.
No text, no logo, no watermark, no human figure.
Clean modern corporate style, high resolution.
```

Ajouter le texte de la bannière avec un outil de mise en page plutôt que par génération, les modèles d’image restant peu fiables sur le rendu typographique.

## Brief photographe

```text
Objectif : photo de profil LinkedIn pour un profil {positionnement}, audience {audience}.
Cadrage : plan buste, format carré exploitable, visage à environ 60 pour cent de la hauteur.
Expression : {neutre confiante, léger sourire, assurée}.
Lumière : source principale douce à 45 degrés, remplissage léger, pas d'ombre dure.
Arrière-plan : {uni clair, dégradé sombre, bureau flouté}, sans texte ni logo.
Optique : 85 mm, ouverture f/2.8 à f/4.
Tenue : {tenue réelle}, prévoir deux options.
Livrables : fichiers haute résolution non retouchés et une sélection retouchée légèrement,
sans lissage de peau.
```

## Paramètres par générateur

- Midjourney : ajouter `--ar 1:1` pour le profil et `--ar 4:1` pour la bannière, déplacer le bloc négatif vers le paramètre d’exclusion de l’outil.
- Stable Diffusion : déplacer le bloc négatif dans le champ de prompt négatif.
- DALL·E et Gemini : conserver les phrases naturelles, le bloc négatif reste exprimé en toutes lettres.
- Firefly : régler le ratio et le style dans l’interface, garder le prompt descriptif court.

Vérifier la syntaxe exacte dans la documentation de l’outil, les paramètres évoluent.

## Nombre de générations à prévoir

| Niveau | Essais à prévoir |
| --- | --- |
| 0 et 1 | 1 à 2 |
| 2, pull ou polo | 2 à 3 |
| 2, chemise à col structuré | 3 à 5 |
| 3 | 5 |
| 4 | 5 à 10 |

Si le résultat ne tient pas après le nombre indiqué, redescendre d’un niveau ou proposer la reprise photo.
