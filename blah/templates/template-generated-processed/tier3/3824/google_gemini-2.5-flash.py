def solve():
    """Index: 3824.
    Returns: the total amount of money Maria gave her three friends.
    """
    # L1
    rene_money = 300 # Rene received $300
    florence_multiplier = 3 # three times as much money as Maria's cousin Rene
    florence_money = florence_multiplier * rene_money

    # L2
    half_divisor = 2 # half of what she gave to Florence
    isha_money = florence_money / half_divisor

    # L3
    total_money_given_to_friends = isha_money + florence_money + rene_money

    # FA
    answer = total_money_given_to_friends
    return answer