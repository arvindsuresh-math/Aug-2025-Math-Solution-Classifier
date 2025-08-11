def solve():
    """Index: 6110.
    Returns: the total cups of water Ginger drank/used that day.
    """
    # L1
    cups_per_bottle = 2 # held 2 cups of water
    hours_worked = 8 # working 8 hours
    cups_drank = cups_per_bottle * hours_worked

    # L2
    bottles_poured = 5 # poured an additional 5 bottles of water
    cups_poured = bottles_poured * cups_per_bottle

    # L3
    total_cups_used = cups_drank + cups_poured

    # FA
    answer = total_cups_used
    return answer