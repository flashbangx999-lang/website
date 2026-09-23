#!/usr/bin/env python3
"""
========================================================
  KHNK X TERMINAL EXPERIENCE — "She Will Be Loved"
  Dibuat oleh: Khnk X
========================================================
"""

import os
import sys
import time
import random
import shutil
import platform
import subprocess

# =========================================================
# CONFIG
# =========================================================
CONFIG = {
    "boot_line_delay": 0.05,
    "hash_rain_duration": 1.8,
    "hash_rain_fps": 0.03,
    "loading_bar_width": 40,
    "loading_bar_speed": 0.02,
    "decrypt_step_delay": 0.43,
    "decrypt_dots": 3,
    "typing_speed": 0.07,        # Kecepatan default ketik teks
    "line_pause": 0.40,          # Jeda default antar baris
    "equalizer_frames": 10,
    "equalizer_fps": 0.05,
    "outro_delay": 1.0,
}

SONG_TITLE = "SHE WILL BE LOVED - MAROON 5"

# =========================================================
# LYRICS (Disesuaikan dengan tempo lagu)
# =========================================================
LYRICS = [
    {
        "text": "I don't mind spending every day",
        "typing_speed": 0.06,
        "line_pause": 0.60,
    },
    {
        "text": "Out on your corner in the pouring rain",
        "typing_speed": 0.05,
        "line_pause": 0.70,
    },
    {
        "text": "Look for the girl with the broken smile",
        "typing_speed": 0.05,
        "line_pause": 0.60,
    },
    {
        "text": "Ask her if she wants to stay a while",
        "typing_speed": 0.05,
        "line_pause": 1.20,
    },
    {
        "text": "And she will be loved",
        "typing_speed": 0.07,
        "line_pause": 0.30,
    },
    {
        "text": "And she will be loved",
        "typing_speed": 0.07,
        "line_pause": 0.30,
    },
    {
        "text": "And she will be loved",
        "typing_speed": 0.07,
        "line_pause": 0.30,
    },
    {
        "text": "And she will be loved",
        "typing_speed": 0.07,
        "line_pause": 1.50,
    },
]

# =========================================================
# ANSI COLOR HELPERS
# =========================================================
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    GREEN = "\033[32m"
    BRIGHT_GREEN = "\033[92m"
    RED = "\033[31m"
    BRIGHT_RED = "\033[91m"
    YELLOW = "\033[33m"
    BRIGHT_YELLOW = "\033[93m"
    CYAN = "\033[36m"
    BRIGHT_CYAN = "\033[96m"
    MAGENTA = "\033[35m"
    BRIGHT_MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    GRAY = "\033[90m"

def cprint(text, color=C.WHITE, end="\n", bold=False):
    prefix = C.BOLD if bold else ""
    sys.stdout.write(f"{prefix}{color}{text}{C.RESET}{end}")
    sys.stdout.flush()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

BOOT_LINES = [
    ("[ OK ]", C.BRIGHT_GREEN, "Starting Khnk X Core Daemon"),
    ("[ OK ]", C.BRIGHT_GREEN, "Mounting virtual audio filesystem"),
    ("[ OK ]", C.BRIGHT_GREEN, "Loading cryptographic modules"),
    ("[WARN]", C.BRIGHT_YELLOW, "Unofficial decoder detected, continuing anyway"),
    ("[ OK ]", C.BRIGHT_GREEN, "Establishing secure tunnel to music-vault"),
    ("[ OK ]", C.BRIGHT_GREEN, "Handshake with node khnkx-pc.local successful"),
    ("[ OK ]", C.BRIGHT_GREEN, "System ready"),
]

def boot_sequence():
    clear_screen()
    cprint("=" * 55, C.GRAY)
    cprint("  Khnk X SYSTEM BOOT", C.BRIGHT_CYAN, bold=True)
    cprint("=" * 55, C.GRAY)
    time.sleep(0.3)
    for tag, color, msg in BOOT_LINES:
        cprint(f"{tag} ", color, end="")
        cprint(msg, C.WHITE)
        time.sleep(CONFIG["boot_line_delay"] * random.randint(3, 10))
    time.sleep(0.5)

def show_neofetch():
    clear_screen()
    if shutil.which("neofetch"):
        subprocess.run(["neofetch"])
    else:
        _fake_neofetch()
    time.sleep(1.2)

def _fake_neofetch():
    logo = [
        "      _____      ",
        "     /     \\     ",
        "    | () () |    ",
        "     \\  ^  /     ",
        "      |||||      ",
        "      |||||      ",
    ]
    info = [
        ("User", os.environ.get("USER", "Khnk X") + "@khnkx"),
        ("OS", platform.system() + " " + platform.release()),
        ("Kernel", platform.version()[:40]),
        ("Python", platform.python_version()),
        ("Shell", os.environ.get("SHELL", "/bin/bash")),
        ("CPU", platform.processor() or "Unknown"),
        ("Uptime", "does not matter, it's fake anyway"),
    ]
    for i in range(max(len(logo), len(info))):
        left = logo[i] if i < len(logo) else " " * 18
        right = ""
        if i < len(info):
            key, val = info[i]
            right = f"{C.BRIGHT_CYAN}{key:<8}{C.RESET}: {C.WHITE}{val}{C.RESET}"
        cprint(left, C.BRIGHT_MAGENTA, end="  ")
        sys.stdout.write(right + "\n")
    sys.stdout.flush()

HASH_CHARS = "0123456789abcdef"

def hash_rain():
    clear_screen()
    end_time = time.time() + CONFIG["hash_rain_duration"]
    width = shutil.get_terminal_size((80, 20)).columns
    colors = [C.GREEN, C.BRIGHT_GREEN, C.DIM + C.GREEN]
    while time.time() < end_time:
        line = "".join(random.choice(HASH_CHARS) for _ in range(width - 1))
        color = random.choice(colors)
        cprint(line, color)
        time.sleep(CONFIG["hash_rain_fps"])
    time.sleep(0.3)

def loading_bar(label="Initializing"):
    width = CONFIG["loading_bar_width"]
    for percent in range(0, 101):
        filled = int(width * percent / 100)
        bar = "█" * filled + "░" * (width - filled)
        color = C.BRIGHT_YELLOW if percent < 100 else C.BRIGHT_GREEN
        sys.stdout.write(
            f"\r{C.CYAN}{label}...{C.RESET} [{color}{bar}{C.RESET}] {C.WHITE}{percent}%{C.RESET}"
        )
        sys.stdout.flush()
        time.sleep(CONFIG["loading_bar_speed"])
    print()
    time.sleep(0.3)

def access_granted():
    cprint("\n" + "▓" * 55, C.BRIGHT_GREEN)
    cprint("   ACCESS GRANTED — WELCOME TO KHNK X", C.BRIGHT_GREEN, bold=True)
    cprint("▓" * 55 + "\n", C.BRIGHT_GREEN)
    time.sleep(CONFIG["outro_delay"] * 0.6)

DECRYPT_STEPS = ["Instrument", "Lyric", "Vocal"]

def decrypt_step(name):
    cprint(f"Decrypting {name}", C.BRIGHT_RED, end="")
    for _ in range(CONFIG["decrypt_dots"]):
        time.sleep(CONFIG["decrypt_step_delay"])
        cprint(".", C.RED, end="")
    cprint("  [DONE]", C.BRIGHT_GREEN)

def decrypting_sequence():
    for step in DECRYPT_STEPS:
        decrypt_step(step)
    time.sleep(0.4)

def song_found():
    cprint("\n>>> SONG FOUND! <<<", C.BRIGHT_MAGENTA, bold=True)
    cprint(f"Title : {SONG_TITLE}\n", C.BRIGHT_CYAN, bold=True)
    time.sleep(CONFIG["outro_delay"])

EQ_BLOCKS = "▁▂▃▄▅▆▇█"
EQ_COLORS = [C.BRIGHT_GREEN, C.BRIGHT_CYAN, C.BRIGHT_MAGENTA, C.BRIGHT_YELLOW]

def equalizer_burst(bars=12):
    for _ in range(CONFIG["equalizer_frames"]):
        frame = "".join(random.choice(EQ_BLOCKS) for _ in range(bars))
        color = random.choice(EQ_COLORS)
        sys.stdout.write(f"\r  {color}{frame}{C.RESET}")
        sys.stdout.flush()
        time.sleep(CONFIG["equalizer_fps"])
    sys.stdout.write("\r" + " " * (bars + 4) + "\r")
    sys.stdout.flush()

LYRIC_COLOR = C.BRIGHT_YELLOW

def type_line(text, color, typing_speed):
    for ch in text:
        sys.stdout.write(f"{color}{ch}{C.RESET}")
        sys.stdout.flush()
        time.sleep(typing_speed)
    print()

def play_lyrics():
    cprint("♪ Now Playing ♪\n", C.GRAY)
    for line in LYRICS:
        text = line["text"]
        typing_speed = line.get("typing_speed", CONFIG["typing_speed"])
        line_pause = line.get("line_pause", CONFIG["line_pause"])

        equalizer_burst()
        type_line(text, LYRIC_COLOR, typing_speed)
        time.sleep(line_pause)

def outro():
    time.sleep(CONFIG["outro_delay"])
    cprint("\n" + "─" * 55, C.GRAY)
    cprint("  © 2026 Khnk — X", C.BRIGHT_GREEN, bold=True)
    cprint("  \"Instagram: @kangzaan.\"", C.DIM + C.WHITE)
    cprint("  ", C.GRAY)
    cprint("─" * 55 + "\n", C.GRAY)

def main():
    try:
        boot_sequence()
        show_neofetch()
        hash_rain()
        loading_bar("Initializing")
        access_granted()
        decrypting_sequence()
        song_found()
        play_lyrics()
        outro()
    except KeyboardInterrupt:
        cprint("\n\n[ABORTED] Transmission interrupted by user.", C.BRIGHT_RED)
        sys.exit(0)

if __name__ == "__main__":
    main()