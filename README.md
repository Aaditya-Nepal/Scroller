# Insta Scroller — Head Movement Controlled Scrolling

A simple and fun Python project that lets you scroll your laptop screen (like Instagram reels or any webpage) using just your **head movements** — no keyboard or mouse needed!

---

## Why This?

If you’re like me — lazy but love scrolling reels or social media on your laptop while eating — this project is perfect.
Instead of touching the keyboard or trackpad, just move your head left or right to scroll **up or down** smoothly!

---

## How It Works

- Uses **Mediapipe Face Mesh** to detect your nose position via webcam.
- Smooths out the head movement to avoid jitter.
- When you move your head **left**, it scrolls **down** the page.
- When you move your head **right**, it scrolls **up** the page.
- Shows visual feedback in a window to help you see your head position.

---

## Features

- Real-time head tracking using your webcam.
- Smooth scrolling based on head position.
- Works on any app that supports scrolling (browsers, social media apps, etc.).
- Easy to run with minimal setup.

---

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- Mediapipe
- PyAutoGUI
- Numpy

## How to use

- Run scroller.py.
- Make sure your webcam is on and facing you.
- Move your head left to scroll down and right to scroll up.

Install dependencies with:

```bash
pip install opencv-python mediapipe pyautogui numpy
