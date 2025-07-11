def solve():
    """Index: 507.
    Returns: the total amount James paid for the steaks.
    """
    # L1
    total_pounds = 20 # he buys 20 pounds
    buy_one_get_one_free_divisor = 2 # buy one get one free
    paid_pounds = total_pounds / buy_one_get_one_free_divisor

    # L2
    price_per_pound = 15 # $15 per pound
    total_cost = paid_pounds * price_per_pound

    # FA
    answer = total_cost
    return answer