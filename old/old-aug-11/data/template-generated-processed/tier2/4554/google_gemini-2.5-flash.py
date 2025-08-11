def solve():
    """Index: 4554.
    Returns: the total cost Michael will spend at the market buying fruit.
    """
    # L1
    fruit_per_pie = 3 # called for 3 pounds of fruit each
    num_peach_pies = 5 # 5 peach pies
    pounds_peaches = fruit_per_pie * num_peach_pies

    # L2
    num_apple_pies = 4 # 4 apple pies
    pounds_apples = fruit_per_pie * num_apple_pies

    # L3
    num_blueberry_pies = 3 # 3 blueberry pies
    pounds_blueberries = fruit_per_pie * num_blueberry_pies

    # L4
    total_pounds_apples_blueberries = pounds_apples + pounds_blueberries

    # L5
    cost_apples_blueberries_per_pound = 1.00 # $1.00 per pound for both blueberries and apples
    cost_apples_blueberries = total_pounds_apples_blueberries * cost_apples_blueberries_per_pound

    # L6
    cost_peaches_per_pound = 2.00 # peaches each cost $2.00 per pound
    cost_peaches = pounds_peaches * cost_peaches_per_pound

    # L7
    total_cost = cost_apples_blueberries + cost_peaches

    # FA
    answer = total_cost
    return answer