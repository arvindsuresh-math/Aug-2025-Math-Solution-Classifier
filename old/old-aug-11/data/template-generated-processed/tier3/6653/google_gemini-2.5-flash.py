def solve():
    """Index: 6653.
    Returns: the number of dozen cupcakes Lillian can bake and ice.
    """
    # L1
    bags_bought = 2 # buys 2 bags of sugar
    cups_per_bag = 6 # Each bag of sugar contains 6 cups
    sugar_from_bags = bags_bought * cups_per_bag

    # L2
    initial_sugar = 3 # only has 3 cups of sugar at home
    total_sugar = sugar_from_bags + initial_sugar

    # L3
    sugar_for_batter_per_dozen = 1 # 1 cup of sugar per 12 cupcakes
    sugar_for_frosting_per_dozen = 2 # 2 cups of sugar to make enough frosting for a dozen cupcakes
    total_sugar_per_dozen = sugar_for_batter_per_dozen + sugar_for_frosting_per_dozen

    # L4
    dozen_cupcakes_possible = total_sugar / total_sugar_per_dozen

    # FA
    answer = dozen_cupcakes_possible
    return answer