def solve():
    """Index: 358.
    Returns: the total number of marbles Carl is going to put in the jar.
    """
    # L1
    initial_marbles_taken_out = 12 # He takes out 12 marbles
    lost_fraction_denominator = 2 # 1/2 the marbles get lost
    marbles_not_lost = initial_marbles_taken_out / lost_fraction_denominator

    # L2
    more_marbles_taken_out = 10 # Carl takes out 10 more marbles
    total_marbles_out_before_new = marbles_not_lost + more_marbles_taken_out

    # L3
    new_marbles_from_mother = 25 # which has 25 marbles in it
    total_marbles_to_put_in_jar = new_marbles_from_mother + total_marbles_out_before_new

    # FA
    answer = total_marbles_to_put_in_jar
    return answer