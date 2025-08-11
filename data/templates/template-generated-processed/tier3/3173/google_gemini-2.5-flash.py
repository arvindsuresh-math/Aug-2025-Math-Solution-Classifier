def solve():
    """Index: 3173.
    Returns: the number of baseball cards Phil has left.
    """
    # L1
    pack_size = 20 # twenty each week
    weeks_per_year = 52 # 52 weeks in a year
    initial_cards = pack_size * weeks_per_year

    # L2
    loss_divisor = 2 # loses half of them
    remaining_cards = initial_cards / loss_divisor

    # FA
    answer = remaining_cards
    return answer