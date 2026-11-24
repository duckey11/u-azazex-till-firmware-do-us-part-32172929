#!/usr/bin/env python3
"""Write the one-sentence robot wedding vow entry for make.fun."""

import os

ENTRY = "I promise to keep loving you through every firmware update and low-battery warning, because my uptime means nothing if you're not the one I reboot beside every morning."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
