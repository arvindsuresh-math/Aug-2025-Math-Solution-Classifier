def solve():
    """Index: 955.
    Returns: the number of cups of juice that were drunk.
    """
    # L1
    gallons_bought = 10 # 10 gallons of juice
    cups_per_gallon = 10 # Each gallon has 10 cups
    total_cups_bought = gallons_bought * cups_per_gallon

    # L2
    cups_left = 5 # 5 cups of juice were left
    cups_drunk = total_cups_bought - cups_left

    # FA
    answer = cups_drunk
    return answer