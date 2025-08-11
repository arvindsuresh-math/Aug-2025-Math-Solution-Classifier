def solve():
    """Index: 6402.
    Returns: the total amount spent on limes.
    """
    # L1
    tablespoons_per_drink = 1 # 1 tablespoon of lime juice per drink
    num_days = 30 # 30 days
    total_tablespoons_juice = tablespoons_per_drink * num_days

    # L2
    tablespoons_per_lime = 2 # 2 tablespoons of lime juice per lime
    total_limes_needed = total_tablespoons_juice / tablespoons_per_lime

    # L3
    limes_per_bundle = 3 # 3 for $1.00
    cost_per_bundle = 1.00 # $1.00
    total_cost_limes = total_limes_needed / limes_per_bundle * cost_per_bundle

    # FA
    answer = total_cost_limes
    return answer