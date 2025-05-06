# fiverr_pipeline_live.py
import os, time, sys
import pyautogui

import config
from omniparser_wrapper import parse_prompt
from mesh_generator import generate_mesh

pyautogui.PAUSE = 0.5

def main_once():
    print("▶ Starting live Fiverr→Cube3D pipeline…")
    while True:
        # 1) Refresh & open latest order
        pyautogui.click(*config.REFRESH_BTN)
        time.sleep(2)
        pyautogui.click(*config.FIVERR_NEW_ORDERS_BTN)
        time.sleep(2)

        # 2) Screenshot & OCR the buyer’s prompt
        img    = pyautogui.screenshot(region=config.FIVERR_DESCRIPTION_REGION)
        prompt = parse_prompt(img)
        print(f"[1] Parsed prompt: “{prompt}”")

        # 3) Text→mesh & export OBJ
        order_id = prompt.replace(" ", "_")[:8]
        obj_path = generate_mesh(prompt, order_id)

        # 4) Deliver: click “Deliver Now”
        pyautogui.click(*config.FIVERR_DELIVER_NOW_BTN)
        time.sleep(1)

        # 5) Write the thank‐you message
        pyautogui.click(*config.FIVERR_MSG_BOX)
        pyautogui.write("Thanks for the order! Attached is your 3D model.")

        # 6) Open the file dialog
        pyautogui.click(*config.FIVERR_UPLOAD_BTN)
        time.sleep(1)

        # 7) Click the search icon
        pyautogui.click(*config.FILE_CHOOSER_SEARCH_BTN)
        time.sleep(0.2)

        # 8) Type “object” to filter down to your mesh
        pyautogui.click(*config.FILE_CHOOSER_SEARCH_FIELD)
        pyautogui.write("output")
        time.sleep(0.5)

        # 9) Click the single result
        pyautogui.click(*config.FILE_CHOOSER_FILE_ENTRY)
        time.sleep(0.2)

        # 10) Click “Open” to attach
        pyautogui.click(*config.FILE_CHOOSER_OPEN_BTN)
        time.sleep(20)

        # Click "Deliver" button to deliver the order
        pyautogui.click(*config.FIVERR_FINAL_DELIVER_BTN)
        time.sleep(2)

        print("[2] Order delivered ✅")
        # exit now that we’re done
        sys.exit(0)

if __name__ == "__main__":
    main_once()
