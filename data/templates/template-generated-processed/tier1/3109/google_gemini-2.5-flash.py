def solve():
    """Index: 3109.
    Returns: the number of cookies remaining in the jar.
    """
    # L1
    lou_sr_initial_take = 3 # took 3 cookies out of the cookie jar
    lou_sr_second_take = 3 # took another 3 cookies out of the jar
    lou_sr_put_back = 2 # put the other two cookies back
    lou_sr_net_removed = lou_sr_initial_take + lou_sr_second_take - lou_sr_put_back

    # L2
    louie_jr_take = 7 # took seven cookies out of the jar
    total_removed = lou_sr_net_removed + louie_jr_take

    # L3
    remaining_cookies = total_removed

    # FA
    answer = remaining_cookies
    return answer