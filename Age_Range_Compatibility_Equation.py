def age_range_compatibility(age):
    """
    Calculate the minimum and maximum age for a compatible partner.

    Parameters:
    age (int): The age of the person.

    Returns:
    tuple: The minimum and maximum age for a compatible partner.
    """
    if age < 0:
        return None, None
    min_age = (age / 2) + 7
    max_age = (age - 7) * 2
    return min_age, max_age

# Example usage
age = int(input("Enter your age: "))

min_age, max_age = age_range_compatibility(age)

if min_age is not None and max_age is not None:
    print(f"The age range for a compatible partner is: {min_age:.1f} - {max_age:.1f}")
else:
    print("Invalid age entered.")