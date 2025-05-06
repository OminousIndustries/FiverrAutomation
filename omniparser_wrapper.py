# omniparser_wrapper.py
import os
import sys
import io
import base64
import torch
from PIL import Image

# 1) Point Python at your OmniParser repo so `import util.utils` works
ROOT = os.path.dirname(__file__)
OMNI_ROOT = os.path.join(ROOT, "OmniParser")
if OMNI_ROOT not in sys.path:
    sys.path.insert(0, OMNI_ROOT)

# 2) Import exactly what we need from util/utils.py
from util.utils import (
    check_ocr_box,
    get_som_labeled_img,
    get_yolo_model,
    get_caption_model_processor,
)

class _OmniParser:
    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        # Load the YOLO icon-detector
        self.som_model = get_yolo_model(
            model_path=os.path.join(OMNI_ROOT, "weights", "icon_detect", "model.pt")
        )
        # Load the Florence-2 captioner
        self.caption_model_processor = get_caption_model_processor(
            model_name="florence2",
            model_name_or_path=os.path.join(OMNI_ROOT, "weights", "icon_caption_florence"),
            device=device,
        )
        # You can tweak this threshold if you like
        self.box_threshold = 0.05

    def parse(self, image_b64: str):
        # Decode & open the image
        img_bytes = base64.b64decode(image_b64)
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")

        # 1) OCR only text-boxes
        (ocr_texts, ocr_bboxes), _ = check_ocr_box(
            img,
            display_img=False,
            output_bb_format="xyxy",
            easyocr_args={"paragraph": False, "text_threshold": 0.9},
            use_paddleocr=False,
        )

        # 2) Detect “icons” & fuse with OCR to get final text elements
        _, _, parsed_list = get_som_labeled_img(
            image_source=img,
            model=self.som_model,
            BOX_TRESHOLD=self.box_threshold,
            output_coord_in_ratio=True,
            ocr_bbox=ocr_bboxes,
            draw_bbox_config=None,
            caption_model_processor=self.caption_model_processor,
            ocr_text=ocr_texts,
            iou_threshold=0.7,
            scale_img=False,
            batch_size=128,
        )

        return parsed_list

# Single global instance
_parser = _OmniParser()

def parse_prompt(img: Image.Image) -> str:
    """
    Take a PIL.Image, run it through OmniParser, and return
    a single string composed of all 'content' fields.
    """
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")

    parsed = _parser.parse(b64)   # parsed is a list of dicts

    # Extract only the text content from each box
    texts = []
    for entry in parsed:
        # each entry is a dict, e.g. {'type':'text', 'bbox':..., 'content': "My prompt"}
        content = entry.get("content")
        if content and isinstance(content, str):
            texts.append(content.strip())

    # Join into one prompt string (you can use " " or "\n")
    return " ".join(texts).strip()
