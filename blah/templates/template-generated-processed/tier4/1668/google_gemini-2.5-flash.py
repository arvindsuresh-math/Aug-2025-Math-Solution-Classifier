def solve():
    """Index: 1668.
    Returns: the number of rocks in the bucket.
    """
    # L1
    total_money_made = 60 # he makes $60 off the sale
    price_per_pound = 4 # $4 for every pound of rocks
    total_pounds_of_rocks = total_money_made / price_per_pound

    # L2
    average_weight_per_rock = 1.5 # average weight of a rock is 1.5 pounds
    num_rocks = total_pounds_of_rocks / average_weight_per_rock

    # FA
    answer = num_rocks
    return answer