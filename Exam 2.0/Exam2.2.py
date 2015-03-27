import math

height = 10
radius = 5

# Create a function that calculates the volume of a cylinder, given height and radius.
def cylinderVolume(height, radius):

    # Perform Calculations
    volume = math.pi * radius ** 2 * height

    # Return results
    return volume

volume = cylinderVolume(height, radius)

print(volume)
    
