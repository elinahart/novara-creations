# NOVARA Creations

Themes and plugins shared by the community of **[NOVARA](https://github.com/elinahart/novara-releases)**,
the free app for making video games with a team of AI agents (Claude Code, Codex, Gemini CLI).

NOVARA reads this repository: everything here shows up in the app under **Settings › Creations**
and installs in one click.

*Version française plus bas.*

## Install a creation

In NOVARA: **Settings › Creations**, pick a theme or a plugin, then “Install”.
- A theme joins **Settings › Appearance › My themes**: NOVARA draws its town and wallpapers on
  your computer.
- A plugin joins **Settings › Plugins**: its game templates show up in “New project”, and your
  agents read its guides.

## Make your own

- **A theme**: in NOVARA, Settings › Appearance › My themes › “Create a theme with AI”, then
  “Export”. The format is described in [docs/themes.md](docs/themes.md).
- **A plugin** (themes, game templates, guides for the agents): [docs/plugins.md](docs/plugins.md),
  with a full example in [plugins/exemple-novara](plugins/exemple-novara).

## Share

- **From NOVARA**: on one of your themes, “Share”. NOVARA opens GitHub in your browser with the
  file ready; sign in to your GitHub account and propose it (“Propose changes”).
- **By hand**: fork this repository, add your theme to `themes/` or your plugin to
  `plugins/<id>/`, then open a pull request.
- **A preview picture** (recommended): a 16:9 PNG of 1 MB at most, next to the theme
  (`themes/my-theme.png`) or in the plugin (`plugins/<id>/apercu.png`). It is shown in NOVARA's
  shop.

Every proposal is checked automatically (`scripts/index.py`), then reviewed before it is added.
Only share what you made yourself: a theme that uses sprites found online stays private, and its
export does not contain them.

## Licence

Creations in this repository are shared under
[Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/): you may use and change
them as long as you credit their author. By proposing a creation, you agree to share it this way.
NOVARA itself is not in this repository.

---

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
- **Une image d'aperçu** (conseillée) : un PNG en 16:9 de 1 Mo au plus, à côté du thème
  (`themes/mon-theme.png`) ou dans le plugin (`plugins/<id>/apercu.png`). C'est elle qui s'affiche
  dans la boutique de NOVARA.

Chaque proposition est vérifiée automatiquement (`scripts/index.py`), puis relue avant d'être
ajoutée. Ne partage que ce que tu as fait toi-même : un thème qui utilise des sprites trouvés en
ligne reste privé, son export ne les contient pas.

## Licence

Les créations de ce dépôt sont partagées sous licence
[Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr) : tu peux les
utiliser et les modifier en citant leur auteur. En proposant une création, tu acceptes de la
partager ainsi. NOVARA lui-même n'est pas dans ce dépôt.
