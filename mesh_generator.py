# mesh_generator.py
import os, sys, glob, subprocess

PROJECT_ROOT  = os.path.dirname(__file__)
CUBE_ROOT     = os.path.join(PROJECT_ROOT, "cube")
GPT_CKPT      = os.path.join(CUBE_ROOT, "model_weights", "shape_gpt.safetensors")
SHAPE_CKPT    = os.path.join(CUBE_ROOT, "model_weights", "shape_tokenizer.safetensors")
OUTPUT_DIR    = os.path.join(CUBE_ROOT, "outputs")

def generate_mesh(prompt: str, order_id: str) -> str:
    """
    1) Calls `python -m cube3d.generate` (fast-inference + prompt).
    2) Grabs `outputs/output.obj`.
    3) Renames to `output_<order_id>.obj` in project root.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    cmd = [
        sys.executable, "-m", "cube3d.generate",
        "--gpt-ckpt-path",   GPT_CKPT,
        "--shape-ckpt-path", SHAPE_CKPT,
        "--prompt", prompt,
        "--output-dir", OUTPUT_DIR,
    ]
    print("[mesh_generator] Running:", " ".join(cmd))
    # If you installed cube3d with `pip install -e ./cube`, no cwd needed.
    # Otherwise, uncomment the cwd=… below:
    subprocess.run(cmd, check=True, cwd=CUBE_ROOT)

    # Find the newest OBJ
    objs = glob.glob(os.path.join(OUTPUT_DIR, "*.obj"))
    if not objs:
        raise RuntimeError("No .obj found in outputs/")
    latest = max(objs, key=os.path.getmtime)

    dest = os.path.join(PROJECT_ROOT, f"output_{order_id}.obj")
    os.replace(latest, dest)
    print(f"[mesh_generator] Renamed {latest} → {dest}")
    return dest
