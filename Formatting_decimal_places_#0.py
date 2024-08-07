def format_decimal(number):
    """
    Format a number to 0 decimal places using rounding.

    Parameters:
    number (float): The number to format.

    Returns:
    int: The formatted number as an integer.
    """
    return round(number)

# Example usage
number = float(input("Enter a decimal number: "))
formatted_number = format_decimal(number)

print(f"The number formatted to 0 decimal places is: {formatted_number}")