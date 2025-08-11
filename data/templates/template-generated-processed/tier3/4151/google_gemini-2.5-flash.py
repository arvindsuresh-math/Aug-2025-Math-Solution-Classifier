def solve():
    """Index: 4151.
    Returns: the total money Jenny makes in cents.
    """
    # L1
    num_cans = 20 # 20 cans
    weight_per_can = 2 # each can weighs 2 ounces
    weight_of_cans = num_cans * weight_per_can

    # L2
    total_capacity = 100 # Jenny can carry a total of 100 ounces
    capacity_for_bottles = total_capacity - weight_of_cans

    # L3
    weight_per_bottle = 6 # Each bottle weighs 6 ounces
    num_bottles = capacity_for_bottles / weight_per_bottle

    # L4
    cents_per_bottle = 10 # 10 cents per bottle
    earnings_bottles = num_bottles * cents_per_bottle

    # L5
    cents_per_can = 3 # 3 cents per can
    earnings_cans = num_cans * cents_per_can

    # L6
    total_earnings = earnings_bottles + earnings_cans

    # FA
    answer = total_earnings
    return answer