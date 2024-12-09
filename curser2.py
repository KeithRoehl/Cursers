import time
import os

# Different frames representing a spinning arrow
arrow_frames = [
    "    |    ",
    "   /     ",
    "  --      ",
    "   \\     ",
    "    |    ",
    "   /     ",
    "  --      ",
    "   \\     "
]

while True:
    for frame in arrow_frames:
        # Clear the terminal screen for Mac
        os.system('clear')
        print(frame)
        time.sleep(0.1)  # Adjust this to control the speed of the rotation
