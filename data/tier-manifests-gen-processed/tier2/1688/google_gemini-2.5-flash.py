def solve():
    """Index: 1688.
    Returns: the total number of cups of liquid the two boys drank.
    """
    # L1
    elijah_coffee_pints = 8.5 # Elijah drank 8.5 pints of coffee yesterday
    emilio_water_pints = 9.5 # Emilio drank 9.5 pints of water yesterday
    total_pints_drunk = elijah_coffee_pints + emilio_water_pints

    # L2
    cups_per_pint = 2 # WK
    total_cups_drunk = total_pints_drunk * cups_per_pint

    # FA
    answer = total_cups_drunk
    return answer