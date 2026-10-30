# Le format d'un thème NOVARA (.novaratheme)

Un thème est un petit fichier JSON : des couleurs et des choix dans des listes connues. NOVARA
le vérifie, puis dessine lui-même la ville, les fonds d'écran, les icônes et le curseur.

Le plus simple est de le créer dans NOVARA (Réglages › Apparence › Mes thèmes › « Créer un thème
avec l'IA ») puis de l'exporter. Exemple : [themes/lagon-corail.novaratheme](../themes/lagon-corail.novaratheme).

| Champ | Contenu |
|---|---|
| `name` | Nom du thème, 40 caractères au plus. |
| `author`, `description` | Facultatifs : ton nom, une phrase. |
| `base` | Les formes des bâtiments : `aero`, `metro`, `eco`, `dorfic`, `dark-aero`, `aurora`, `technozen`, `glacier`. |
| `sky_kind` | `soleil`, `pastel`, `brume`, `nuit`, `aurore`, `bandes`. |
| `horizon` | `verre`, `eco`, `montagnes`, `glaciers`, `zen`, `usine`, `neon`, `aplats`. |
| `plaza` | Le sol de la place : `verre`, `jardin`, `mosaique`, `gravier`, `grille`, `glace`, `neon`. |
| `roof` | Les toits : `jardin`, `solaire`, `tuile`, `zen`, `chalet`, `neige`, `neon`, `technique`. |
| `particles` | Ce qui flotte : `bulles`, `neige`, `petales`, `pollen`, `lucioles`, `etincelles`, `confettis`. |
| `birds` | `mouette`, `pigeon`, `hirondelle`, `grue-vol`, `aucun`. |
| `trees`, `animals` | 1 à 8 noms d'arbres et d'animaux de la ville (voir l'exemple). |
| `icon_style` | Les icônes : `verre`, `aplats`, `contour`, `neon`. |
| `cursor_mark` | Le signe du curseur : `bulle`, `feuille`, `etoile`, `flocon`, `coeur`, `lune`, `eclair`, `note`, `cible`, `fleur`. |
| `night`, `snow`, `flat`, `neon`, `smoke` | `true` ou `false`. |
| `colors` | 12 couleurs `#rrggbb` : `primary`, `secondary`, `sky_top`, `sky_bottom`, `water`, `lawn`, `road`, `sidewalk`, `walls`, `glass`, `leaves`, `light`. |
| `ui` | 3 couleurs `#rrggbb` de l'interface : `background`, `surface`, `text` (lisible sur `surface`). |
| `scene` | Facultatif : le décor des fonds d'écran, décrit en anglais pour le générateur d'images local. |
| `props` | Facultatif : les créatures et objets du thème (décrits en anglais dans `look`), dessinés par le générateur d'images local. |
