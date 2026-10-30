# Créations NOVARA

Les thèmes et les plugins partagés par la communauté de **NOVARA**, l'espace de travail pour
créer des jeux avec des agents IA (Claude Code, Codex, Gemini CLI).

NOVARA lit ce dépôt : tout ce qui est ici apparaît dans l'app, dans **Réglages › Créations**, et
s'installe en un clic.

## Installer une création

Dans NOVARA : **Réglages › Créations**, choisis un thème ou un plugin, puis « Installer ».
- Un thème rejoint **Réglages › Apparence › Mes thèmes** : NOVARA dessine sa ville et ses fonds
  d'écran sur ton ordinateur.
- Un plugin rejoint **Réglages › Plugins** : ses modèles de jeu apparaissent dans « Nouveau
  projet », ses guides sont lus par tes agents.

Tu peux aussi installer un plugin à la main : télécharge son dossier, puis **Réglages › Plugins ›
Installer un plugin…**.

## Créer

- **Un thème** : dans NOVARA, Réglages › Apparence › Mes thèmes › « Créer un thème avec l'IA »,
  puis « Exporter ». Le format est décrit dans [docs/themes.md](docs/themes.md).
- **Un plugin** (thèmes, modèles de jeu, guides pour les agents) : [docs/plugins.md](docs/plugins.md),
  avec un exemple complet dans [plugins/exemple-novara](plugins/exemple-novara).

## Partager

- **Depuis NOVARA** : sur un de tes thèmes, « Partager ». NOVARA ouvre GitHub dans ton navigateur
  avec le fichier prêt ; connecte-toi à ton compte GitHub et propose-le (« Propose changes »).
- **À la main** : fais un fork de ce dépôt, ajoute ton thème dans `themes/` ou ton plugin dans
  `plugins/<id>/`, puis ouvre une pull request.

Chaque proposition est vérifiée automatiquement (`scripts/index.py`), puis relue avant d'être
ajoutée. Ne partage que ce que tu as fait toi-même : un thème qui utilise des sprites trouvés en
ligne reste privé, son export ne les contient pas.

## Licence

Les créations de ce dépôt sont partagées sous licence
[Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr) : tu peux les
utiliser et les modifier en citant leur auteur. En proposant une création, tu acceptes de la
partager ainsi. NOVARA lui-même n'est pas dans ce dépôt.
