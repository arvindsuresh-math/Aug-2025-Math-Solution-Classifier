def solve():
    """Index: 6086.
    Returns: the amount John paid for the candy bars.
    """
    # L1
    total_candy_bars = 20 # John buys 20 candy bars
    dave_paid_bars = 6 # Dave pays for 6 of them
    john_paid_bars = total_candy_bars - dave_paid_bars

    # L2
    candy_bar_cost = 1.50 # each candy bar costs $1.50
    john_total_payment = john_paid_bars * candy_bar_cost

    # FA
    answer = john_total_payment
    return answer