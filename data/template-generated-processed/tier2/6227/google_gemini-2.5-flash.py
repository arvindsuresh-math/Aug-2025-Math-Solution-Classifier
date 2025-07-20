def solve():
    """Index: 6227.
    Returns: the total cost Carly pays for shipping.
    """
    # L1
    package_weight = 5 # weighs 5 pounds
    cost_per_pound = 0.80 # $0.80 per pound of weight
    weight_based_charge = package_weight * cost_per_pound

    # L2
    flat_fee = 5.00 # a flat $5.00 fee
    total_cost = weight_based_charge + flat_fee

    # FA
    answer = total_cost
    return answer