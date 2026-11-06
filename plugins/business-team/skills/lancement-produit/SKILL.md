---
name: lancement-produit
description: Enchaîne les 4 agents de l’équipe business, Enquêteur, Comptable, Rédacteur puis Avocat du diable, pour préparer le lancement d’un produit de la recherche de marché à la fiche produit. Utiliser quand l’utilisateur veut étudier, chiffrer, présenter et éprouver un produit ou une offre en une seule demande, ou demande de faire travailler toute l’équipe.
metadata:
  version: "1.0.0"
  updated: "2026-11-07"
---

# Lancement produit

## Principes non négociables

- Chaque étape est confiée à l’agent dont c’est le métier. Tu ne fais pas toi-même la recherche, les calculs, la rédaction ni la critique.
- Les agents de ce plugin s’appellent `business-team:enqueteur`, `business-team:comptable`, `business-team:redacteur` et `business-team:avocat-du-diable`. S’ils ne sont pas disponibles, le dire à l’utilisateur et s’arrêter, ne pas les imiter.
- Ne jamais inventer de donnée. Une information absente reste `[à compléter]` d’une étape à l’autre.
- Transmettre à chaque agent les résultats utiles des étapes précédentes, tels quels, avec leurs sources.
- Ne pas utiliser d’em dash.

## Données d’entrée attendues

Demander ou utiliser si disponible :

- Le produit ou l’offre : ce que c’est, pour qui, quel problème il règle.
- Le marché visé : pays, canal de vente (site, marketplace, boutique), cible.
- Les coûts connus : achat ou fabrication, livraison, frais de plateforme, emballage.
- Le prix envisagé, s’il existe déjà.
- Les supports à rédiger : fiche produit, post et sur quel réseau.
- Les étapes à sauter, si l’utilisateur a déjà une partie du travail.

## Mission

Produire en une demande un dossier de lancement complet : faits sourcés, chiffres, textes prêts à publier et liste des risques, chaque partie faite par l’agent spécialisé.

## Déclencheurs

Utiliser cette skill lorsque l’utilisateur veut :

- préparer le lancement d’un produit ou d’une offre de bout en bout ;
- faire travailler toute l’équipe business sur un même sujet ;
- obtenir recherche, prix, fiche produit et risques dans un seul livrable.

Pour une seule tâche, appeler directement l’agent concerné plutôt que cette skill. Si l’utilisateur se demande encore s’il doit se lancer, utiliser `etude-opportunite`.

## Méthode

1. **Cadrer.** Vérifier les données d’entrée. Poser au plus deux questions si le produit ou le marché manquent. Sinon, avancer et marquer le reste `[à compléter]`.
2. **Enquêteur.** Lui demander les prix publics des concurrents, la taille ou la tendance du marché et les contraintes réglementaires, avec sources.
3. **Comptable.** Lui transmettre les coûts de l’utilisateur et les prix trouvés par l’Enquêteur. Lui demander coût de revient, prix de vente HT et TTC, marge et seuil de rentabilité.
4. **Rédacteur.** Lui transmettre le brief produit, les faits sourcés utiles et le prix retenu. Lui demander les supports voulus.
5. **Avocat du diable.** Lui transmettre tout le dossier. Lui demander la liste de ce qui peut échouer.
6. **Assembler.** Réunir les quatre livrables sans les réécrire, puis lister les `[à compléter]` restants.

Les étapes 2 et 3 ne se lancent pas en parallèle : le Comptable a besoin des prix du marché. L’étape 4 peut partir dès que le prix est connu.

## Livrables spécifiques

- Dossier de lancement en quatre parties, une par agent.
- Liste consolidée des informations manquantes.

## Format de sortie recommandé

1. Résumé en trois lignes : produit, prix proposé, risque le plus grave.
2. Recherche, sortie de l’Enquêteur avec ses sources.
3. Chiffres, tableau du Comptable avec formules et hypothèses.
4. Textes, sortie du Rédacteur, directement copiable.
5. Risques, liste de l’Avocat du diable.
6. À compléter, toutes les zones `[à compléter]` du dossier.

## Checklist qualité avant réponse

- Chaque partie vient bien de l’agent concerné, et n’a pas été réécrite ?
- Chaque fait de la recherche a-t-il sa source ?
- Le prix utilisé par le Rédacteur est-il celui du tableau du Comptable ?
- Les risques sont-ils restés sans solution proposée ?
- Les zones `[à compléter]` sont-elles toutes listées à la fin ?

## Ressources

Ces fichiers complètent cette page. Les lire au moment indiqué :

- [references/example-output.md](references/example-output.md) : exemple fictif du dossier. Le lire avant d’assembler, pour le format et le niveau de détail attendus.
- [references/quality-checklist.md](references/quality-checklist.md) : contrôles détaillés. Les passer avant de livrer, en plus de la section `Checklist qualité avant réponse`.
- [templates/prompt-template.md](templates/prompt-template.md) : modèle de demande. Le proposer à l’utilisateur quand des données d’entrée manquent, pour qu’il le complète.
