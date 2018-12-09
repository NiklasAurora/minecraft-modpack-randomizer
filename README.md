# Minecraft Modpack Randomizer

This tool will help you randomize a modpack with a set amount of mods at a set version on Minecraft.

## Requirements

* Python 3
* Pip

## Getting started

* `git clone LINK`
* `cd minecraft-modpack-randomizer`
* `python3 -m pip install -r requirements.txt`
* `python3 main.py`

## Features

- [x] Fetch JSON from `minecraft.curseforge.com` which includes:
    - `id` - ID of the mod on CurseForge
    - `name` - Name of the mod
    - `author_id` - ID of the author of the mod
    - `category` - Which category it belongs to on CurseForge
    - `description` - The description provided for the mod
    - `downloads` - Amount of downloads
    - `link` - Link to the CurseForge page for the mod

- [ ] Use cache on already fetched list of mods
- [ ] Host pre-fetched JSON to save requests to CurseForge (updates every 24 hour)
- [ ] Get X amount of random mods from that JSON
- [ ] Generate a `manifest.json` so that users can import the modpack in the Twitch Launcher

## Example JSON

```json
{
    "id": 32274,
    "name": "JourneyMap",
    "author_id": 7577665,
    "category": "Map and Information",
    "description": "Real-time mapping in-game or your browser as you explore.",
    "downloads": 41885956,
    "link": "https://www.curseforge.com/minecraft/mc-mods/journeymap"
}
```

## Credits

This project is not affiliated with, funded, or in any way associated with CurseForge or Mojang.

[Licensed under MIT](LICENSE.md)

```
Niklas 'Aurora' Andersson
```