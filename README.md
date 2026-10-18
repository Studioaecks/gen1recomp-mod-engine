# Gen1Recomp Mod Engine

**A practical toolkit for creating, editing, packaging, and distributing mods for the Pokemon Gen 1 Recompilation Project.**

Based on the Pokemon Gen 1 Recompilation Project by BOIS CLUB GAMES, LLC  
(https://github.com/bryanthaboi/gen1recomp)

This is an independent community tool. It is **not** affiliated with BOIS CLUB GAMES, LLC or the official Gen1Recomp project. It generates standard Gen1Recomp mods (`manifest.json` + `main.lua`) that work with the official engine and mod loader.

**Repository:** https://github.com/Studioaecks/gen1recomp-mod-engine

## What this is

A local toolkit (Python + templates) designed specifically for Gen1Recomp modding. It aims to reduce friction for both new and experienced modders by providing:

- Correct scaffolding with automatic licensing attribution and changelog updates
- Predictive coding templates and common-pattern suggestions
- Sprite auto-import and registration code generation
- Map preset system (reusable tree/house/building/town combinations) and multi-ROM layering helpers
- AI-assisted snippet generation and error handling (via optional xAI / SuperGrok API key)
- Packaging into installable zip formats with version targeting and update-check metadata
- Clear instructions for sharing on Discord and official mod lists
- GitHub-ready structure so the community can extend it

Full voxel-level game navigation and in-engine tile selection require the Gen1Recomp source and a running LÖVE instance. This toolkit focuses on the authoring, validation, and packaging layers that sit in front of the official mod API.

## Desktop launch (Godot-style editor)

The toolkit includes a self-contained **XENO-MOD** visual editor:

- Godot-like layout: File Weave, Map Lattice viewport, Node Inspector, Signal Log
- Alien-intelligence aesthetic (void panels, bioluminescent accents)
- Simulated draggable map lattice, code strand with predictive hints, sprite view
- Always-visible attribution

### Launch from desktop

| Platform | Shortcut file | How to use |
|----------|---------------|------------|
| Windows  | `ModEngine.bat` | Double-click, or create a desktop shortcut pointing to it |
| Linux    | `ModEngine.sh` or `ModEngine.desktop` | `chmod +x ModEngine.sh` then run, or copy `.desktop` to `~/.local/share/applications` |
| macOS    | `ModEngine.command` | Double-click (may need to allow in Security settings) |

All launchers start a local server and open the editor in your default browser. Close the terminal window to shut it down.

```bash
# Or run directly
python3 ModEngine.py
```

## Quick start (tools)

```bash
# Scaffold a new content mod
python tools/scaffold.py my_cool_mod --name "My Cool Mod" --games red,blue --category GAMEPLAY

# Generate a sprite registration snippet after dropping PNGs into assets/
python tools/sprite_importer.py my_cool_mod

# Get AI help on an error or for a small snippet (requires XAI_API_KEY)
python tools/ai_helper.py --prompt "patch Growlithe's speed to 90 and log when it enters a map"

# Package for distribution
python tools/pack.py my_cool_mod
```

Mods produced by this toolkit are pure Lua + JSON and run on every platform Gen1Recomp supports (Windows, macOS, Linux, and others where the official builds exist).

## License & attribution

See `LICENSE`. All work based on or generating mods for Gen1Recomp must carry the mandatory credit:

> Based on the Pokemon Gen 1 Recompilation Project by BOIS CLUB GAMES, LLC  
> (https://github.com/bryanthaboi/gen1recomp)

## Community

- Official Gen1Recomp: https://github.com/bryanthaboi/gen1recomp
- This toolkit: open for PRs, new templates, better AI prompts, and UI front-ends
- Share mods made with the toolkit on the official Discord mod channels

---

*Created to make Gen1Recomp modding faster, clearer, and more accessible while respecting the original project's license and attribution requirements.*
