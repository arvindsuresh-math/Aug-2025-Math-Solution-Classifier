def solve():
    """Index: 2777.
    Returns: the total number of cups of coffee they drink together.
    """
    # L1
    brayan_cups_per_hour = 4 # Brayan drinks 4 cups of coffee in an hour
    ratio_brayan_to_ivory = 2 # twice what Ivory drinks
    ivory_cups_per_hour = brayan_cups_per_hour / ratio_brayan_to_ivory

    # L2
    total_cups_per_hour = brayan_cups_per_hour + ivory_cups_per_hour

    # L3
    total_hours = 5 # in 5 hours
    total_cups_in_5_hours = total_hours * total_cups_per_hour

    # FA
    answer = total_cups_in_5_hours
    return answer