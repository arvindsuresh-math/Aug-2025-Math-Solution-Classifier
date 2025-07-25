def solve():
    """Index: 5969.
    Returns: the number of racers who will run in the final section of the race.
    """
    # L1
    initial_racers = 100 # If 100 racers started the race
    eliminated_first_segment = 10 # 10 racers are eliminated after the first segment
    racers_after_first_segment = initial_racers - eliminated_first_segment

    # L2
    elimination_fraction_denominator_second = 3 # A third of the remaining racers
    eliminated_second_segment = racers_after_first_segment / elimination_fraction_denominator_second

    # L3
    racers_after_second_segment = racers_after_first_segment - eliminated_second_segment

    # L4
    elimination_fraction_denominator_third = 2 # Half of the remaining racers
    eliminated_third_segment = racers_after_second_segment / elimination_fraction_denominator_third

    # L5
    racers_final_segment = racers_after_second_segment - eliminated_third_segment

    # FA
    answer = racers_final_segment
    return answer