def solve():
    """Index: 130.
    Returns: the number of seashells Ali had left after all transactions.
    """
    # L1
    initial_seashells = 180 # Ali started with 180 seashells
    seashells_given_friends = 40 # gave away 40 seashells to his friends
    after_friends = initial_seashells - seashells_given_friends

    # L2
    seashells_given_brothers = 30 # gave 30 seashells to his brothers
    after_brothers = after_friends - seashells_given_brothers

    # L3
    sold_fraction_denominator = 2 # sold half of the remaining seashells
    seashells_sold = after_brothers / sold_fraction_denominator

    # L4
    seashells_left = after_brothers - seashells_sold

    # FA
    answer = seashells_left
    return answer