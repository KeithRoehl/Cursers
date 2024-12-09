import time
import os

# Different frames representing the rotating "LOADING" text
loading_frames = [
    "LOADING.",
    "LOADING..",
    "LOADING...",
    "LOADING....",
    "LOADING...",
    "LOADING..",
    "LOADING.",
]

while True:
    for frame in loading_frames:
        # Clear the terminal screen for Mac
        os.system('clear')
        print(frame)
        time.sleep(0.5)  # Adjust this to control the speed of the rotation
