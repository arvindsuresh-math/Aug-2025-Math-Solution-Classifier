def solve():
    """Index: 5223.
    Returns: the total amount Spongebob will earn for the day.
    """
    # L1
    num_burgers = 30 # sells 30 burgers
    price_per_burger = 2 # for $2 each
    earnings_burgers = num_burgers * price_per_burger

    # L2
    num_fries = 12 # 12 large fries
    price_per_fry = 1.5 # for $1.5
    earnings_fries = num_fries * price_per_fry

    # L3
    total_earnings = earnings_burgers + earnings_fries

    # FA
    answer = total_earnings
    return answer