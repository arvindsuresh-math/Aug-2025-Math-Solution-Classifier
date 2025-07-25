def solve():
    """Index: 702.
    Returns: the amount of money left in Lily's account after her purchases.
    """
    # L1
    initial_balance = 55 # $55 in her account
    shirt_cost = 7 # spent $7 on a shirt
    after_shirt = initial_balance - shirt_cost

    # L2
    times_shirt_cost = 3 # thrice as much as she spent on a shirt
    other_store_spent = shirt_cost * times_shirt_cost

    # L3
    final_balance = after_shirt - other_store_spent

    # FA
    answer = final_balance
    return answer