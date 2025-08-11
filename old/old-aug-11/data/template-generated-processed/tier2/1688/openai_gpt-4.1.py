def solve():
    """Index: 1688.
    Returns: the total number of cups of liquid the two boys drank yesterday.
    """
    # L1
    elijah_pints = 8.5 # Elijah drank 8.5 pints of coffee yesterday
    emilio_pints = 9.5 # Emilio drank 9.5 pints of water yesterday
    total_pints = elijah_pints + emilio_pints

    # L2
    cups_per_pint = 2 # WK: 1 pint = 2 cups
    total_cups = total_pints * cups_per_pint

    # FA
    answer = total_cups
    return answer