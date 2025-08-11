def solve():
    """Index: 2865.
    Returns: the number of smaller boxes of peaches.
    """
    # L1
    peaches_per_basket = 25 # 25 peaches in each basket
    baskets_delivered = 5 # Five baskets of peaches
    total_peaches_delivered = baskets_delivered * peaches_per_basket

    # L2
    initial_peaches_for_l2 = 150 # Value from solution line L2
    peaches_eaten = 5 # The farmers have eaten 5 peaches
    peaches_after_eaten = initial_peaches_for_l2 - peaches_eaten

    # L3
    peaches_for_packing_l3 = 120 # Value from solution line L3
    peaches_per_small_box = 15 # smaller boxes of 15 each
    number_of_boxes = peaches_for_packing_l3 / peaches_per_small_box

    # FA
    answer = number_of_boxes
    return answer