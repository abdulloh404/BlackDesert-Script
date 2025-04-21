#!/usr/bin/env python3
import subprocess
import time
import threading
from pynput import keyboard

running = False
restart_requested = False
current_thread = None

def press_shift_w_and_turn_a():
    global running, restart_requested

    try:
        # skill 1
        if not running: return
        subprocess.call(['xdotool', 'key', '1'])
        print("[DEBUG] กด 1")
        time.sleep(1)

        if not running: return
        subprocess.call(['xdotool', 'click', '3'])  # คลิกขวา
        print("[DEBUG] คลิกขวาครั้งที่ 1")
        time.sleep(0.75)

        if not running: return
        subprocess.call(['xdotool', 'click', '3'])  # คลิกขวาครั้งที่ 2
        print("[DEBUG] คลิกขวาครั้งที่ 2")

        # เคลื่อนที่
        # เพิ่มส่วนอื่นได้ต่อท้าย...

    finally:
        if restart_requested:
            print("[RESTARTING]")
            restart_requested = False
            start_skill_sequence()

def start_skill_sequence():
    global running, current_thread
    running = True
    current_thread = threading.Thread(target=press_shift_w_and_turn_a)
    current_thread.start()

def listen_keys():
    global running, restart_requested, current_thread

    def on_press(key):
        global running
        if key == keyboard.Key.f9 and not running:
            print("[START]")
            start_skill_sequence()

        elif key == keyboard.Key.f10 and running:
            print("[STOP]")
            running = False

        elif key == keyboard.Key.f11:
            if running:
                print("[RESTART TRIGGERED]")
                restart_requested = True
                running = False
            else:
                print("[RESTART DIRECT]")
                start_skill_sequence()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    listen_keys()
