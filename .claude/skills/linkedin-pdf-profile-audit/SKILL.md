---
name: linkedin-pdf-profile-audit
version: 1.1.1
updated: 2026-08-03
description: Audite un profil LinkedIn à partir de son export PDF, le sien ou celui d’un tiers, section par section, avec diagnostic priorisé et reformulations prêtes à coller. Utiliser quand l’utilisateur fournit un PDF exporté depuis LinkedIn, un fichier Profile.pdf, demande un audit complet de profil, évalue une candidature, accompagne quelqu’un sur son profil ou compare plusieurs profils.
---

# LinkedIn PDF Profile Audit

## Principes non négociables

- Ne jamais inventer une expérience, une date, un diplôme, une certification, un chiffre ou un employeur absent du PDF.
- Ne jamais compléter un trou de parcours par une hypothèse. Le signaler et poser la question.
- Ne jamais conclure à l’absence d’une section avant d’avoir vérifié que l’extraction du PDF est complète.
- Distinguer ce que l’export ne contient jamais de ce qui est absent parce que la section est vide sur le profil. Les deux ne se traitent pas de la même façon.
- Adapter le livrable à la personne auditée et à l’objectif, voir la section sur les personas.
- Distinguer le constat, l’hypothèse et la proposition de reformulation.
- Neutraliser les informations internes, clients et projets dans toute reformulation destinée à une diffusion publique.
- Ne pas utiliser d’em dash.
- Toute reformulation doit être directement copiable et reposer uniquement sur des faits présents dans le PDF ou fournis par l’utilisateur.

## Données d’entrée attendues

Demander ou utiliser si disponible :

- L’export PDF du profil. Le lire intégralement, page par page si nécessaire.
- Qui est audité et dans quel but. C’est la première question, elle change le livrable.
- Rôle cible et audience visée. Sans eux, l’audit reste générique et sa valeur chute.
- 3 à 5 offres d’emploi cibles, pour calibrer le vocabulaire et les mots-clés.
- Langue du profil et langue visée, un profil en français pour un marché international se traite différemment.
- Éléments jamais présents dans l’export, listés plus bas.
- Contraintes de confidentialité, employeur actuel informé ou non de la démarche.

## Mission

Produire un audit complet et priorisé d’un profil LinkedIn à partir de son export PDF, avec un livrable adapté à celui qui le demande et à ce qu’il compte en faire.

## Déclencheurs

Utiliser cette skill lorsque l’utilisateur :

- fournit un PDF exporté depuis LinkedIn ;
- demande un audit ou un bilan complet d’un profil ;
- évalue une candidature à partir de son profil ;
- accompagne quelqu’un sur son profil, en coaching, en management ou en formation ;
- compare plusieurs profils ;
- veut une vision d’ensemble avant de retravailler une section précise.

## Personas et adaptation du livrable

Le même audit ne sert pas le même objectif. Identifier le cas avant de produire.

| Cas | Qui demande | Livrable attendu |
| --- | --- | --- |
| Auto-audit | La personne elle-même | Constats, reformulations prêtes à coller, plan d’action personnel |
| Accompagnement | Coach, manager, formateur, proche | Constats et reformulations formulés comme des propositions à transmettre, avec le pourquoi de chaque conseil |
| Évaluation de candidature | Recruteur, hiring manager | Lecture d’évaluation, forces, zones à creuser en entretien, questions à poser. **Aucune reformulation**, le rôle n’est pas de réécrire le profil d’un candidat |
| Comparaison | Recruteur, chargé de sourcing, benchmark | Grille commune appliquée à chaque profil, puis tableau comparatif et écarts |

Si le persona n’est pas déclaré, ne pas bloquer. Appliquer la règle de repli suivante :

1. Retenir `Accompagnement` par défaut, c’est le cas le plus complet et le moins risqué sur un profil tiers.
2. L’annoncer explicitement en tête de réponse, avec les autres cas possibles.
3. Indiquer en une ligne ce que le livrable deviendrait en évaluation de candidature, pour que l’utilisateur puisse corriger d’un mot.

Ne jamais retenir `Auto-audit` par défaut. Rien ne permet de supposer que le profil est celui de l’utilisateur.

Règles associées :

- En évaluation de candidature, ne pas produire de jugement sur la personne, seulement sur ce que le document démontre ou ne démontre pas.
- En évaluation de candidature, ne jamais déduire d’un trou de parcours une explication personnelle. Le formuler en question d’entretien.
- En accompagnement, rappeler que les reformulations doivent être validées par la personne concernée avant publication.
- Dans tous les cas, l’audit reste privé. Ne pas produire de contenu destiné à être diffusé publiquement sur un tiers.

## Structure de l’export, format fixe

L’export LinkedIn suit toujours la même mise en page, en deux zones. Cette régularité permet de vérifier une extraction et de conclure de façon fiable.

**Zone 1, colonne latérale sur fond sombre, partie gauche**

| Bloc | Libellé français | Libellé anglais |
| --- | --- | --- |
| Contact | Coordonnées | Contact |
| Compétences | Principales compétences | Top Skills |
| Langues | Langues | Languages |
| Certifications | Certifications | Certifications |
| Publications | Publications | Publications |
| Distinctions | Distinctions | Honors-Awards |

**Zone 2, colonne principale, partie droite**

| Bloc | Libellé français | Libellé anglais |
| --- | --- | --- |
| Identité | Nom, titre, localisation | Nom, titre, localisation |
| Résumé | Résumé | Summary |
| Expériences | Expérience | Experience |
| Formation | Formation | Education |
| Pied de page | Page X sur Y | Page X of Y |

Deux règles de lecture qui découlent du format fixe :

1. **Un bloc n’apparaît que s’il contient quelque chose.** L’absence du bloc `Résumé` dans une extraction complète signifie que la section est vide sur le profil, pas qu’elle a échappé à la lecture. Même raisonnement pour `Certifications`, `Langues`, `Publications` et `Distinctions`.
2. **L’ordre des blocs est stable.** Le `Résumé` se situe entre la localisation et `Expérience`. Si l’extraction passe de la localisation à `Expérience`, la conclusion d’absence est fiable.

## Contrôle de complétude de l’extraction

À faire avant tout constat d’absence.

1. Vérifier que le nom, le titre et la localisation ont été lus. S’ils manquent, l’extraction a échoué, pas le profil.
2. Vérifier que les deux zones ont produit du texte. Une seule zone lue signale une extraction en une colonne, qui mélange l’ordre.
3. Vérifier le pied de page `Page X sur Y` et lire toutes les pages annoncées.
4. Vérifier que chaque expérience comporte au minimum une entreprise, un intitulé et des dates. Une expérience réduite à une entreprise signale une lecture partielle.
5. Si l’extraction directe échoue, une extraction positionnée conservant les coordonnées x et y permet de reconstituer les deux colonnes. Les polices de l’export sont des sous-ensembles à identifiants de glyphes, une table de correspondance vers unicode est nécessaire.

Ne jamais conclure sur une absence tant que ces cinq points ne sont pas vérifiés.

## Ce que l’export ne contient jamais

Ces éléments ne figurent dans aucun export, quel que soit le profil. Leur absence ne dit rien. Les demander.

| Élément | Conséquence sur l’audit |
| --- | --- |
| Photo de profil et bannière | Orienter vers `linkedin-profile-photo-prompt` |
| Section Sélection ou Featured | Impossible de savoir si des preuves sont mises en avant |
| Recommandations reçues et données | Preuve sociale non évaluable |
| Activité, publications LinkedIn, commentaires | Visibilité et régularité non évaluables |
| Compétences au delà des principales affichées | Couverture réelle des mots-clés non évaluable |
| Validations de compétences | Crédibilité des compétences déclarées non évaluable |
| Mention Open to work, paramètres de visibilité | Efficacité du profil non évaluable |

L’URL du profil, elle, figure dans le bloc `Coordonnées`. Une URL avec suffixe numérique ou caractère accentué est un constat, pas une question.

## Délimitation avec les autres skills

- Cette skill fait l’inventaire et le diagnostic de l’ensemble du profil, puis priorise.
- `linkedin-profile-optimizer` travaille en profondeur une section fournie en texte, une fois la priorité connue.
- `recruiter-perspective-reviewer` simule le tri d’un recruteur sur un document donné, sans structure d’export.
- `achievement-extractor` produit la matière chiffrée qui manque quand l’audit révèle des expériences sans preuve.

En fin d’audit, orienter vers la skill adaptée à la première priorité.

## Méthode

1. Identifier le persona et l’objectif. Le livrable en dépend. S’ils ne sont pas déclarés, appliquer la règle de repli et l’annoncer.
2. Lire le PDF intégralement et contrôler la complétude de l’extraction.
3. Produire l’inventaire des blocs présents et absents, en appliquant les deux règles de lecture du format fixe.
4. Reconstituer la chronologie et repérer les trous, les chevauchements et les incohérences de dates.
5. Auditer chaque section présente selon la grille ci-dessous.
6. Vérifier la cohérence transverse, le titre annonce-t-il ce que les expériences démontrent.
7. Confronter au rôle cible et aux offres si elles sont fournies.
8. Prioriser par effet sur la décision du lecteur, pas par ordre d’apparition dans le PDF.
9. Produire le livrable correspondant au persona.
10. Lister les questions ouvertes et orienter vers la skill suivante.

## Grille d’audit par section

| Section | Ce qui est contrôlé | Défauts fréquents |
| --- | --- | --- |
| Titre | Métier, spécialité et séniorité identifiables seuls | Intitulé interne non compris à l’extérieur, liste de mots-clés sans phrase, titre vide |
| Résumé | Première phrase autonome, promesse claire, preuves | Ouverture générique, paragraphe unique compact, aucun chiffre, section absente |
| Expériences | Une ligne de contexte, des décisions, des résultats mesurés | Description vide, verbes de présence, aucun périmètre, copie de fiche de poste |
| Intitulés de poste | Compréhensibles hors de l’entreprise | Intitulés internes, noms de service, niveaux maison, acronymes |
| Dates | Continuité, cohérence, durées lisibles | Trous non expliqués, chevauchements, absence de poste en cours |
| Formation | Diplôme, établissement, année | Chevauchement avec un poste non expliqué, formations obsolètes au même niveau que le diplôme principal |
| Certifications | Pertinence par rapport au rôle cible, validité | Certifications expirées, sans date, sans organisme |
| Compétences | Correspondance avec les expériences décrites | Compétences déclarées sans aucune trace dans le parcours |
| Langues | Niveau exprimé sur une échelle explicite | Auto-évaluation floue, notion sans référentiel |
| Publications et distinctions | Cohérence avec le positionnement | Contenu sans lien avec le métier, laissé par défaut |
| Coordonnées | Cohérence et professionnalisme | URL par défaut avec suffixe numérique, caractère accentué dans l’URL, adresse électronique inadaptée |
| Cohérence entre blocs | Ce qu’un bloc affirme se retrouve dans les blocs prévus pour cela | Voir la table dédiée ci-dessous |

## Contrôles de cohérence entre blocs

Un défaut fréquent n’apparaît dans aucun bloc pris isolément, il naît de la contradiction entre deux blocs. À contrôler systématiquement.

| Ce qui est affirmé | Où cela devrait se retrouver | Constat si absent |
| --- | --- | --- |
| Une langue citée dans `Principales compétences` | Bloc `Langues`, avec un niveau | La langue n’est pas indexée comme telle, les filtres recruteur ne la voient pas |
| Un outil cité dans `Principales compétences` | Une description d’expérience | Compétence déclarée sans preuve |
| Une certification citée dans une expérience | Bloc `Certifications` | Certification non valorisée là où elle est cherchée |
| Un domaine annoncé dans le titre ou le résumé | Les expériences décrites | Le profil promet ce qu’il ne démontre pas |
| Une formation chevauchant un emploi | Le résumé ou la description du poste | Alternance probable non déclarée, un atout perdu |
| Une publication ou une distinction | Le positionnement annoncé | Contenu laissé par défaut, sans lien avec le métier |

Ces contrôles sont peu coûteux et produisent souvent des corrections de deux minutes.

## Grille de priorisation

Classer chaque constat selon deux axes, l’effet sur la décision du lecteur et l’effort de correction.

| Priorité | Définition |
| --- | --- |
| P1 | Bloque la compréhension du profil ou la décision, correction rapide |
| P2 | Affaiblit fortement la crédibilité, correction rapide |
| P3 | Améliore nettement, effort important |
| P4 | Confort, à traiter en dernier |

Annoncer les P1 en premier et limiter leur nombre à cinq. Un audit qui liste trente points ne produit aucune action.

## Livrables spécifiques

Communs à tous les personas :

- Contrôle de complétude de l’extraction.
- Inventaire des blocs présents et absents, avec la distinction vide contre non exporté.
- Chronologie reconstituée avec les trous et chevauchements signalés.
- Diagnostic par section, avec citation de l’élément concerné.
- Constats classés P1 à P4.
- Questions ouvertes.

Selon le persona :

- Auto-audit et accompagnement : reformulations en avant et après pour les P1 et P2, plan de correction séquencé, orientation vers la skill suivante.
- Évaluation de candidature : forces démontrées, zones non démontrées, questions à poser en entretien.
- Comparaison : grille commune et tableau comparatif.

## Format de sortie recommandé

Toujours produire :

1. Persona et objectif retenus.
2. Contrôle de complétude, puis ce que l’export ne contient jamais.
3. Inventaire et chronologie.
4. Constats classés par priorité, avec citation de l’élément concerné.
5. Le livrable propre au persona.
6. Questions ouvertes et informations manquantes.
7. Orientation vers la skill adaptée à la première priorité.

## Checklist qualité avant réponse

- Le persona et l’objectif ont-ils été identifiés avant de produire, ou la règle de repli a-t-elle été annoncée ?
- Les six contrôles de cohérence entre blocs ont-ils été passés ?
- Le contrôle de complétude de l’extraction a-t-il été fait avant tout constat d’absence ?
- Les blocs vides sont-ils distingués des blocs jamais exportés ?
- Chaque constat cite-t-il l’élément précis du PDF concerné ?
- Les trous de parcours sont-ils signalés sans être interprétés ?
- En évaluation de candidature, l’analyse porte-t-elle sur le document et jamais sur la personne ?
- Les reformulations reposent-elles uniquement sur des faits présents ou fournis ?
- Le nombre de P1 reste-t-il inférieur ou égal à cinq ?
- Les informations internes et clients sont-elles neutralisées ?
- L’orientation vers la skill suivante est-elle explicite ?
