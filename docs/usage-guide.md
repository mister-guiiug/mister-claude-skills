# Guide d’usage

## En cas de doute

Passer par `career-skills-router`. Il pose deux questions au maximum, identifie l’objectif réel et propose l’enchaînement adapté.

## Choisir la bonne skill

| Besoin | Skill |
| --- | --- |
| Je ne sais pas par où commencer | `career-skills-router` |
| Audit complet du profil depuis son export PDF | `linkedin-pdf-profile-audit` |
| Profil LinkedIn, une section précise | `linkedin-profile-optimizer` |
| Photo de profil et bannière LinkedIn | `linkedin-profile-photo-prompt` |
| Positionnement senior | `executive-personal-branding` |
| Réalisations et preuves d’impact | `achievement-extractor` |
| CV | `cv-optimizer` |
| Relecture recruteur | `recruiter-perspective-reviewer` |
| Préparation d’entretien | `interview-preparation` |
| Salaire, package, contre-offre | `salary-negotiation` |
| Message de mise en relation ou relance | `networking-outreach` |
| Idées et angles de posts | `thought-leadership-generator` |
| Rédaction finale d’un contenu | `executive-content-writer` |
| Récit de projet d’architecture | `architecture-storytelling-expert` |
| Réponse à un appel à conférenciers | `call-for-papers-responder` |
| Préparation d’un talk | `conference-speaker-coach` |
| Évolution de carrière architecte | `it-architect-career-advisor` |
| Veille technologique | `technology-watch` |
| Gouvernance IA | `ai-governance` |

## Enchaînements utiles

| Objectif | Enchaînement de skills |
| --- | --- |
| Recherche de poste complète | `achievement-extractor`, `cv-optimizer`, `linkedin-profile-optimizer`, `recruiter-perspective-reviewer`, `interview-preparation`, `salary-negotiation` |
| Refonte du profil LinkedIn | `achievement-extractor`, `linkedin-profile-optimizer`, `linkedin-profile-photo-prompt`, `recruiter-perspective-reviewer` |
| Gagner en visibilité experte | `executive-personal-branding`, `technology-watch`, `thought-leadership-generator`, `executive-content-writer` |
| Prise de parole publique | `call-for-papers-responder`, `conference-speaker-coach`, `architecture-storytelling-expert` |
| Approche directe d’une entreprise | `networking-outreach`, `achievement-extractor`, `interview-preparation` |
| Cadrer une pratique interne | `technology-watch`, `ai-governance` |

## Règles de désambiguïsation

- `linkedin-pdf-profile-audit` diagnostique tout le profil et priorise, `linkedin-profile-optimizer` réécrit une section une fois la priorité connue.
- `achievement-extractor` produit la matière, `cv-optimizer` et `linkedin-profile-optimizer` la mettent en forme.
- `thought-leadership-generator` produit les angles, `executive-content-writer` rédige le texte final.
- `call-for-papers-responder` traite la candidature à un événement, `conference-speaker-coach` traite la préparation du talk retenu.
- `executive-personal-branding` définit le positionnement, les autres skills le déclinent sur un support.
- `it-architect-career-advisor` traite la trajectoire, `interview-preparation` et `salary-negotiation` traitent une opportunité identifiée.

## Étudier et lancer une activité, plugin business-team

| Besoin | Agent ou skill |
| --- | --- |
| Faits sur le marché, les concurrents, les prix publics, avec sources | `enqueteur` |
| Vérifier un brainstorm ou une étude faits avec une autre IA | `enqueteur` |
| Prix de vente, marge, seuil de rentabilité, scénarios, sensibilité | `comptable` |
| Tout ce qui peut faire échouer le projet | `avocat-du-diable` |
| Parades, tests, critères d’arrêt, verdict sur un dossier réuni | `stratege` |
| Fiche produit, post, newsletter, page de test de la demande | `redacteur` |
| Dois-je démarrer, renforcer ou abandonner cette activité ? | `etude-opportunite` |
| C’est décidé, préparer prix, fiche produit, posts et risques | `lancement-produit` |

| Objectif | Enchaînement |
| --- | --- |
| De l’idée au lancement | `etude-opportunite`, puis si le verdict le permet et après les tests, `lancement-produit` |

- Un agent sollicité hors de son métier le dit et ne livre que sa partie. Pour une tâche, appeler l’agent ; pour un dossier complet, une skill.
- `etude-opportunite` traite un brainstorm comme une liste d’hypothèses : l’enregistrer dans un fichier et le citer avec `@fichier`. Donner aussi ses critères de décision (budget, temps, revenu visé), sans eux le Stratège ne peut pas trancher pour toi.
- `redacteur` n’invente aucun chiffre : lui donner les résultats de `enqueteur` et le prix du `comptable`.
- `avocat-du-diable` ne propose pas de solution, c’est voulu. Les parades viennent du `stratege`.
- `business-team` ne recoupe pas `career-skills` : `executive-content-writer` rédige un contenu professionnel au ton sobre, `redacteur` une fiche produit ou un post commercial au tutoiement.

## Bonnes pratiques

1. Fournir des faits bruts, y compris ce qui n’a pas fonctionné.
2. Indiquer l’audience cible.
3. Préciser le niveau de confidentialité et ce qui est publiable.
4. Demander une version courte et une version détaillée.
5. Relire les chiffres, dates et responsabilités avant publication.
6. Consulter le fichier `references/example-output.md` de la skill pour voir le niveau de détail attendu.
