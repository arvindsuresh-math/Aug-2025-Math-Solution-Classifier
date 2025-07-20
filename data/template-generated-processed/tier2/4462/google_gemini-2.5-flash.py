def solve():
    """Index: 4462.
    Returns: the total money spent on soap.
    """
    # L1
    num_bars = 20 # 20 bars of soap
    weight_per_bar = 1.5 # 1.5 pounds
    total_pounds_of_soap = num_bars * weight_per_bar

    # L2
    cost_per_pound = 0.5 # $.5 per pound
    total_cost = total_pounds_of_soap * cost_per_pound

    # FA
    answer = total_cost
    return answer