def solve():
    """Index: 642.
    Returns: the total miles Tony will have driven when he is halfway through his errands.
    """
    # L1
    groceries_miles = 10 # 10 miles to get groceries
    haircut_miles = 15 # 15 miles to get a haircut
    doctors_miles = 5 # 5 miles to go to a doctor's appointment
    total_miles = groceries_miles + haircut_miles + doctors_miles

    # L2
    halfway_divisor = 2 # halfway through driving around for his errands
    halfway_miles = total_miles / halfway_divisor

    # FA
    answer = halfway_miles
    return answer