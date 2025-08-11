def solve():
    """Index: 7111.
    Returns: the number of feathers Jerry has left.
    """
    # L1
    hawk_feathers = 6 # six hawk feathers
    eagle_multiplier = 17 # 17 times as many eagle feathers as hawk feathers
    eagle_feathers = eagle_multiplier * hawk_feathers

    # L2
    total_feathers_initial = eagle_feathers + hawk_feathers

    # L3
    feathers_given_to_sister = 10 # gives 10 feathers to his sister
    feathers_after_giving_to_sister = total_feathers_initial - feathers_given_to_sister

    # L4
    half_divisor = 2 # sells half the remaining feathers
    feathers_left = feathers_after_giving_to_sister / half_divisor

    # FA
    answer = feathers_left
    return answer