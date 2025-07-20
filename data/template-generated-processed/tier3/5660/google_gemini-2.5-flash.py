from fractions import Fraction

def solve():
    """Index: 5660.
    Returns: the total number of hours Mr. Willson worked.
    """
    # L1
    minutes_per_hour = 60 # WK
    monday_fraction = Fraction(3, 4) # 3/4 an hour on Monday
    monday_minutes = minutes_per_hour * monday_fraction

    # L2
    tuesday_divisor = 2 # half an hour
    tuesday_minutes = minutes_per_hour / tuesday_divisor

    # L3
    wednesday_fraction = Fraction(2, 3) # 2/3 an hour on Wednesday
    wednesday_minutes = minutes_per_hour * wednesday_fraction

    # L4
    thursday_fraction = Fraction(5, 6) # 5/6 of an hour on Thursday
    thursday_minutes = minutes_per_hour * thursday_fraction

    # L5
    friday_minutes = 75 # 75 minutes on Friday
    total_minutes = monday_minutes + tuesday_minutes + wednesday_minutes + thursday_minutes + friday_minutes

    # L6
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer