def calculate_pet_years(age, pet_type):
    """
    Calculate the age of a pet in human years.

    Parameters:
    age (int): The age of the pet.
    pet_type (str): The type of the pet, either 'cat' or 'dog'.

    Returns:
    int: The age of the pet in human years.
    """
    if pet_type == 'cat':
        if age == 1:
            return 15
        elif age == 2:
            return 24
        else:
            return 24 + (age - 2) * 4
    elif pet_type == 'dog':
        if age <= 2:
            return age * 10.5
        else:
            return 21 + (age - 2) * 4
    else:
        return None


# Input from the user
age = int(input("Enter the age of your pet: "))
pet_type = input("Enter the type of your pet (cat or dog): ").strip().lower()

# Calculate the pet's age in human years
human_years = calculate_pet_years(age, pet_type)

if human_years is not None:
    print(f"The age of your {pet_type} in human years is: {human_years}")
else:
    print("Invalid pet type. Please enter either 'cat' or 'dog'.")