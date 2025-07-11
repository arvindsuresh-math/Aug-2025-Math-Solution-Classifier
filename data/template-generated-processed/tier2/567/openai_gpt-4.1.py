def solve():
    """Index: 567.
    Returns: the total amount of money Lilith will have to find to buy her friend the birthday gift after selling her water bottles at the reduced cost.
    """
    # L1
    bottles_per_dozen = 12 # a dozen has 12 water bottles
    num_dozens = 5 # 5 dozen water bottles
    total_bottles = bottles_per_dozen * num_dozens

    # L2
    original_price_per_bottle = 2 # $2 each
    original_total_needed = total_bottles * original_price_per_bottle

    # L3
    reduced_price_per_bottle = 1.85 # reduced price to $1.85
    reduced_total = reduced_price_per_bottle * total_bottles

    # L4
    money_to_find = original_total_needed - reduced_total

    # FA
    answer = money_to_find
    return answer