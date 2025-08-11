def solve():
    """Index: 5312.
    Returns: the amount of money Kekai has left after giving half to his parents.
    """
    # L1
    num_shirts = 5 # Kekai sells 5 shirts
    shirt_price = 1 # Each shirt sells for $1
    money_from_shirts = num_shirts * shirt_price

    # L2
    num_pants = 5 # and 5 pairs of pants
    pants_price = 3 # each pair of pants sells for $3
    money_from_pants = num_pants * pants_price

    # L3
    total_money_earned = money_from_shirts + money_from_pants

    # L4
    share_divisor = 2 # half of the money
    money_left = total_money_earned / share_divisor

    # FA
    answer = money_left
    return answer