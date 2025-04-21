#!/usr/bin/env python3
from pynput import mouse, keyboard
from datetime import datetime

last_x, last_y = None, None
min_move_threshold = 10  # จะ log เมื่อขยับมากกว่า 10 พิกเซล

def log_time():
    return datetime.now().strftime("%H:%M:%S.%f")

def on_press(key):
    with open("input_log2.txt", "a") as f:
        f.write(f"[{log_time()}] KEY: {key}\n")

def on_click(x, y, button, pressed):
    with open("input_log2.txt", "a") as f:
        action = "DOWN" if pressed else "UP"
        f.write(f"[{log_time()}] MOUSE CLICK: {button} {action} at ({x},{y})\n")

def on_move(x, y):
    global last_x, last_y
    if last_x is None or last_y is None:
        last_x, last_y = x, y
        return

    dx = abs(x - last_x)
    dy = abs(y - last_y)

    if dx > min_move_threshold or dy > min_move_threshold:
        with open("input_log.txt", "a") as f:
            f.write(f"[{log_time()}] MOUSE MOVE to ({x},{y})\n")
        last_x, last_y = x, y

# Start listeners
kb_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click, on_move=on_move)

kb_listener.start()
mouse_listener.start()
kb_listener.join()
mouse_listener.join()
