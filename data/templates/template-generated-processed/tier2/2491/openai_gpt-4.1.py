def solve():
    """Index: 2491.
    Returns: the total money the candy store made from sales.
    """
    # L1
    fudge_pounds = 20 # 20 pounds of fudge
    fudge_price_per_pound = 2.50 # $2.50/pound
    fudge_total = fudge_pounds * fudge_price_per_pound

    # L2
    truffle_dozens = 5 # 5 dozen chocolate truffles
    dozen = 12 # WK
    truffle_count = truffle_dozens * dozen

    # L3
    truffle_price_each = 1.50 # $1.50 each
    truffle_total = truffle_count * truffle_price_each

    # L4
    pretzel_dozens = 3 # 3 dozen chocolate-covered pretzels
    pretzel_count = pretzel_dozens * dozen

    # L5
    pretzel_price_each = 2.00 # $2.00 each
    pretzel_total = pretzel_count * pretzel_price_each

    # L6
    total_sales = fudge_total + truffle_total + pretzel_total

    # FA
    answer = total_sales
    return answer