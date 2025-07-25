def solve():
    """Index: 3971.
    Returns: the number of miles Mona biked on Monday.
    """
    # L4
    total_miles_week = 30 # Mona bikes 30 miles each week
    miles_wednesday = 12 # On Wednesday, she biked 12 miles
    combined_monday_saturday_miles = total_miles_week - miles_wednesday

    # L5
    coefficient_of_M = 3 # WK (from M + 2M = 3M)
    miles_monday = combined_monday_saturday_miles / coefficient_of_M

    # FA
    answer = miles_monday
    return answer