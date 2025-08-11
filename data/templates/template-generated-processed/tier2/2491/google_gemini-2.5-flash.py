def solve():
    """Index: 2491.
    Returns: the total money the candy store made.
    """
    # L1
    fudge_pounds = 20 # 20 pounds of fudge
    fudge_price_per_pound = 2.50 # $2.50/pound
    fudge_revenue = fudge_pounds * fudge_price_per_pound

    # L2
    truffle_dozens = 5 # 5 dozen chocolate truffles
    dozen = 12 # WK
    total_truffles = truffle_dozens * dozen

    # L3
    truffle_price_each = 1.50 # $1.50 each
    truffle_revenue = total_truffles * truffle_price_each

    # L4
    pretzel_dozens = 3 # 3 dozen chocolate-covered pretzels
    total_pretzels = pretzel_dozens * dozen

    # L5
    pretzel_price_each = 2.00 # $2.00 each
    pretzel_revenue = total_pretzels * pretzel_price_each

    # L6
    total_revenue = fudge_revenue + truffle_revenue + pretzel_revenue

    # FA
    answer = total_revenue
    return answer