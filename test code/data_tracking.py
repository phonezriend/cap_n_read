import pyautogui
import pytesseract
from PIL import Image
import time
from datetime import datetime
import re

region = (521, 124, 806, 53) # (x, y, width, height)

def capture_and_read_text():
    # แคปจอ
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    screenshot = pyautogui.screenshot(region=region) # capture เฉพาะเพื้นที่
    screenshot.save(filename)
    print(f"Captured: {filename}")

    # อ่านข้อความจากภาพ
    text = pytesseract.image_to_string(Image.open(filename), lang="eng")

    # เอาเฉพาะตัวเลข
    numbers = re.findall(r"\d+\.\d+", text)

    print("Detected Numbers:", numbers)

time.sleep(1)
capture_and_read_text()