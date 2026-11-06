# Exemple de sortie

Exemple fictif produit à des fins d’illustration. Les données, prix et sources ne correspondent à aucune entreprise ni page réelle. Il montre le niveau de détail attendu, pas un contenu à réutiliser.

## Entrée fournie par l’utilisateur

```text
Je veux vendre une gourde isotherme en inox 500 ml sur mon site, en France.
Coût d'achat 6,40 € HT, livraison 4,90 €, emballage 0,60 €.
Il me faut une fiche produit et un post Instagram.
```

## Sortie attendue

### Résumé

- Produit : gourde isotherme inox 500 ml, vente en ligne en France.
- Prix proposé : 29,90 € TTC.
- Risque le plus grave : frais de livraison qui absorbent la marge sur une commande d’une seule gourde.

### Recherche, par l’Enquêteur

1. Trois concurrents vendent une gourde inox 500 ml entre 24,90 € et 34,90 € TTC, [Exemple de page](https://exemple.invalid/a), date non indiquée.
2. Le contact alimentaire impose une déclaration de conformité du fournisseur, [Exemple de page](https://exemple.invalid/b), 2026-03-12.

### Chiffres, par le Comptable

| Poste | Montant (€) | % du prix HT |
|---|---:|---:|
| Prix de vente HT | 24,92 | 100,0 |
| Coût de revient | 11,90 | 47,8 |
| Marge brute | 13,02 | 52,2 |

- Prix HT = 29,90 / 1,20
- Marge brute = Prix HT - Coût de revient
- Hypothèse : TVA à 20 %, livraison offerte au client.

### Textes, par le Rédacteur

```text
Ta boisson reste fraîche. Toute la journée.
Inox double paroi. 500 ml. Zéro goût de plastique.
Tu la glisses dans ton sac. Elle ne fuit pas.
29,90 €. Commande-la maintenant.
```

### Risques, par l’Avocat du diable

1. **Livraison qui mange la marge**, gravité élevée. Ce qui se passe : 4,90 € sur 13,02 € de marge. Pourquoi c’est probable : une gourde se commande à l’unité.
2. **Conformité non prouvée**, gravité critique. Ce qui se passe : retrait du produit. Pourquoi c’est probable : aucune déclaration fournisseur n’est citée.

## Contrôles appliqués

| Point | Statut |
| --- | --- |
| Prix identique entre tableau et texte | 29,90 € des deux côtés |
| Faits sourcés | 2 sur 2 |
| Risques sans solution proposée | oui |

## À compléter

- Déclaration de conformité contact alimentaire du fournisseur, `[à compléter]`.
- Durée de maintien en température, à fournir avant de la citer dans la fiche, `[à compléter]`.
