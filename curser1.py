import time
import os

# Different frames representing a rotating circle effect
circle_frames = [
    "   O   ",
    "  /O\\  ",
    "  O O  ",
    " /O O\\ ",
    "  O O  ",
    "  \\O/  ",
    "   O   ",
    "  /O\\  "
]

while True:
    for frame in circle_frames:
        # Clear the terminal screen for Mac
        os.system('clear')
        print(frame)
        time.sleep(0.1)  # Adjust this to control the speed of the rotation
