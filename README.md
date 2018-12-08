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

## Features implemented

* Fetch JSON from `minecraft.curseforge.com` which includes:
    - `id` - ID of the mod on CurseForge
    - `name` - Name of the mod
    - `category` - Which category it belongs to on CurseForge
    - `description` - The description provided for the mod
    - `link` - Link to the CurseForge page for the mod

## Features missing

* Use cache on already fetched list of mods
* Host pre-fetched JSON to save requests to CurseForge (updates every 24 hour)
* Get X amount of random mods from that JSON
* Generate a `manifest.json` so that users can import the modpack in the Twitch Launcher