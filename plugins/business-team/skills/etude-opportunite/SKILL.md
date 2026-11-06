---
name: etude-opportunite
description: Étudie de long en large une idée d’activité ou le renforcement d’une activité existante, vérifie un brainstorm ou une étude déjà faite, chiffre les scénarios, liste les risques, propose parades et tests, puis rend un verdict démarrer ou pas. Utiliser quand l’utilisateur se demande s’il doit se lancer, investir, renforcer ou abandonner une activité, veut challenger une idée de business ou faire vérifier des recherches faites avec une autre IA.
metadata:
  version: "1.0.0"
  updated: "2026-11-07"
---

# Étude d’opportunité

## Principes non négociables

- Chaque étape est confiée à l’agent dont c’est le métier. Tu ne fais toi-même ni recherche, ni calcul, ni critique, ni arbitrage.
- Les agents s’appellent `business-team:enqueteur`, `business-team:comptable`, `business-team:avocat-du-diable`, `business-team:stratege` et `business-team:redacteur`. S’ils ne sont pas disponibles, le dire à l’utilisateur et s’arrêter, ne pas les imiter.
- Un brainstorm ou une étude fournis par l’utilisateur sont des **hypothèses à vérifier**, jamais des faits. Aucun chiffre du document n’est transmis au Comptable avant d’avoir été vérifié par l’Enquêteur, ou marqué comme non vérifié.
- Ne jamais inventer de donnée. Une information absente reste `[à compléter]` d’une étape à l’autre.
- Transmettre à chaque agent les pièces utiles des étapes précédentes, telles quelles, avec leurs sources. Un sous-agent ne voit pas cette conversation : lui donner le chemin des fichiers et tout ce dont il a besoin.
- Ne pas utiliser d’em dash.

## Données d’entrée attendues

Demander ou utiliser si disponible :

- **Mode** : démarrer une nouvelle activité, ou renforcer une activité existante.
- L’idée en quelques phrases : quoi, pour qui, quel problème, comment on gagne de l’argent.
- Les recherches déjà faites : brainstorm, étude, notes. De préférence en fichier, cité avec `@fichier`, plutôt que collées dans le message.
- Les critères de décision de l’utilisateur : budget maximal, temps disponible par semaine, revenu visé et délai, tolérance au risque.
- En mode renforcer : chiffre d’affaires, marge, nombre de clients, ce qui marche et ce qui ne marche pas, ce que le renforcement change.
- Le niveau de confidentialité : l’Enquêteur fera des recherches web avec les mots de l’idée.

## Mission

Dire à l’utilisateur, preuves à l’appui, s’il doit démarrer, renforcer, attendre ou abandonner, et ce qu’il doit tester d’abord pour réduire les risques majeurs au moindre coût.

## Déclencheurs

Utiliser cette skill lorsque l’utilisateur veut :

- savoir s’il doit se lancer dans une activité ou y investir davantage ;
- challenger une idée de business sous tous les angles ;
- faire vérifier un brainstorm ou une étude réalisés avec une autre IA ;
- identifier les risques d’une activité et la renforcer.

Si la décision de lancer est déjà prise et qu’il faut préparer prix, fiche produit et posts, utiliser `lancement-produit`.

## Méthode

1. **Cadrer.** Vérifier les données d’entrée. Poser au plus trois questions, en priorité le mode et les critères de décision. Sans critères, le Stratège ne peut pas trancher pour l’utilisateur : le signaler.
2. **Enquêteur, vérification puis recherche.** Lui donner le chemin du document fourni. Lui demander de classer chaque affirmation (confirmée, contredite, nuancée, non trouvée), puis de chercher ce qui manque : demande réelle, concurrents et leurs prix, réglementation, tendance du marché.
3. **Comptable, scénarios.** Lui transmettre les coûts de l’utilisateur, les chiffres confirmés par l’Enquêteur et, à part, les chiffres non vérifiés. Lui demander trois scénarios, le seuil de rentabilité, la trésorerie nécessaire, le délai d’équilibre et l’analyse de sensibilité. En mode renforcer, partir des chiffres réels.
4. **Avocat du diable, première passe.** Lui transmettre le document de départ, la vérification et les chiffres. Lui demander tout ce qui peut échouer, y compris les biais du document de départ.
5. **Stratège.** Lui transmettre tout le dossier et les critères de l’utilisateur. Lui demander parades, plan de tests sur 30 jours, conditions de démarrage, critères d’arrêt et verdict.
6. **Avocat du diable, seconde passe.** Lui transmettre le plan du Stratège. Une seule passe. Si elle révèle un risque critique non couvert, le renvoyer au Stratège une fois pour ajuster son verdict, pas plus.
7. **Rédacteur, si l’utilisateur le veut.** Si le plan prévoit un test de la demande, lui faire écrire la page ou le post de test, avec le prix du Comptable.
8. **Assembler.** Réunir les livrables sans les réécrire, puis lister les `[à compléter]` restants.

Les étapes sont séquentielles : chaque agent a besoin des pièces de la précédente.

## Livrables spécifiques

- Verdict argumenté et tableau de décision.
- Vérification ligne à ligne du document de départ.
- Scénarios chiffrés et analyse de sensibilité.
- Risques, parades, plan de tests sur 30 jours, critères d’arrêt.
- Texte de test de la demande, en option.

## Format de sortie recommandé

1. **Verdict** du Stratège, en tête, en deux phrases.
2. **Ce que valait le brainstorm** : tableau de vérification de l’Enquêteur, avec le nombre d’affirmations confirmées, contredites et non trouvées.
3. **Le marché** : autres résultats de l’Enquêteur, sources comprises.
4. **Les chiffres** : scénarios, seuil, trésorerie, sensibilité, par le Comptable.
5. **Ce qui peut échouer** : première passe de l’Avocat du diable.
6. **Comment renforcer** : parades, tests, conditions et critères d’arrêt du Stratège.
7. **Ce que le plan ne couvre pas** : seconde passe de l’Avocat du diable.
8. **Texte de test**, si demandé.
9. **À compléter** : toutes les zones `[à compléter]` du dossier, avec l’agent qui doit les fournir.

## Checklist qualité avant réponse

- Chaque chiffre du brainstorm utilisé par le Comptable a-t-il été vérifié, ou marqué non vérifié ?
- Le verdict cite-t-il des pièces du dossier, et tient-il compte des critères de l’utilisateur ?
- Les critères d’arrêt sont-ils mesurables et datés ?
- La seconde passe de l’Avocat du diable figure-t-elle, et le verdict en tient-il compte ?
- Chaque partie vient-elle de l’agent concerné, sans réécriture ?

## Ressources

Ces fichiers complètent cette page. Les lire au moment indiqué :

- [references/example-output.md](references/example-output.md) : exemple fictif du dossier. Le lire avant d’assembler, pour le format et le niveau de détail attendus.
- [references/quality-checklist.md](references/quality-checklist.md) : contrôles détaillés. Les passer avant de livrer, en plus de la section `Checklist qualité avant réponse`.
- [templates/prompt-template.md](templates/prompt-template.md) : modèle de demande. Le proposer à l’utilisateur quand des données d’entrée manquent, pour qu’il le complète.
