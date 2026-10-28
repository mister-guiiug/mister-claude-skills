# Exemple de sortie

Exemple fictif produit à des fins d’illustration. Les photos, attributs et données ne correspondent à aucune personne réelle.

## Situation

Trois photos candidates fournies. Positionnement, architecte IT, socles d’intégration. Audience, recruteurs et DSI. Reprise photo possible.

## 1. Tri d’admissibilité

| Photo | Décision | Motif |
| --- | --- | --- |
| A, terrasse, t-shirt gris | Admise | Aucun motif d’écartement, tiers éloignés et supprimables |
| B, intérieur, pull marine | Admise | Aucun motif d’écartement |
| C, bord de mer, torse nu | **Écartée** | Torse nu, fabrication de tenue nécessaire |

La photo C reste utile comme référence d’expression, elle ne sera pas retouchée.

## 2. Diagnostic

Photo A :

| Point | Constat | Corrigeable |
| --- | --- | --- |
| Tenue | T-shirt gris, réelle, encolure couverte | Aucune fabrication |
| Tiers | Trois personnes en arrière-plan éloigné | Oui |
| Angle | Niveau des yeux | Rien à corriger |
| Lumière | Douce et homogène sur le visage | Rien à corriger |
| Expression | Sourire fermé naturel | Rien à corriger |
| Résolution utile | 919 px après recadrage carré | Confortable |

Photo B :

| Point | Constat | Corrigeable |
| --- | --- | --- |
| Tenue | Pull marine, réelle et plus formelle | Aucune fabrication |
| Angle | Contre-plongée marquée, plafond dans le cadre | **Non** |
| Lumière | Fenêtre brûlée à gauche | Partiellement |
| Expression | Fermée, sans sourire | **Non** |
| Résolution utile | 919 px | Confortable |

## 3. Classement

| Rang | Photo | Verdict |
| --- | --- | --- |
| 1 | A | Retenue, aucun défaut non corrigeable |
| 2 | B | Écartée, contre-plongée non corrigeable malgré une tenue plus formelle |
| 3 | C | Écartée à l’admissibilité |

Photo retenue, A. La tenue de B est plus adaptée à l’audience, mais un angle non corrigeable l’emporte sur un avantage vestimentaire.

## 4. Mode de production et niveau de fabrication

Mode retenu, conservation. Niveau 1 sur l’échelle de fabrication, retrait d’une impression sur le vêtement. Aucun risque de rendu.

Option proposée, niveau 2 si l’audience impose plus de formalité, remplacement du t-shirt par un polo noir. Risque faible, l’encolure est déjà couverte.

## 5. Prompt retenu, niveau 1

```text
Edit this photograph. Preserve the person's identity exactly: same face, same facial
features, same expression, same smile, same eyes, same eyebrows, same facial hair, same
skin tone, same age, same body shape, same hairstyle. Do not beautify, do not slim, do not
reshape anything.

Keep the existing grey heather crew neck t-shirt exactly as it is, same color, same
fabric, same folds. Remove any printed graphic or logo from the garment, leaving plain
grey heather fabric.

Remove all other people from the image. Remove the glass facade, the furniture and the
horizon. Replace the entire background with a plain neutral light grey gradient, clean,
no texture, no text, no objects.

Keep the existing soft even lighting on the face. Neutralise the warm color cast. Keep
natural skin texture and pores. No skin smoothing, no beauty filter.

Recompose to a chest-up square 1:1 crop, face centered horizontally, eyes on the upper
third line, face occupying about 60 percent of the image height.

Output a high resolution photograph.

Avoid: text, watermark, logo, brand, printed graphic, plastic skin, heavy skin smoothing,
other people, background objects, visible arm, distorted features.
```

## 6. Contrôles, par ordre de probabilité d’échec

1. Fragments de tiers subsistant sur les bords après recadrage, surtout à droite.
2. Dominante de couleur, vérifier qu’elle n’a pas viré au gris terne.
3. Impression du vêtement, vérifier sa suppression complète.
4. Lisibilité en vignette, réduire à 100 pixels de côté et vérifier que le visage reste identifiable.

Prévoir 1 à 2 générations pour un prompt de niveau 1.

## 7. Points à vérifier ou compléter

- Le t-shirt gris est-il représentatif de la tenue professionnelle réelle, `[à compléter]`.
- Fichier original haute résolution, `[à compléter]`.
- Générateur visé, `[à compléter]`.
