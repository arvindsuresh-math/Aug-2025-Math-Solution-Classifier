from fractions import Fraction

def solve():
    """Index: 6857.
    Returns: the total number of fish Archer caught that day.
    """
    # L1
    initial_catch = 8 # Archer caught eight fish
    additional_second_round_fish = 12 # caught 12 more fish in the second round
    second_round_catch = additional_second_round_fish + initial_catch

    # L2
    total_two_rounds_catch = second_round_catch + initial_catch

    # L3
    percentage_more_third_round = Fraction(60, 100) # 60% more fish
    additional_third_round_fish = percentage_more_third_round * second_round_catch

    # L4
    third_round_total_catch = additional_third_round_fish + second_round_catch

    # L5
    total_fish_that_day = total_two_rounds_catch + third_round_total_catch

    # FA
    answer = total_fish_that_day
    return answer