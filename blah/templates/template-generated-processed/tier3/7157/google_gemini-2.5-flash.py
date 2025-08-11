def solve():
    """Index: 7157.
    Returns: the total number of pints of cider Haley can make.
    """
    # L1
    golden_delicious_per_pint = 20 # 20 golden delicious apples
    pink_lady_per_pint = 40 # 40 pink lady apples
    total_apples_per_pint = golden_delicious_per_pint + pink_lady_per_pint

    # L2
    pints_per_gallon = 8 # WK
    apples_per_gallon = total_apples_per_pint * pints_per_gallon

    # L3
    apples_per_hour_per_farmhand = 240 # pick 240 apples per hour
    num_farmhands = 6 # 6 farmhands
    total_apples_per_hour = apples_per_hour_per_farmhand * num_farmhands

    # L4
    hours_worked = 5 # will work 5 hours today
    total_apples_gathered = total_apples_per_hour * hours_worked

    # L5
    gallons_of_cider = total_apples_gathered / apples_per_gallon

    # L6
    total_pints_of_cider = gallons_of_cider * pints_per_gallon

    # FA
    answer = total_pints_of_cider
    return answer