from fractions import Fraction

def solve():
    """Index: 4066.
    Returns: the total number of marbles Cleo had on the third day.
    """
    # L1
    initial_marbles = 30 # 30 of their marbles
    fraction_taken_day2 = Fraction(3, 5) # 3/5 of the marbles
    marbles_taken_day2 = fraction_taken_day2 * initial_marbles

    # L2
    num_people_sharing = 2 # divided them equally
    marbles_per_person_day2 = marbles_taken_day2 / num_people_sharing

    # L3
    marbles_remaining_jar_day3_start = initial_marbles - marbles_taken_day2

    # L4
    fraction_cleo_took_day3 = Fraction(1, 2) # 1/2 of the marbles remaining
    marbles_cleo_took_day3 = fraction_cleo_took_day3 * marbles_remaining_jar_day3_start

    # L5
    total_marbles_cleo_day3 = marbles_cleo_took_day3 + marbles_per_person_day2

    # FA
    answer = total_marbles_cleo_day3
    return answer