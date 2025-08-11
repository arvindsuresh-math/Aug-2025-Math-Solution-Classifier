def solve():
    """Index: 6936.
    Returns: the total worth of all the produce stocked.
    """
    # L1
    asparagus_bundles = 60 # 60 bundles of asparagus
    asparagus_price_per_bundle = 3.00 # $3.00 each
    total_asparagus_cost = asparagus_bundles * asparagus_price_per_bundle

    # L2
    grape_boxes = 40 # 40 boxes of grapes
    grape_price_per_box = 2.50 # $2.50 each
    total_grape_cost = grape_boxes * grape_price_per_box

    # L3
    num_apples = 700 # 700 apples
    apple_price_per_apple = 0.50 # $0.50 each
    total_apple_cost = num_apples * apple_price_per_apple

    # L4
    total_produce_worth = total_asparagus_cost + total_grape_cost + total_apple_cost

    # FA
    answer = total_produce_worth
    return answer