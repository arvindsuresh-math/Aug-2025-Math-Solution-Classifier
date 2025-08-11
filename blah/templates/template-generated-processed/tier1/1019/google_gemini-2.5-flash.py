def solve():
    """Index: 1019.
    Returns: the number of cookies accidentally thrown on the floor.
    """
    # L1
    alice_initial_cookies = 74 # Alice baked 74 chocolate chip cookies
    bob_initial_cookies = 7 # Bob baked 7 peanut butter cookies
    initial_baked_cookies = alice_initial_cookies + bob_initial_cookies

    # L2
    alice_additional_cookies = 5 # Alice baked 5 more cookies
    bob_additional_cookies = 36 # Bob baked 36 more
    additional_baked_cookies = alice_additional_cookies + bob_additional_cookies

    # L3
    total_baked_cookies = initial_baked_cookies + additional_baked_cookies

    # L4
    edible_cookies = 93 # they had 93 edible cookies at the end
    thrown_cookies = total_baked_cookies - edible_cookies

    # FA
    answer = thrown_cookies
    return answer