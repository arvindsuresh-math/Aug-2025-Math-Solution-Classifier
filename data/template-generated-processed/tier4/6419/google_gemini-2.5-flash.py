def solve():
    """Index: 6419.
    Returns: the maximum number of ounces of food Amber can get.
    """
    # L1
    total_money = 7 # $7
    candy_bag_cost = 1 # $1
    num_candy_bags = total_money / candy_bag_cost

    # L2
    chips_bag_cost = 1.40 # $1.40
    num_chip_bags = total_money / chips_bag_cost

    # L3
    candy_ounces_per_bag = 12 # 12 ounces each
    total_candy_ounces = num_candy_bags * candy_ounces_per_bag

    # L4
    chips_ounces_per_bag = 17 # 17 ounces each
    total_chip_ounces = num_chip_bags * chips_ounces_per_bag

    # L5
    max_ounces = max(total_chip_ounces, total_candy_ounces)

    # FA
    answer = max_ounces
    return answer