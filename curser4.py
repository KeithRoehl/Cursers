import time
import os

# Dog body with alternating leg positions
dog_frames = [
    """
       __
    o-''|\\_____/)
     \\_/|_)     )
        \\  __  /
        (_/ (_/
    """,
    """
       __
    o-''|\\_____/)
     \\_/|_)     )
        \\  __  /
        (_/ (_/    
    """,
    """
       __
    o-''|\\_____/)
     \\_/|_)     )
        \\  __  /
        (_/ (_/    
    """,
    """
       __
    o-'-|\\_____/)
     \\_/|_)     )
        \\  __  /
         (_\  (_\   
    """
]

# Function to animate the dog walking
def walk_dog():
    width = 50  # Width of the terminal screen
    while True:
        for i in range(width):
            os.system('clear')  # Clear the terminal screen
            # Loop through dog frames with alternating leg positions
            frame = dog_frames[i % len(dog_frames)]  # Alternating leg frames
            print(" " * i + frame)  # Move the dog across the screen
            time.sleep(0.2)  # Control the speed of the walking

# Run the dog walking animation
walk_dog()
