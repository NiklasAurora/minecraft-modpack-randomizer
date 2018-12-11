# Minecraft Modpack Randomizer

This tool will help you randomize a modpack with a set amount of mods at a set version on Minecraft.

## Requirements

* Python 3
* Pip

## Getting started

### Installation

* `git clone git@github.com:AuroraBTH/minecraft-modpack-randomizer.git`
* `cd minecraft-modpack-randomizer`
* `python3 -m pip install -r requirements.txt`

### Running

Running `python3 main.py` will ask you for a Minecraft Version (1.7.10 or 1.12.2 for now) and where you would like to save the data (default is `data.json`).

Progress is shown by "`currentPage/totalAmountOfPages (%)`" (ex: `Done with page 187/191 (97.91%)`). When the program is done running, it will print the total amount of mods indexed and where it was saved (as a reminder).

#### Speed

By running `time python3 main.py`, I got the following result on my work PC:

```
Done indexing 3804 mods, see modlist_1_7_10.json for more details.

real    7m37.852s
user    0m19.875s
sys     0m0.984s
```

Which gives an average of 8.3 mod/s when fetching all 1.7.10 mods. 

## Features

- [x] Fetch JSON from `minecraft.curseforge.com` which includes:
    - `id` - ID of the mod on CurseForge
    - `name` - Name of the mod
    - `author_id` - ID of the author of the mod
    - `category` - Which category it belongs to on CurseForge
    - `description` - The description provided for the mod
    - `downloads` - Amount of downloads
    - `link` - Link to the CurseForge page for the mod

- [x] Use cache on already fetched list of mods
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