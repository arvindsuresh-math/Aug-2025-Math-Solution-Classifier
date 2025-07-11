def solve():
    """Index: 2776.
    Returns: the total amount Jim paid for lamps and bulbs.
    """
    # L1
    lamp_cost_single = 7 # a $7 lamp
    bulb_cost_less = 4 # a bulb which cost $4 less
    bulb_cost_single = lamp_cost_single - bulb_cost_less

    # L2
    num_lamps_bought = 2 # bought 2 lamps
    total_cost_lamps = lamp_cost_single * num_lamps_bought

    # L3
    num_bulbs_bought = 6 # bought 6 bulbs
    total_cost_bulbs = bulb_cost_single * num_bulbs_bought

    # L4
    total_paid = total_cost_lamps + total_cost_bulbs

    # FA
    answer = total_paid
    return answer