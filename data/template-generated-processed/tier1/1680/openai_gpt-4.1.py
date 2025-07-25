def solve():
    """Index: 1680.
    Returns: the number of pieces of candy remaining in the bowl.
    """
    # L1
    initial_candy = 349 # 349 pieces of candy in a bowl
    talitha_took = 108 # Talitha took 108 pieces
    after_talitha = initial_candy - talitha_took
    solomon_took = 153 # Solomon took 153 pieces
    remaining_candy = after_talitha - solomon_took

    # FA
    answer = remaining_candy
    return answer