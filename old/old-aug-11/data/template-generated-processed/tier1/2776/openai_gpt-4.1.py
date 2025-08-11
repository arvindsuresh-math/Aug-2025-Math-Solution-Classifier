def solve():
    """Index: 2776.
    Returns: the total amount Jim paid for 2 lamps and 6 bulbs.
    """
    # L1
    lamp_cost = 7 # $7 lamp
    bulb_less_than_lamp = 4 # bulb which cost $4 less
    bulb_cost = lamp_cost - bulb_less_than_lamp

    # L2
    num_lamps = 2 # 2 lamps
    total_lamp_cost = lamp_cost * num_lamps

    # L3
    num_bulbs = 6 # 6 bulbs
    total_bulb_cost = bulb_cost * num_bulbs

    # L4
    total_cost = total_lamp_cost + total_bulb_cost

    # FA
    answer = total_cost
    return answer