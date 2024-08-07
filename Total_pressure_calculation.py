def calculate_total_pressure(pressures):
    """
    Calculate the total pressure of a mixture of gases.

    Parameters:
    pressures (list): A list of pressures of individual gases.

    Returns:
    float: The total pressure of the mixture.
    """
    return sum(pressures)

# Example usage
num_gases = int(input("Enter the number of gases in the mixture: "))

pressures = []
for i in range(num_gases):
    pressure = float(input(f"Enter the pressure of gas {i+1}: "))
    pressures.append(pressure)

total_pressure = calculate_total_pressure(pressures)

print(f"The total pressure of the mixture is: {total_pressure:.2f} units")