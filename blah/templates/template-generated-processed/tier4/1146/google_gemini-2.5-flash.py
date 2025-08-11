def solve():
    """Index: 1146.
    Returns: the total money Jane earned.
    """
    # L1
    tulip_bulbs = 20 # 20 tulip bulbs
    cost_per_bulb = 0.50 # $.50 for every flower bulb
    tulip_earnings = tulip_bulbs * cost_per_bulb

    # L2
    iris_divisor = 2 # half that amount
    iris_bulbs = tulip_bulbs / iris_divisor

    # L3
    iris_earnings = iris_bulbs * cost_per_bulb

    # L4
    daffodil_bulbs = 30 # 30 daffodil bulbs
    daffodil_earnings = daffodil_bulbs * cost_per_bulb

    # L5
    crocus_multiplier = 3 # three times that amount
    crocus_bulbs = daffodil_bulbs * crocus_multiplier

    # L6
    crocus_earnings = crocus_bulbs * cost_per_bulb

    # L7
    total_earnings = tulip_earnings + iris_earnings + daffodil_earnings + crocus_earnings

    # FA
    answer = total_earnings
    return answer