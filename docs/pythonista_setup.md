# Pythonista 3 Setup Guide (iOS)

**PCVR Studios — Running modules on iPhone & iPad**

---

## 1. Installing Pythonista 3

1. Open the **App Store** on your iPhone or iPad.
2. Search for **Pythonista 3** (by Ole Zorn).
3. Purchase and install — it includes a full Python 3 interpreter with `scene`,
   `ui`, `canvas`, and many built-in modules.

> **Note:** Pythonista 3 is a paid app (~$9.99). It is the standard environment
> for all PCVR Studios iOS titles.

---

## 2. Cloning via StaSh or Working Copy

### Option A — StaSh (shell inside Pythonista)

1. Install **StaSh** by running this in Pythonista's console:
   ```python
   import requests as r; exec(r.get('https://raw.githubusercontent.com/ywangd/stash/master/getstash.py').text)
   ```
2. Restart Pythonista.
3. Open `launch_stash.py` and tap **Run**.
4. In the StaSh shell:
   ```bash
   git clone https://github.com/AIVaneer/AIVaneer-PCVR-Studios.git
   ```

### Option B — Working Copy (Git client)

1. Install **Working Copy** from the App Store (free tier works).
2. Clone `https://github.com/AIVaneer/AIVaneer-PCVR-Studios.git`.
3. Use the **Share** menu to move files into Pythonista's `Documents` folder.

---

## 3. File Structure on iOS

After cloning, your Pythonista `Documents` folder should look like:

```
Documents/
└── AIVaneer-PCVR-Studios/
    ├── skyburner/
    │   ├── atlas_nexus.py
    │   ├── entities.py
    │   └── main_scene.py
    ├── eve_toolkit/
    │   ├── __init__.py
    │   ├── dashboard.py
    │   ├── economy.py
    │   └── ...
    └── project_dont_die/
        ├── __init__.py
        └── token_economy.py
```

---

## 4. Running Modules

### SkyBurner Ultimate

1. Navigate to `skyburner/` in the Pythonista file browser.
2. Open `main_scene.py`.
3. Tap **Run** (▶).
4. The game launches in full-screen.

### Eve Toolkit Dashboard

1. Open `eve_toolkit/dashboard.py`.
2. Tap **Run** (▶).
3. The terminal dashboard renders in the console.

### Atlas Omega Command Center

1. Open `eve_toolkit/atlas_omega.py`.
2. Tap **Run** (▶).
3. All registered modules run in sequence and report their status.

---

## 5. Tips & Tricks

- **Auto-complete:** Pythonista's editor has full Python auto-complete built in.
- **Multiple files:** Use Pythonista's tab system to keep multiple files open.
- **External keyboard:** Pairs with any Bluetooth keyboard for faster coding.
- **No internet required:** All PCVR Studios games run fully offline.

---

© PCVR STUDIOS 2026
