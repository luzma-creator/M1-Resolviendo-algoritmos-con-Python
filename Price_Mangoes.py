def calculate_price_of_mangoes(mango_count, price_per_mango):
    """
    Calculate the total price of mangoes with a 'buy 2 get 1 free' offer.

    Parameters:
    mango_count (int): The total number of mangoes.
    price_per_mango (float): The price of a single mango.

    Returns:
    float: The total price after applying the offer.
    """
    # Calculate the number of mangoes you need to pay for
    paid_mangoes = (mango_count // 3) * 2 + (mango_count % 3)

    # Calculate the total price
    total_price = paid_mangoes * price_per_mango

    return total_price


# Example usage
mango_count = int(input("Enter the number of mangoes: "))
price_per_mango = float(input("Enter the price per mango: "))

total_price = calculate_price_of_mangoes(mango_count, price_per_mango)

print(f"The total price for {mango_count} mangoes is: ${total_price:.2f}")