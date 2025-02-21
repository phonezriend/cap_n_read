import pyautogui
import pytesseract
from PIL import Image
import keyboard
import time
from datetime import datetime
import re

start_x, start_y, end_x, end_y = None, None, None, None
capturing = False

print("press 's' to start selecting, 'e' to end selecting, and press 'r' for reset")

def find_region():
    global start_x, start_y, end_x, end_y, capturing

    while True:
        x, y = pyautogui.position()
        print(f"Cursor Position: x={x}, y={y}", end="\r")  # Real-time displaying the region

        if keyboard.is_pressed('s') and not capturing:
            start_x, start_y = x, y
            capturing = True
            print(f"\nStart at ({start_x}, {start_y})")
            time.sleep(0.2)

        if keyboard.is_pressed('e') and capturing:
            end_x, end_y = x, y
            capturing = False
            width = abs(end_x - start_x)
            height = abs(end_y - start_y)

            print(f"\nSelected Region: x={start_x}, y={start_y}, width={width}, height={height}")
            return (start_x, start_y, width, height)

        if keyboard.is_pressed('r'):
            start_x, start_y, end_x, end_y = None, None, None, None
            capturing = False
            print("\nReset done! Select the new region")
            time.sleep(0.2)

        time.sleep(0.1)

region = find_region()

def capture_and_read_text():
    if region is None:
        print("Please select the region!")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(filename)
    print(f"Captured: {filename}")

    text = pytesseract.image_to_string(Image.open(filename), lang="eng")

    numbers = re.findall(r"\d+[\.,]?\d*", text)

    # use this if want only numbers with decimal points ex: 0.00, 2.91, 3.14 ...
    # numbers = re.findall(r"\d+\.\d+", text)

    print("Detected Numbers:", numbers)

time.sleep(1)

capture_and_read_text()
