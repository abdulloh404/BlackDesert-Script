#!/usr/bin/env python3
import subprocess
import time
import threading
import random
from pynput import keyboard

running = False
restart_requested = False
current_thread = None

def press_key(key):
    subprocess.call(['xdotool', 'key', key])

def press_shift_w_and_turn_a():
    global running, restart_requested

    try:
        # monster group1
        if not running: return
        subprocess.call(['xdotool', 'key', '1'])
        print("[DEBUG] กด 1")
        time.sleep(1)

        if not running: return
        subprocess.call(['xdotool', 'click', '3'])
        print("[DEBUG] คลิกขวาครั้งที่ 1")
        time.sleep(0.75)

        if not running: return
        subprocess.call(['xdotool', 'click', '3'])
        print("[DEBUG] คลิกขวาครั้งที่ 2")
        time.sleep(1)

        # monster group2
        subprocess.call(['xdotool', 'keydown', 'Shift_L'])
        time.sleep(0.05)
        subprocess.call(['xdotool', 'keydown', 'w'])
        time.sleep(0.05)
        subprocess.call(['xdotool', 'keydown', 'a'])
        time.sleep(0.35)
        subprocess.call(['xdotool', 'keyup', 'Shift_L'])
        subprocess.call(['xdotool', 'keyup', 'w'])
        subprocess.call(['xdotool', 'keyup', 'a'])
        subprocess.call(['xdotool', 'keydown', 'Shift_L'])
        time.sleep(0.05)
        subprocess.call(['xdotool', 'keydown', 'w'])
        time.sleep(1.5)
        subprocess.call(['xdotool', 'keyup', 'Shift_L'])
        subprocess.call(['xdotool', 'keyup', 'w'])

        subprocess.call(['xdotool', 'key', '2'])
        time.sleep(0.8)
        for _ in range(6):
            press_key("F")
            time.sleep(0.7)

        time.sleep(0.6)
        subprocess.call(['xdotool', 'key', '3'])
        time.sleep(0.8)

        # monster group3
        subprocess.call(['xdotool', 'keydown', 'Shift_L'])
        time.sleep(0.05)
        subprocess.call(['xdotool', 'keydown', 'w'])
        time.sleep(0.05)
        subprocess.call(['xdotool', 'keydown', 'a'])
        time.sleep(0.9)
        subprocess.call(['xdotool', 'keyup', 'a'])
        time.sleep(4)
        subprocess.call(['xdotool', 'keyup', 'Shift_L'])
        subprocess.call(['xdotool', 'keyup', 'w'])
        time.sleep(0.2)
        subprocess.call(['xdotool', 'key', '4'])
        time.sleep(0.3)
        subprocess.call(['xdotool', 'key', '3'])

        # monster group4
        subprocess.call(['xdotool', 'keydown', 'Shift_L'])
        time.sleep(0.05)
        subprocess.call(['xdotool', 'keydown', 'w'])
        time.sleep(0.05)
        subprocess.call(['xdotool', 'keydown', 'a'])
        time.sleep(0.9)
        subprocess.call(['xdotool', 'keyup', 'a'])
        time.sleep(4)
        subprocess.call(['xdotool', 'keyup', 'Shift_L'])
        subprocess.call(['xdotool', 'keyup', 'w'])
        time.sleep(0.2)
        subprocess.call(['xdotool', 'key', '4'])
        time.sleep(0.6)
        subprocess.call(['xdotool', 'key', '3'])


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
