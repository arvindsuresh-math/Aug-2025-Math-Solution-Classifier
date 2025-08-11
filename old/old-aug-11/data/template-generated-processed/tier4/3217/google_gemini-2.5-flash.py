def solve():
    """Index: 3217.
    Returns: the total money spent on pens by the three friends.
    """
    # L1
    robert_pens = 4 # Robert buys 4 pens
    julia_multiplier = 3 # Julia buys three times as many pens as Robert
    julia_pens = robert_pens * julia_multiplier

    # L2
    dorothy_divisor = 2 # Dorothy buys half as many pens as Julia
    dorothy_pens = julia_pens / dorothy_divisor

    # L3
    total_pens = robert_pens + julia_pens + dorothy_pens

    # L4
    cost_per_pen = 1.50 # one pen costs $1.50
    total_cost = total_pens * cost_per_pen

    # FA
    answer = total_cost
    return answer