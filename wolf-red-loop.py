#!/usr/bin/env python3
from pynput import keyboard
import threading
import time
import random
import subprocess

running = False
listener = None
forward = True  # ต้องมีตัวแปรนี้ตั้งแต่แรก

def press_key(key):
    subprocess.call(['xdotool', 'key', key])

def small_forward_or_backward(go_forward=True):
    repeat = random.randint(3, 4)
    key = 'w' if go_forward else 's'
    print(f"[DEBUG] {'เดินหน้า' if go_forward else 'ถอยหลัง'} (กด '{key}' {repeat} ครั้ง)")
    for _ in range(repeat):
        subprocess.call(['xdotool', 'key', key])
        time.sleep(random.uniform(0.2, 0.3))
    time.sleep(random.uniform(0.3, 0.5))  # พักนิดหน่อยหลังเดิน

def skill_loop():
    global running, forward
    while running:
        press_key("1")
        time.sleep(random.uniform(2, 2.75))

        press_key("2")
        time.sleep(random.uniform(0.5, 0.75))
        for _ in range(4):
            press_key("F")
            time.sleep(random.uniform(0.5, 0.75))

        time.sleep(random.uniform(1.5, 2.5))

        press_key("3")
        time.sleep(random.uniform(5, 6))
        press_key("4")
        time.sleep(random.uniform(1.25, 1.65))
        press_key("5")
        time.sleep(random.uniform(1.5, 1.8))

        print(f"[DEBUG] Walking {'forward' if forward else 'backward'}")
        small_forward_or_backward(go_forward=forward)
        forward = not forward

        print("[DEBUG] Loop end, sleeping...\n")
        time.sleep(random.uniform(5, 6))

def on_press(key):
    global running

    try:
        if key == keyboard.Key.f11 and keyboard.Controller().pressed_keys == {keyboard.Key.ctrl_l}:
            pass  # won't trigger, Controller() doesn't track current keys, so let's handle it better
    except:
        pass

    if isinstance(key, keyboard.HotKey):
        return

    if key == keyboard.Key.f11 and ctrl_pressed[0]:
        if not running:
            running = True
            threading.Thread(target=skill_loop, daemon=True).start()
            print("Started")
    elif key == keyboard.Key.f12 and ctrl_pressed[0]:
        running = False
        print("Stopped")

ctrl_pressed = [False]

def on_key_event(key):
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed[0] = True
    on_press(key)

def on_key_release(key):
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed[0] = False

def main():
    with keyboard.Listener(on_press=on_key_event, on_release=on_key_release) as l:
        l.join()

if __name__ == "__main__":
    main()
