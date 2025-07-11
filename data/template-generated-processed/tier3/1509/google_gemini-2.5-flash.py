def solve():
    """Index: 1509.
    Returns: John's height in feet.
    """
    # L1
    growth_per_month = 2 # grew 2 inches per month
    growth_months = 3 # for 3 months
    inches_gained = growth_per_month * growth_months

    # L2
    initial_height_inches = 66 # John was 66 inches tall
    total_height_inches = initial_height_inches + inches_gained

    # L3
    inches_per_foot = 12 # WK
    total_height_feet = total_height_inches / inches_per_foot

    # FA
    answer = total_height_feet
    return answer