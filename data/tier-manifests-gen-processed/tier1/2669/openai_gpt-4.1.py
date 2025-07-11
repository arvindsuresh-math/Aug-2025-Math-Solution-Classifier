def solve():
    """Index: 2669.
    Returns: the number of TVs Beatrice looked at on the auction site.
    """
    # L1
    num_tvs_in_person = 8 # 8 TVs at one store in person
    online_multiplier = 3 # three times as many TVs at an online store
    num_tvs_online = online_multiplier * num_tvs_in_person

    # L2
    num_tvs_first_two = num_tvs_in_person + num_tvs_online

    # L3
    total_tvs = 42 # Beatrice looked at 42 TVs in all
    num_tvs_auction = total_tvs - num_tvs_first_two

    # FA
    answer = num_tvs_auction
    return answer