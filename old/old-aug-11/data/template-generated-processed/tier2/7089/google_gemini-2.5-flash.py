def solve():
    """Index: 7089.
    Returns: the total amount Zach spent on the car rental.
    """
    # L1
    miles_monday = 620 # 620 miles on Monday
    cost_per_mile = 0.5 # 50 cents for each mile
    cost_monday_miles = miles_monday * cost_per_mile

    # L2
    miles_thursday = 744 # another 744 miles on Thursday
    cost_thursday_miles = miles_thursday * cost_per_mile

    # L3
    base_rental_cost = 150 # $150
    total_cost = base_rental_cost + cost_monday_miles + cost_thursday_miles

    # FA
    answer = total_cost
    return answer