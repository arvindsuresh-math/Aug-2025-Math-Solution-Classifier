def solve():
    """Index: 4160.
    Returns: the number of strawberries Hannah has by the end of April.
    """
    # L1
    strawberries_per_day = 5 # harvests 5 strawberries daily
    days_in_april = 30 # month of April, which has 30 days
    total_harvested_strawberries = strawberries_per_day * days_in_april

    # L2
    given_to_friends = 20 # gives away 20 strawberries to her friends
    strawberries_after_giving = total_harvested_strawberries - given_to_friends

    # L3
    stolen_strawberries = 30 # 30 strawberries are stolen
    strawberries_remaining = strawberries_after_giving - stolen_strawberries

    # FA
    answer = strawberries_remaining
    return answer