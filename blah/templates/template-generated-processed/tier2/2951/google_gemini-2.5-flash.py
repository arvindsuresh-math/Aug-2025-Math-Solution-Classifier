def solve():
    """Index: 2951.
    Returns: how much more Anna made from plain lemonade than strawberry lemonade.
    """
    # L1
    num_plain_lemonade_glasses = 36 # 36 glasses of plain lemonade
    price_plain_lemonade_per_glass = 0.75 # $0.75 each
    earnings_plain_lemonade = num_plain_lemonade_glasses * price_plain_lemonade_per_glass

    # L2
    earnings_strawberry_lemonade = 16 # $16 total from selling strawberry lemonade
    difference_in_earnings = earnings_plain_lemonade - earnings_strawberry_lemonade

    # FA
    answer = difference_in_earnings
    return answer