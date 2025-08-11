def solve():
    """Index: 1335.
    Returns: the total number of apples Lexie and Tom collected altogether.
    """
    # L1
    lexie_apples = 12 # Lexie picked 12 apples
    tom_multiplier = 2 # Tom picked twice as many apples
    tom_apples = lexie_apples * tom_multiplier

    # L2
    total_apples = lexie_apples + tom_apples

    # FA
    answer = total_apples
    return answer