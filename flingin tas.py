import mouse
import math
import ctypes
import pymem
import win32gui
import win32process
import psutil
import pydirectinput
import time
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
time_filepath = os.path.join(current_dir, 'time.txt')
inputs_filepath = os.path.join(current_dir, 'inputs.txt')
redos_filepath = os.path.join(current_dir, 'redos.txt')

for filepath in [time_filepath, inputs_filepath, redos_filepath]:
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass


target_process = "Frog Flinger.exe"

key = {
    'LBUTTON': 0x01,
    'RBUTTON': 0x02,
    'CANCEL': 0x03,
    'MBUTTON': 0x04,
    'XBUTTON1': 0x05,
    'XBUTTON2': 0x06,
    'BACK': 0x08,
    'TAB': 0x09,
    'CLEAR': 0x0C,
    'RETURN': 0x0D,
    'SHIFT': 0x10,
    'CONTROL': 0x11,
    'MENU': 0x12,
    'PAUSE': 0x13,
    'CAPITAL': 0x14,
    'ESCAPE': 0x1B,
    'SPACE': 0x20,
    'PRIOR': 0x21,  # Page Up
    'NEXT': 0x22,   # Page Down
    'END': 0x23,
    'HOME': 0x24,
    'LEFT': 0x25,
    'UP': 0x26,
    'RIGHT': 0x27,
    'DOWN': 0x28,
    'SELECT': 0x29,
    'PRINT': 0x2A,
    'EXECUTE': 0x2B,
    'SNAPSHOT': 0x2C,  # Print Screen
    'INSERT': 0x2D,
    'DELETE': 0x2E,
    'HELP': 0x2F,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'A': 0x41,
    'B': 0x42,
    'C': 0x43,
    'D': 0x44,
    'E': 0x45,
    'F': 0x46,
    'G': 0x47,
    'H': 0x48,
    'I': 0x49,
    'J': 0x4A,
    'K': 0x4B,
    'L': 0x4C,
    'M': 0x4D,
    'N': 0x4E,
    'O': 0x4F,
    'P': 0x50,
    'Q': 0x51,
    'R': 0x52,
    'S': 0x53,
    'T': 0x54,
    'U': 0x55,
    'V': 0x56,
    'W': 0x57,
    'X': 0x58,
    'Y': 0x59,
    'Z': 0x5A,
    'NUMPAD0': 0x60,
    'NUMPAD1': 0x61,
    'NUMPAD2': 0x62,
    'NUMPAD3': 0x63,
    'NUMPAD4': 0x64,
    'NUMPAD5': 0x65,
    'NUMPAD6': 0x66,
    'NUMPAD7': 0x67,
    'NUMPAD8': 0x68,
    'NUMPAD9': 0x69,
    'MULTIPLY': 0x6A,
    'ADD': 0x6B,
    'SEPARATOR': 0x6C,
    'SUBTRACT': 0x6D,
    'DECIMAL': 0x6E,
    'DIVIDE': 0x6F,
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
    'NUMLOCK': 0x90,
    'SCROLL': 0x91,
    'LSHIFT': 0xA0,
    'RSHIFT': 0xA1,
    'LCONTROL': 0xA2,
    'RCONTROL': 0xA3,
    'LMENU': 0xA4,
    'RMENU': 0xA5,
    # Add more as needed
}

hwnd_target = None

def enum_windows(hwnd, _):
    global hwnd_target
    if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        try:
            p = psutil.Process(pid)
            if p.name().lower() == target_process.lower():
                hwnd_target = hwnd
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

win32gui.EnumWindows(enum_windows, None)

if hwnd_target:
    left, top, right, bottom = win32gui.GetWindowRect(hwnd_target)
    width = right - left
    height = bottom - top
else:
    print("game not open")


GetAsyncKeyState = ctypes.windll.user32.GetAsyncKeyState

def key_pressed(vk_code):
    return (GetAsyncKeyState(vk_code) & 0x8000) != 0

def mouse_input(angle_deg, duration=0.005, dist=500):
    mouse.move(width//2,height//2, absolute=False)
    mouse.press()
    
    angle = math.radians(angle_deg-90)

    # Calculate x/y offsets
    x_offset = dist * math.cos(angle)
    y_offset = dist * math.sin(angle)

    # Press, move, release
    mouse.press()
    mouse.move(int(x_offset), int(y_offset), absolute=False, duration=duration)
    mouse.release()
    

pm = pymem.Pymem("Frog Flinger")
def waitfor(ms, pause=False):
    done = False
    while not done:
        with open(time_filepath, 'r') as file:
            curtime = file.read().strip()
        if curtime == '':
            curtime = -1
            
        if (int(curtime) >= int(ms)  and int(curtime) < int(ms) +100) and int(curtime) > -1:
            if pause:
                pydirectinput.press('esc')
            done = True
            print(f"done at {int(curtime)/1000}")

def reset():
    mouse.move(950,550)
    mouse.click()
    mouse.move(770,662)
    time.sleep(0.5)
    mouse.click()
    
def execute_instructions_from_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):  # skip empty lines or comments
                continue
            try:
                exec(line)
            except Exception as e:
                print(f"Error executing line: {line}\n{e}")
    
while True:
    user32 = ctypes.windll.user32
    GetForegroundWindow = user32.GetForegroundWindow
    GetWindowTextLengthW = user32.GetWindowTextLengthW
    GetWindowTextW = user32.GetWindowTextW

    hwnd = GetForegroundWindow()
    length = GetWindowTextLengthW(hwnd)
    buffer = ctypes.create_unicode_buffer(length + 1)
    GetWindowTextW(hwnd, buffer, length + 1)
    
    
    
    
    if key_pressed(key['SHIFT']) and "Frog" in buffer.value:
        with open(redos_filepath, 'r') as f:
            content = f.read().strip()
            current_redos = int(content) if content else 0
        new_redos = current_redos + 1
        with open(redos_filepath, 'w') as f:
            f.write(str(new_redos))
        
        
        execute_instructions_from_file(inputs_filepath)