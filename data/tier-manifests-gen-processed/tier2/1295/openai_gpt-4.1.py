def solve():
    """Index: 1295.
    Returns: the total amount Lilia earned after selling 14 peaches.
    """
    # L1
    peaches_friends = 10 # sold 10 peaches to her friends
    price_per_peach_friends = 2 # $2 each
    earnings_friends = peaches_friends * price_per_peach_friends

    # L2
    peaches_relatives = 4 # 4 other peaches were sold to her relatives
    price_per_peach_relatives = 1.25 # $1.25 each
    earnings_relatives = peaches_relatives * price_per_peach_relatives

    # L3
    total_earnings = earnings_friends + earnings_relatives

    # FA
    answer = total_earnings
    return answer