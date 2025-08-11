def solve():
    """Index: 7145.
    Returns: the profit from selling the gold cube.
    """
    # L1
    side_length = 6 # 6 cm on each side
    cube_volume = side_length * side_length * side_length

    # L2
    gold_density = 19 # 19 grams per cubic centimeter
    gold_mass = cube_volume * gold_density

    # L3
    cost_per_gram = 60 # $60 per gram
    total_cost = cost_per_gram * gold_mass

    # L4
    sell_multiplier = 1.5 # 1.5 times its gold value
    total_revenue = total_cost * sell_multiplier

    # L5
    profit = total_revenue - total_cost

    # FA
    answer = profit
    return answer