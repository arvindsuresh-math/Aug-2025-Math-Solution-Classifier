def solve():
    """Index: 567.
    Returns: the total amount of money Lilith will have to find.
    """
    # L1
    num_dozen_bottles = 5 # five dozen water bottles
    bottles_per_dozen = 12 # WK
    total_bottles = bottles_per_dozen * num_dozen_bottles

    # L2
    original_price_per_bottle = 2 # $2 each
    original_target_money = total_bottles * original_price_per_bottle

    # L3
    reduced_price_per_bottle = 1.85 # $1.85 per water bottle
    money_from_reduced_sales = reduced_price_per_bottle * total_bottles

    # L4
    money_to_find = original_target_money - money_from_reduced_sales

    # FA
    answer = money_to_find
    return answer