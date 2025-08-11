def solve():
    """Index: 1019.
    Returns: the number of cookies accidentally thrown on the floor.
    """
    # L1
    alice_initial = 74 # Alice baked 74 chocolate chip cookies
    bob_initial = 7 # Bob baked 7 peanut butter cookies
    initial_total = alice_initial + bob_initial

    # L2
    alice_more = 5 # Alice baked 5 more cookies
    bob_more = 36 # Bob baked 36 more
    more_total = alice_more + bob_more

    # L3
    total_baked = initial_total + more_total

    # L4
    edible_cookies = 93 # they had 93 edible cookies at the end
    thrown_away = total_baked - edible_cookies

    # FA
    answer = thrown_away
    return answer