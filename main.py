from microbit import *

# Define star patterns
star1 = Image("00000:00090:00900:09000:00000")
star2 = Image("00000:00900:09090:00090:00000")
star3 = Image("00090:00990:00000:00000:00900")

# Create a list of frames for the animation
frames = [star1, star2, star3]

# Loop through frames to create the spinning star animation
while True:
    for frame in frames:
        display.show(frame)
        sleep(200)
