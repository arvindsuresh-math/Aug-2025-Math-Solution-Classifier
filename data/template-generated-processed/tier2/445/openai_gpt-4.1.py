def solve():
    """Index: 445.
    Returns: the total amount Carla spent on 2 bags of candy.
    """
    # L1
    bag_price = 6.00 # Each bag was $6.00
    discount_percent = 0.75 # was 75% off
    discount_amount = bag_price * discount_percent

    # L2
    discounted_bag_price = bag_price - discount_amount

    # L3
    num_bags = 2 # bought 2 bags
    total_cost = discounted_bag_price * num_bags

    # FA
    answer = total_cost
    return answer