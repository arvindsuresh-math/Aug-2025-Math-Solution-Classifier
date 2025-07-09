def solve_26():
    """
    Calculates the amount of salt in milliliters from a given volume of seawater
    with a certain salt percentage.
    """
    total_seawater_liters = 2
    salt_percentage = 0.20  # 20% as a decimal
    ml_per_liter = 1000

    # Calculate the amount of salt in liters
    salt_liters = total_seawater_liters * salt_percentage

    # Convert the amount of salt from liters to milliliters
    salt_ml = salt_liters * ml_per_liter

    return salt_ml

# Execute the function to get the final answer
final_answer = solve_26()
print(final_answer)