def solve():
    """Index: 2951.
    Returns: how much more Anna made from plain lemonade than strawberry lemonade.
    """
    # L1
    num_plain_glasses = 36 # 36 glasses
    price_per_plain = 0.75 # $0.75 each
    plain_earnings = num_plain_glasses * price_per_plain

    # L2
    strawberry_earnings = 16 # made $16 total from selling strawberry lemonade
    difference = plain_earnings - strawberry_earnings

    # FA
    answer = difference
    return answer