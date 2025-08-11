def solve():
    """Index: 7041.
    Returns: 10 times the average number of letters in both names.
    """
    # L1
    elida_letters = 5 # Elida has 5 letters
    twice_factor = 2 # twice the number
    twice_elida_letters = twice_factor * elida_letters

    # L2
    adrianna_less_amount = 2 # 2 less than twice the number
    adrianna_letters = twice_elida_letters - adrianna_less_amount

    # L3
    total_letters = adrianna_letters + elida_letters

    # L4
    num_names = 2 # WK
    average_letters = total_letters / num_names

    # L5
    multiplier = 10 # 10 times
    final_result = multiplier * average_letters

    # FA
    answer = final_result
    return answer