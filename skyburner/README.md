# SkyBurner Ultimate

> Part of the [PCVR Studios monorepo](../README.md)

SkyBurner Ultimate is a vertical-scrolling arcade space-shooter written entirely in Python for [Pythonista 3](http://omz-software.com/pythonista/) on iPhone and iPad. No external assets required — all visuals are drawn with Pythonista's `scene` and `ui` modules.

**Engine:** Atlas Nexus Engine v1.0  
**Platform:** Pythonista 3 / iOS  
**Dependencies:** None (pure Python)

---

## Files

| File | Description |
|------|-------------|
| `atlas_nexus.py` | Core engine: entity/component system, AABB collision, score manager, wave manager |
| `entities.py` | Player, enemies (Fighter, Cruiser, Boss), bullets, power-ups |
| `skyburner.py` | Pythonista Scene subclass, HUD, starfield, game states, touch input |

---

## How to Run

1. Install **Pythonista 3** from the App Store.
2. Copy all three files into a folder inside Pythonista.
3. Open `skyburner.py` and tap ▶ Run.

---

## Features

| Feature | Details |
|---------|---------|
| Engine | Custom entity-component system with AABB collision |
| Weapons | 4 tiers: Single laser → Dual cannon → Triple spread → Homing missiles |
| Enemies | Fighter, Cruiser, Boss (every 5th wave) |
| Boss | Multi-phase: Entry → Attack 1 → Attack 2 → Rage |
| Power-ups | Weapon upgrade, shield, health, bomb, speed |
| Combo | Kill-streak multiplier up to ×8 |
| Background | 115-star parallax starfield |
| HUD | Score, high-score, health, shield, lives, bombs, wave, boss bar |

---

## Controls

| Input | Action |
|-------|--------|
| Drag (left half) | Move ship |
| Tap (right half) | Detonate bomb |
| *(automatic)* | Continuous fire |

---

## Downloads

Downloads are hosted on Discord — [join free](https://discord.gg/E7bW3Zh4x).

- **Game:** [Download SkyBurner Ultimate](https://discord.com/channels/1316937801995911198/1484003872178573495/1484552464639332605)
- **Music:** [Download Game Music](https://discord.com/channels/1316937801995911198/1484003872178573495/1484595490828845229)

---

*© PCVR STUDIOS 2026 · Atlas Nexus Engine v1.0*
