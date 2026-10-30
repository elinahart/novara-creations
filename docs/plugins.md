# Créer un plugin NOVARA

Un plugin ajoute à NOVARA :

- des **thèmes** (fichiers `.novaratheme`, ceux qu'exporte Réglages › Apparence › Mes thèmes) ;
- des **modèles de jeu** : des dossiers de départ, copiés dans un nouveau projet quand on le choisit
  dans la fenêtre « Nouveau projet » ;
- des **guides pour les agents** : des fichiers Markdown que Claude Code, Codex et Gemini CLI
  trouvent dans chaque projet (`.novara/guides/plugins/`).

Un plugin ne contient **que des fichiers** : aucun programme de NOVARA ne s'y exécute. NOVARA le
vérifie avant de l'installer (voir « Ce que NOVARA vérifie »).

Un exemple complet est dans [`plugins/exemple-novara`](../plugins/exemple-novara).

## Structure

```
mon-plugin/
├── plugin.json
├── themes/
│   └── mon-theme.novaratheme
├── modeles/
│   └── mon-jeu/
│       ├── index.html
│       └── jeu.js
└── guides/
    └── conseils.md
```

## plugin.json

```json
{
  "id": "mon-plugin",
  "name": "Mon plugin",
  "version": "1.0.0",
  "author": "Ton nom",
  "description": "Ce que le plugin apporte, en une ou deux phrases.",
  "themes": ["themes/mon-theme.novaratheme"],
  "templates": [
    {
      "name": "Mon jeu",
      "path": "modeles/mon-jeu",
      "engine": "web2d",
      "description": "Ce que contient ce modèle de jeu."
    }
  ],
  "guides": ["guides/conseils.md"]
}
```

| Champ | Obligatoire | Règle |
|---|---|---|
| `id` | oui | 1 à 48 caractères : minuscules, chiffres et tirets. Unique : une nouvelle version remplace l'ancienne. |
| `name` | oui | 60 caractères au plus. |
| `version` | oui | 20 caractères au plus (par exemple `1.2.0`). |
| `author`, `description` | non | 60 et 400 caractères au plus. |
| `themes` | non | Chemins de fichiers `.novaratheme` dans le plugin. |
| `templates` | non | `name`, `path` (un dossier du plugin), `engine` (le moteur visé : `web2d`, `roblox`, `unity`… ou vide pour tous), `description`. |
| `guides` | non | Chemins de fichiers `.md` dans le plugin. |

Il faut au moins un thème, un modèle de jeu ou un guide.

## Les thèmes

Le plus simple : crée ton thème dans NOVARA (Réglages › Apparence › Mes thèmes › Créer un thème
avec l'IA), puis « Exporter ». Le fichier `.novaratheme` contient ses couleurs et ses choix ; NOVARA
redessine la ville et les fonds d'écran chez la personne qui installe le plugin. Les thèmes qui
utilisent des sprites trouvés en ligne sont **privés** : leur export ne contient pas ces sprites.

## Les modèles de jeu

Tout le contenu du dossier est copié dans le nouveau projet, puis NOVARA ajoute ses propres
fichiers (AGENTS.md, `.novara/`). Mets-y un jeu qui fonctionne déjà, même petit : les agents
partiront de là.

## Les guides

Un guide est un fichier Markdown court et concret (conventions, style, pièges à éviter). Il est
recopié dans chaque projet ; le résumé que les agents lisent en premier leur indique qu'il existe.

## Ce que NOVARA vérifie

- `plugin.json` lisible, champs dans les limites ci-dessus ;
- chaque chemin reste **dans** le dossier du plugin (pas de `..`, pas de chemin absolu) ;
- aucun lien symbolique ; 2 000 fichiers et 200 Mo au plus ;
- chaque thème est vérifié comme un thème exporté (couleurs `#rrggbb`, choix dans des listes connues).

## Installer, tester, retirer

Réglages › Plugins › « Installer un plugin… », puis choisis le dossier qui contient `plugin.json`.
Le plugin est copié dans NOVARA ; tu peux modifier ton dossier et réinstaller pour le mettre à
jour. « Retirer » enlève ses modèles de jeu et ses guides ; les thèmes déjà ajoutés restent dans
Mes thèmes et les projets ne changent pas.

## Partager ton plugin

Ajoute son dossier dans `plugins/<id>/` de ce dépôt et ouvre une pull request (voir le README).
Il sera vérifié automatiquement, puis relu, avant d'apparaître dans **Réglages › Créations**.
