def solve():
    """Index: 1750.
    Returns: the difference in dollars Alberto spent on his car compared to Samara.
    """
    # L1
    oil_cost = 25 # spent $25 on oil
    tires_cost = 467 # $467 on tires
    detailing_cost = 79 # $79 on detailing
    samara_total_cost = oil_cost + tires_cost + detailing_cost

    # L2
    alberto_cost = 2457 # spent $2457 on a new engine
    difference_in_cost = alberto_cost - samara_total_cost

    # FA
    answer = difference_in_cost
    return answer