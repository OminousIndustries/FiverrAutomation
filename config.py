# config.py
# 1920×1080 display, calibrated coords

# ——— Browser polling ———
REFRESH_BTN                = (95,   85)   # your browser’s Refresh

# ——— Order navigation ———
FIVERR_NEW_ORDERS_BTN      = (850,  480)  # click to open the latest order

# ——— Prompt OCR region ———
# top-left = (431,579), bottom-right = (1013,616)
FIVERR_DESCRIPTION_REGION  = (431,  579, 582, 37)

# ——— Delivery steps ———
FIVERR_DELIVER_NOW_BTN     = (1496, 186)
FIVERR_MSG_BOX             = (580,  410)
FIVERR_UPLOAD_BTN          = (630,  608)
# File‐chooser search & select coords (Ubuntu GTK chooser)
FILE_CHOOSER_SEARCH_BTN    = (1276, 354)   # magnifying‐glass icon
FILE_CHOOSER_SEARCH_FIELD  = ( 869, 401)   # where you type “object”
FILE_CHOOSER_FILE_ENTRY    = ( 791, 468)   # the generated OBJ in the list
FILE_CHOOSER_OPEN_BTN      = (1339, 351)   # orange “Open” button

FIVERR_FINAL_DELIVER_BTN   = (1306, 877)

# ——— Timing ———
POLL_INTERVAL              = 30          # seconds between each cycle
