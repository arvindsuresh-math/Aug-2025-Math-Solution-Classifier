def solve():
    """Index: 1744.
    Returns: the total amount of money the farmer got from selling all crops.
    """
    # L1
    total_potatoes = 250 # 250 potatoes
    potatoes_per_bundle = 25 # bundled them in twenty-five's
    num_potato_bundles = total_potatoes / potatoes_per_bundle

    # L2
    price_per_potato_bundle = 1.90 # sold each bundle for $1.90
    total_potato_revenue = price_per_potato_bundle * num_potato_bundles

    # L3
    total_carrots = 320 # 320 carrots
    carrots_per_bundle = 20 # bundled them in twenty's
    num_carrot_bundles = total_carrots / carrots_per_bundle

    # L4
    price_per_carrot_bundle = 2 # sold each bundle for $2
    total_carrot_revenue = price_per_carrot_bundle * num_carrot_bundles

    # L5
    total_revenue = total_potato_revenue + total_carrot_revenue

    # FA
    answer = total_revenue
    return answer