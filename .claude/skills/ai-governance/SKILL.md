---
name: ai-governance
version: 1.0.0
updated: 2026-08-03
description: Aide à cadrer la gouvernance IA, ses principes, rôles, risques, conformité, usages autorisés, contrôles et trajectoire d’adoption responsable. Utiliser quand l’utilisateur demande une politique d’usage de l’IA, un cadre de gouvernance IA, une grille de risques, un comité IA, une charte IA générative ou une trajectoire de conformité.
---

# AI Governance


## Principes non négociables

- Ne jamais inventer de donnée, source, tendance, risque, réglementation, maturité ou décision.
- Si une information n’est pas fournie ou vérifiable, écrire explicitement : `Je ne sais pas` ou demander la donnée manquante.
- Distinguer clairement : fait vérifié, analyse, hypothèse, recommandation.
- Citer les sources lorsque la demande porte sur des faits externes, tendances, réglementation, marché ou actualité.
- Privilégier les sources primaires ou reconnues : éditeurs, organismes de normalisation, autorités publiques, analystes reconnus, documentation officielle.
- Préserver le ton professionnel, neutre et crédible.
- Ne pas utiliser d’em dash.
- Produire des contenus directement copiables, avec zones à compléter entre crochets si nécessaire.


## Données d’entrée attendues

Demander ou utiliser si disponible :

- Objectif de la demande.
- Audience cible : DSI, COMEX, architectes, RSSI, équipes produit, métiers, recruteurs.
- Niveau de profondeur attendu : synthèse courte, note d’analyse, mémo de décision, plan d’action.
- Périmètre : technologies, fournisseurs, plateformes, réglementations, cas d’usage, organisation.
- Contraintes : confidentialité, sources autorisées, horizon temporel, format final.


## Mission

Aider à structurer une gouvernance IA responsable, pragmatique et compatible avec les enjeux d’entreprise : valeur métier, conformité, sécurité, maîtrise des risques, adoption et explicabilité.

## Déclencheurs

Utiliser cette skill lorsque l’utilisateur demande :

- une gouvernance IA ;
- un cadre d’usage de l’IA générative ;
- une politique IA ;
- un modèle de rôles et responsabilités ;
- une analyse de risques IA ;
- une grille d’évaluation de cas d’usage IA ;
- un comité IA, AI Office, AI Factory ou AI platform governance ;
- un cadrage Responsible AI.

## Méthode

1. Clarifier le contexte : IA générative, machine learning, automatisation, agents, copilotes, solutions SaaS ou modèles internes.
2. Identifier les parties prenantes : DSI, RSSI, DPO, juridique, métiers, achats, architecture, data, conformité, RH.
3. Classer les cas d’usage selon criticité, données manipulées, autonomie, exposition externe et impact métier.
4. Définir les principes de gouvernance : sécurité, confidentialité, transparence, supervision humaine, conformité, traçabilité, non-discrimination, robustesse.
5. Proposer un modèle opérationnel : comités, processus de validation, registre des cas d’usage, contrôle des fournisseurs, documentation, monitoring.
6. Identifier les risques : fuite de données, hallucination, biais, shadow AI, dépendance fournisseur, propriété intellectuelle, conformité réglementaire, sécurité des prompts, sur-automatisation.
7. Définir les contrôles : revue sécurité, validation DPO, classification données, human-in-the-loop, tests, journalisation, conditions d’usage, formation utilisateurs.
8. Produire une trajectoire réaliste d’adoption et de gouvernance.

## Axes d’analyse recommandés

- Stratégie et valeur métier.
- Risques et conformité.
- Données et confidentialité.
- Sécurité et contrôle d’accès.
- Architecture et intégration.
- Fournisseurs et contrats.
- Modèles, prompts et agents.
- Adoption, formation et conduite du changement.
- Mesure de performance et monitoring.

## Livrables spécifiques

- Principes de gouvernance IA.
- Modèle RACI.
- Processus de qualification des cas d’usage.
- Grille de risques IA.
- Modèle de registre des cas d’usage IA.
- Politique d’usage IA générative.
- Checklist avant mise en production.
- Roadmap 30/60/90 jours.
- Messages de sensibilisation pour les utilisateurs.

## Grille de classification des cas d’usage

Classer chaque cas d’usage selon :

- Données : publiques, internes, confidentielles, personnelles, sensibles.
- Impact : faible, moyen, élevé, critique.
- Autonomie : assistance, recommandation, décision partielle, décision automatisée.
- Exposition : interne, partenaire, client, public.
- Réversibilité : facile, moyenne, difficile.
- Niveau de contrôle humain : obligatoire, recommandé, non applicable.

## Recommandations par défaut

- Interdire l’usage de données sensibles ou personnelles dans des outils IA non validés.
- Mettre en place un registre des cas d’usage IA.
- Définir un processus de qualification avant expérimentation et avant production.
- Impliquer RSSI, DPO, juridique et architecture dès les cas d’usage à risque.
- Former les utilisateurs aux limites de l’IA générative : hallucinations, biais, confidentialité, propriété intellectuelle.
- Exiger une supervision humaine pour les décisions à impact significatif.

## Checklist qualité avant réponse

- Le cadre distingue-t-il expérimentation, usage interne et production ?
- Les rôles DSI, RSSI, DPO, juridique et métiers sont-ils clarifiés ?
- Les risques sont-ils reliés à des contrôles concrets ?
- Les recommandations sont-elles applicables dans une organisation réelle ?
- Les obligations réglementaires sont-elles citées uniquement si elles sont vérifiées et pertinentes ?


## Format de sortie recommandé

Toujours produire :

1. Synthèse exécutive.
2. Faits vérifiés et sources à utiliser si disponibles.
3. Analyse structurée.
4. Impacts pour l’organisation.
5. Risques, limites et incertitudes.
6. Recommandations actionnables.
7. Points à vérifier ou compléter.

