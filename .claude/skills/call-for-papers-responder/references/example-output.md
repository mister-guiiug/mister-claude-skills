# Exemple de sortie

Exemple fictif produit à des fins d’illustration. L’événement, les critères et le contenu ne correspondent à aucun appel réel.

## Analyse de l’appel

- Audience : architectes et responsables plateforme, niveau intermédiaire à avancé.
- Format : session de 40 minutes, 5 minutes de questions incluses.
- Critères publiés : retour d’expérience réel, contenu non promotionnel, enseignements transposables.
- Critère implicite déduit : le comité privilégie les sessions qui exposent ce qui a échoué.
- Limites du formulaire : titre 80 caractères, abstract 1200 caractères, bio 400 caractères.

## Angle retenu

Le décommissionnement d’un ESB par vagues, avec le coût réel du double run. Angle étroit, appuyé sur un programme vécu, et qui expose un arbitrage discutable plutôt qu’une réussite lisse.

Angles écartés : panorama de l’API management, trop large et déjà couvert. Comparatif de plateformes, perçu comme promotionnel.

## Titre, 3 propositions

Sobre, 62 caractères :

```text
Décommissionner un ESB par vagues, ce que le double run a coûté
```

Orienté bénéfice, 71 caractères :

```text
Migrer 40 applications sans interruption, les arbitrages qui ont compté
```

Orienté problème, 58 caractères :

```text
Six mois de double run, deux de trop, retour d'expérience
```

## Abstract, 1147 caractères sur 1200

```text
Notre ESB supportait 40 applications et générait 12 incidents majeurs par an.
Le remplacer n'était pas discutable, la façon de le faire l'était.

Nous avons écarté la bascule unique, plus courte et moins coûteuse, au profit
d'une migration par vagues avec double run. Ce choix a préservé la continuité
de service, il a aussi allongé le programme de quatre mois et alourdi
l'exploitation pendant six mois.

Dans cette session, je détaille les trois arbitrages qui ont réellement pesé,
le découpage des vagues, la durée du double run et le moment où la gouvernance
des API a dû être revue. Je montre les mesures avant et après, incidents majeurs
et délai de mise à disposition d'une API, et j'explique ce que je referais
différemment, en particulier sur la durée du double run.

La session s'adresse aux architectes et responsables de plateforme confrontés
à un socle historique. Vous repartirez avec une grille de décision entre bascule
unique et migration progressive, et avec les indicateurs à instrumenter avant
de démarrer.
```

## Plan détaillé minuté

| Durée | Contenu |
| --- | --- |
| 5 min | Contexte, socle, incidents, contrainte de continuité |
| 8 min | L’arbitrage bascule unique contre migration par vagues |
| 10 min | Découpage des vagues et instrumentation |
| 7 min | Le coût réel du double run, mesures à l’appui |
| 5 min | Ce que je referais différemment |
| 5 min | Questions |

## Biographie, 312 caractères

```text
Architecte IT, spécialisé sur les plateformes d'intégration et le décommissionnement
de socles historiques en grande entreprise. Douze ans à conduire des migrations
sous contrainte de continuité de service. Intervient sur la gouvernance des API
et la dette d'intégration.
```

## Risques de refus identifiés et corrections

| Risque | Correction appliquée |
| --- | --- |
| Sujet trop large | Angle recentré sur le seul arbitrage du double run |
| Perception promotionnelle | Aucun nom de plateforme dans le titre ni dans l’abstract |
| Absence d’enseignement | Section explicite sur ce qui serait refait différemment |
| Niveau incohérent | Prérequis annoncés, connaissance des architectures d’intégration |

## Points à vérifier ou compléter

- Autorisation employeur de présenter ce retour d’expérience, `[à compléter]`.
- Disponibilité aux dates de l’événement, `[à compléter]`.
- Enregistrement d’une session passée à joindre, `[à compléter]`.
