def full_48_minutes_average(stat, minutes_played):
    """
    Calculate the full 48 minutes average for an NBA player.

    Parameters:
    stat (float): The player's statistic (e.g., points, rebounds, assists).
    minutes_played (float): The number of minutes the player has played.

    Returns:
    float: The player's full 48 minutes average.
    """
    if minutes_played == 0:
        return 0
    return (stat / minutes_played) * 48

# Example usage
stat = float(input("Enter the player's statistic (e.g., points, rebounds, assists): "))
minutes_played = float(input("Enter the number of minutes the player has played: "))

average_48_minutes = full_48_minutes_average(stat, minutes_played)

print(f"The player's full 48 minutes average is: {average_48_minutes:.2f}")