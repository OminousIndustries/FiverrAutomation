# Live Fiverr → Cube3D Demo Pipeline

An end-to-end proof-of-concept showing how to automate a Fiverr 3D-model gig - Skeleton Script for fiverr automation - designed to be a starting point to modify with AI Coding Agents

1. **OCR** the buyer’s prompt from your seller dashboard via [Microsoft OmniParser](https://github.com/microsoft/OmniParser)  
2. **Text→Mesh** using Roblox’s [Cube 3D](https://github.com/Roblox/cube) foundation model  
3. **UI Automation** with PyAutoGUI to upload the generated `.obj` and deliver the order  

> 🎥 See the companion video walkthrough for a step-by-step demo.

---

## Repo Layout

```
your-project/
├── config.py
├── fiverr_pipeline_live.py
├── mesh_generator.py
├── get_coords.py
├── omniparser_wrapper.py
├── cube/               ← clone of https://github.com/Roblox/cube
└── OmniParser/         ← clone of https://github.com/microsoft/OmniParser
```

---

## Prerequisites

- Python 3.10+ (use a venv or conda, etc.)  
- NVIDIA GPU + CUDA (For a carbon copy of this you need 24gb+)  
- Browser logged in to your Fiverr **seller** account, in a fixed window position  

---

## Quickstart

1. **Clone this repo** and the two dependencies side-by-side:

   ```bash
   git clone <this-repo>.git
   git clone https://github.com/Roblox/cube.git cube
   git clone https://github.com/microsoft/OmniParser.git OmniParser
   ```

2. **Install Python deps** (inside your `fiverr-pipeline` env):

   ```bash
   pip install torch pillow pyautogui
   ```

3. **Install Cube 3D & OmniParser** (per their README):


4. **Calibrate your screen**  
   Edit `config.py` so that all `(x, y)` coordinates match your display and browser layout. Use the included `get_coords.py` snippet to hover & record positions.

5. **Run the pipeline**  
   ```bash
   python fiverr_pipeline_live.py
   ```
   Watch it pick up your test order, generate a mesh, upload the `.obj` and deliver—all automatically.

---

## Customization

- **Swap in a different TTI backend**  
  Replace `mesh_generator.py` with your own text-to-image or text-to-mesh model or anything else you want to do with this.  
- **Extend the flow**  
  Plug in AI coding agents to modify or enhance steps (e.g. add texture generation, automate revisions, integrate payment checks).  
- **One-off demo**  
  The script exits after a single order—feel free to remove the `sys.exit()`/`break` if you want continuous polling.

---

## Caveats

- **Screen-coordinate driven**  
  This relies on fixed clicks and screenshot regions. Any UI change or resolution shift requires updating `config.py`.  
- **Security & fragility**  
  GUI-automation can be brittle. Use this as a learning template, not production code.

---

## Credits

- [Roblox Cube 3D](https://github.com/Roblox/cube) — text-to-shape foundation model  
- [Microsoft OmniParser](https://github.com/microsoft/OmniParser) — visual GUI OCR & semantic parsing  
- [PyAutoGUI](https://github.com/asweigart/pyautogui) — cross-platform GUI automation  
