from fractions import Fraction

def solve():
    """Index: 1031.
    Returns: the number of people who remained to see the end of the game.
    """
    # L1
    total_people_start = 600 # There were 600 people in the stadium
    initial_girls = 240 # 240 girls at the beginning of the game
    initial_boys = total_people_start - initial_girls

    # L2
    boys_left_fraction = Fraction(1, 4) # one-fourth of the boys
    boys_left_early = initial_boys * boys_left_fraction

    # L3
    girls_left_fraction = Fraction(1, 8) # one-eighth of the girls
    girls_left_early = initial_girls * girls_left_fraction

    # L4
    total_people_left_early = boys_left_early + girls_left_early

    # L5
    people_remained = total_people_start - total_people_left_early

    # FA
    answer = people_remained
    return answer