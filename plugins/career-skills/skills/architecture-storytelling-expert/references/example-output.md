# Exemple de sortie

Exemple fictif produit à des fins d’illustration. Les données ne correspondent à aucune personne ni organisation réelle.

## Récit structuré

### Contexte

Une entreprise de 5 000 personnes faisait transiter les échanges de 40 applications par un ESB installé douze ans plus tôt. Le produit n’était plus supporté par l’éditeur, les compétences internes reposaient sur deux personnes, et l’exploitation comptait 12 incidents majeurs par an. Arrêter le socle n’était pas une option, le remplacer non plus sans réponse à une question simple, comment le faire sans interrompre le service.

### Contrainte structurante

Aucune fenêtre d’arrêt supérieure à quatre heures n’était acceptable pour 12 des 40 applications. Cette contrainte a déterminé toute la trajectoire.

### Décision et alternatives écartées

| Option | Avantage | Raison de l’écarter ou de la retenir |
| --- | --- | --- |
| Bascule unique | 4 mois plus courte, moins coûteuse | Écartée, expose 40 applications sur une même fenêtre |
| Réécriture des flux applicatifs | Supprime la dépendance au socle | Écartée, charge applicative hors de portée du programme |
| Migration par vagues avec double run | Préserve la continuité | Retenue malgré un surcoût d’exploitation de 6 mois |

### Compromis assumé

Le double run a allongé le programme de quatre mois et alourdi l’exploitation pendant six. Ce coût a été chiffré et validé comme ligne budgétaire dédiée avant le démarrage, précisément pour qu’il ne soit pas remis en cause au premier arbitrage.

### Ce qui n’a pas fonctionné

Le modèle de gouvernance des API défini en amont n’a pas survécu à la deuxième vague. Il supposait une validation centrale de chaque exposition, incompatible avec le rythme des équipes produit. Il a été refait au bout de cinq mois, en déléguant la validation aux équipes avec un contrôle a posteriori.

### Résultats

| Indicateur | Avant | Après |
| --- | --- | --- |
| Incidents majeurs par an | 12 | 3 |
| Délai de mise à disposition d’une API | 6 semaines | 5 jours |
| Applications sur le socle historique | 40 | 0 |

### Valeur pour l’organisation

La disponibilité des échanges n’est plus dépendante de deux personnes ni d’un produit non supporté. Le délai de mise à disposition d’une API est passé d’un obstacle de planning à un délai absorbable dans un sprint.

## Version courte pour un public non technique, 90 mots

```text
Nos échanges entre applications passaient par un système central installé
douze ans plus tôt, que l'éditeur ne supportait plus, et qui provoquait
une douzaine de pannes majeures par an.

Nous l'avons remplacé progressivement, application par application, en faisant
fonctionner l'ancien et le nouveau système en parallèle pendant six mois.
Ce parallèle a coûté cher et nous l'avons assumé.

Résultat, trois pannes majeures par an au lieu de douze, et un délai
de mise à disposition ramené de six semaines à cinq jours.
```

## Points à vérifier ou compléter

- Autorisation de citer le secteur et la taille de l’organisation, `[à compléter]`.
- Coût du double run si le chiffre doit être communiqué, `[à compléter]`.
- Part de la contribution personnelle par rapport à l’équipe, à préciser selon le support.
