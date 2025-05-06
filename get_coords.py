import pyautogui, time

try:
    print("Ctrl+C to stop\n")
    while True:
        x, y = pyautogui.position()
        print(f"x={x}, y={y}")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Done.")
