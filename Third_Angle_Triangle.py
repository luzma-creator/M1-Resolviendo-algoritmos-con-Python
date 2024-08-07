def calculate_third_angle(angle1, angle2):
    """
    Calculate the third angle of a triangle given two angles.

    Parameters:
    angle1 (float): The first angle of the triangle.
    angle2 (float): The second angle of the triangle.

    Returns:
    float: The third angle of the triangle.
    """
    # The sum of angles in a triangle is always 180 degrees
    return 180 - (angle1 + angle2)

# Example usage
angle1 = float(input("Enter the first angle of the triangle: "))
angle2 = float(input("Enter the second angle of the triangle: "))

third_angle = calculate_third_angle(angle1, angle2)

print(f"The third angle of the triangle is: {third_angle} degrees")