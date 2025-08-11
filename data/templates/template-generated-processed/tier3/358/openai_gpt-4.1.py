def solve():
    """Index: 358.
    Returns: the total number of marbles Carl is going to put in the jar after his game.
    """
    # L1
    marbles_taken_out = 12 # Carl takes out 12 marbles to play a game with
    lost_fraction_denominator = 2 # 1/2 the marbles get lost
    marbles_not_lost = marbles_taken_out / lost_fraction_denominator

    # L2
    additional_marbles_taken_out = 10 # Carl takes out 10 more marbles
    marbles_after_second_take = marbles_not_lost + additional_marbles_taken_out

    # L3
    new_marbles_from_mother = 25 # his mother comes home with another bag of marbles for him, which has 25 marbles in it
    total_marbles_to_put_in_jar = new_marbles_from_mother + marbles_after_second_take

    # FA
    answer = total_marbles_to_put_in_jar
    return answer