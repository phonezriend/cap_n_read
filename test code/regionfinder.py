import pyautogui
import keyboard  # ใช้ตรวจจับการกดปุ่ม
import time

# สร้างตัวแปรเก็บพิกัด
start_x, start_y, end_x, end_y = None, None, None, None
capturing = False

print("กด 's' เพื่อเริ่มเลือกจุด, 'e' เพื่อจบการเลือก, และ 'r' เพื่อรีเซ็ต")

while True:
    x, y = pyautogui.position()
    print(f"Cursor Position: x={x}, y={y}", end="\r")  # แสดงพิกัดแบบเรียลไทม์

    # กด 's' เพื่อเริ่มจับพิกัด
    if keyboard.is_pressed('s') and not capturing:
        start_x, start_y = x, y
        capturing = True
        print(f"\nเริ่มจับพิกัดที่ ({start_x}, {start_y})")

    # กด 'e' เพื่อจบการเลือก
    if keyboard.is_pressed('e') and capturing:
        end_x, end_y = x, y
        capturing = False
        width = abs(end_x - start_x)
        height = abs(end_y - start_y)

        print(f"\nพิกัดที่เลือก: x={start_x}, y={start_y}, width={width}, height={height}")
        break

    # กด 'r' เพื่อรีเซ็ตค่า
    if keyboard.is_pressed('r'):
        start_x, start_y, end_x, end_y = None, None, None, None
        capturing = False
        print("\nรีเซ็ตค่าเรียบร้อยแล้ว! เริ่มเลือกใหม่ได้เลย")

    time.sleep(0.1)
