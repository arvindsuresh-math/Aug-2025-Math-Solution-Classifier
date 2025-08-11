def solve():
    """Index: 4820.
    Returns: the amount of soda Danny has left, expressed as a percentage of a bottle.
    """
    # L1
    drank_bottle_count = 1 # one bottle
    drank_percentage_decimal = 0.9 # 90% of one bottle
    soda_drank = drank_bottle_count * drank_percentage_decimal

    # L2
    friends_count = 2 # other two bottles
    given_percentage_decimal = 0.7 # 70% of the other two bottles
    bottles_per_friend = 1 # WK
    soda_given_away = friends_count * bottles_per_friend * given_percentage_decimal

    # L3
    total_bottles = 3 # 3 bottles of soda
    remaining_soda_decimal = total_bottles - soda_drank - soda_given_away
    percentage_factor = 100 # WK
    remaining_soda_percentage = remaining_soda_decimal * percentage_factor

    # FA
    answer = remaining_soda_percentage
    return answer