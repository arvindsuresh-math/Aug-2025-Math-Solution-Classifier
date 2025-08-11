def solve():
    """Index: 6995.
    Returns: the number of rats Bill bought.
    """
    # L2
    total_animals = 70 # Bill thought he bought 70 chihuahuas
    rats_multiplier = 6 # number of rats was 6 times the number of chihuahuas
    combined_coefficient = rats_multiplier + 1

    # L3
    num_chihuahuas = total_animals / combined_coefficient

    # L4
    num_rats = rats_multiplier * num_chihuahuas

    # FA
    answer = num_rats
    return answer