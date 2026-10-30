"""Checks every creation of this repository and writes index.json, the list NOVARA reads.

    python3 scripts/index.py          # check and write index.json
    python3 scripts/index.py --check  # check only (pull requests)

Standard library only. A creation that does not pass is reported and left out (exit code 1).
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEX = re.compile(r"^#[0-9a-fA-F]{6}$")
ID = re.compile(r"^[a-z0-9-]{1,48}$")
COLOURS = ["primary", "secondary", "sky_top", "sky_bottom", "water", "lawn", "road", "sidewalk", "walls", "glass", "leaves", "light"]
UI = ["background", "surface", "text"]
MAX_FILES, MAX_BYTES = 2000, 200 * 1024 * 1024


def text(v, n):
    return isinstance(v, str) and len(v) <= n and not any(ord(c) < 32 for c in v)


def inside(rel):
    p = Path(rel)
    return isinstance(rel, str) and rel and not p.is_absolute() and ".." not in p.parts and "\\" not in rel and ":" not in rel


def check_theme(path):
    t = json.loads(path.read_text(encoding="utf-8"))
    errs = []
    if not text(t.get("name"), 40) or not t["name"].strip():
        errs.append("nom manquant ou trop long")
    for k in COLOURS:
        if not HEX.match(str(t.get("colors", {}).get(k, ""))):
            errs.append(f"couleur {k}")
    for k in UI:
        if not HEX.match(str(t.get("ui", {}).get(k, ""))):
            errs.append(f"couleur d'interface {k}")
    for p in t.get("props", []):
        if p.get("sprite_url") or p.get("anims"):
            errs.append("sprites trouvés en ligne : un thème partagé ne doit pas en contenir")
            break
    entry = {"type": "theme", "id": path.stem, "name": t.get("name", ""), "author": t.get("author", ""), "description": t.get("description", ""),
             "path": str(path.relative_to(ROOT)), "night": bool(t.get("night")),
             "swatches": [t.get("colors", {}).get(k) for k in ("sky_top", "sky_bottom", "primary", "secondary", "lawn")] + [t.get("ui", {}).get("surface")]}
    return entry, errs


def check_plugin(folder):
    errs = []
    m = json.loads((folder / "plugin.json").read_text(encoding="utf-8"))
    if not ID.match(str(m.get("id", ""))) or m["id"] != folder.name:
        errs.append("id invalide ou différent du nom du dossier")
    if not text(m.get("name"), 60) or not text(m.get("version"), 20) or not text(m.get("author", ""), 60) or not text(m.get("description", ""), 400):
        errs.append("nom, version, auteur ou description")
    refs = list(m.get("themes", [])) + list(m.get("guides", [])) + [t.get("path") for t in m.get("templates", [])]
    if not refs:
        errs.append("n'apporte rien")
    for r in refs:
        if not inside(r) or not (folder / r).exists():
            errs.append(f"chemin introuvable ou hors du plugin : {r}")
    files, total = [], 0
    for f in sorted(folder.rglob("*")):
        if f.is_symlink():
            errs.append(f"lien symbolique : {f.name}")
        elif f.is_file():
            total += f.stat().st_size
            files.append(str(f.relative_to(folder)))
    if len(files) > MAX_FILES or total > MAX_BYTES:
        errs.append("trop gros")
    entry = {"type": "plugin", "id": m.get("id", folder.name), "name": m.get("name", ""), "author": m.get("author", ""), "description": m.get("description", ""),
             "version": m.get("version", ""), "path": str(folder.relative_to(ROOT)), "files": files,
             "adds": {"themes": len(m.get("themes", [])), "templates": len(m.get("templates", [])), "guides": len(m.get("guides", []))}}
    return entry, errs


def main():
    entries, bad = [], 0
    for path in sorted((ROOT / "themes").glob("*.novaratheme")):
        try:
            e, errs = check_theme(path)
        except Exception as ex:
            e, errs = None, [f"illisible : {ex}"]
        if errs:
            bad += 1
            print(f"✗ {path.relative_to(ROOT)} : {', '.join(errs)}")
        else:
            entries.append(e)
    for folder in sorted(p for p in (ROOT / "plugins").iterdir() if p.is_dir()):
        try:
            e, errs = check_plugin(folder)
        except Exception as ex:
            e, errs = None, [f"illisible : {ex}"]
        if errs:
            bad += 1
            print(f"✗ {folder.relative_to(ROOT)} : {', '.join(errs)}")
        else:
            entries.append(e)
    print(f"{len(entries)} création(s) valide(s), {bad} refusée(s)")
    if "--check" not in sys.argv:
        (ROOT / "index.json").write_text(json.dumps({"version": 1, "creations": entries}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
