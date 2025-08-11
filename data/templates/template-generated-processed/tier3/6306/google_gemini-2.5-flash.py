def solve():
    """Index: 6306.
    Returns: the total ounces of apples Marta should buy.
    """
    # L1
    ounces_per_bag = 49 # Each plastic bag in the grocery store can hold 49 ounces of fruit
    num_bags = 3 # buy 3 full bags of fruit
    total_ounces_in_three_bags = ounces_per_bag * num_bags

    # L2
    orange_weight_per_fruit = 3 # the oranges weight 3 ounces
    apple_weight_per_fruit = 4 # The apples weigh four ounces each
    weight_per_pair = orange_weight_per_fruit + apple_weight_per_fruit

    # L3
    num_pairs_of_fruit = total_ounces_in_three_bags / weight_per_pair

    # L4
    ounces_of_apples_to_buy = num_pairs_of_fruit * apple_weight_per_fruit

    # FA
    answer = ounces_of_apples_to_buy
    return answer