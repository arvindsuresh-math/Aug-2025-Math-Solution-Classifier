def solve():
    """Index: 3573.
    Returns: the number of candies Bob bought.
    """
    # L1
    emily_candies = 6 # Emily bought 6 candies
    jennifer_multiplier_emily = 2 # twice as many candies as Emily
    jennifer_candies = emily_candies * jennifer_multiplier_emily

    # L3
    jennifer_multiplier_bob = 3 # three times as many as Bob bought
    bob_candies = jennifer_candies / jennifer_multiplier_bob

    # FA
    answer = bob_candies
    return answer