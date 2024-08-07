def liters(time):
    """
    Calculate the amount of water (in liters) to drink based on the time spent exercising.

    Parameters:
    time (float): The time spent exercising in hours.

    Returns:
    float: The amount of water in liters.
    """
    return time * 0.5

# Example usage
time_spent = float(input("Enter the time spent exercising in hours: "))
water_needed = liters(time_spent)

print(f"You need to drink {water_needed} liters of water.")