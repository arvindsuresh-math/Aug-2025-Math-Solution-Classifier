def solve():
    """Index: 1668.
    Returns: the number of rocks in the bucket.
    """
    # L1
    total_money = 60 # he makes $60 off the sale
    price_per_pound = 4 # $4 for every pound of rocks
    total_pounds = total_money / price_per_pound

    # L2
    avg_weight_per_rock = 1.5 # average weight of a rock is 1.5 pounds
    num_rocks = total_pounds / avg_weight_per_rock

    # FA
    answer = num_rocks
    return answer