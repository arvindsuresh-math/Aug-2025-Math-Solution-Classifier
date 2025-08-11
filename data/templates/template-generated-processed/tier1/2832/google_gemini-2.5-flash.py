def solve():
    """Index: 2832.
    Returns: the total earnings of the baker.
    """
    # L1
    num_cakes = 453 # 453 cakes
    price_per_cake = 12 # $12
    earnings_cakes = num_cakes * price_per_cake

    # L2
    num_pies = 126 # 126 pies
    price_per_pie = 7 # $7
    earnings_pies = num_pies * price_per_pie

    # L3
    total_earnings = earnings_cakes + earnings_pies

    # FA
    answer = total_earnings
    return answer