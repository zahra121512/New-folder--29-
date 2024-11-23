import math

def calculate_circumference(radius):
    """Calculates the circumference of a circle given its radius.

    Args:
        radius: The radius of the circle.

    Returns:
        The circumference of the circle.
    """

    circumference = 2 * math.pi * radius
    return circumference

# Example usage:
radius = 5
result = calculate_circumference(radius)
print("The circumference of the circle is:", result)