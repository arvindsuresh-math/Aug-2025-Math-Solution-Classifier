def solve():
    """Index: 1101.
    Returns: the sum of the ages of all 4 people.
    """
    # L1
    beckett_age = 12 # Beckett is 12
    years_younger_than_olaf = 3 # three years younger than Olaf
    olaf_age = beckett_age + years_younger_than_olaf

    # L2
    years_younger_than_olaf_shannen = 2 # two years younger than Olaf
    shannen_age = olaf_age - years_younger_than_olaf_shannen

    # L3
    jack_more_than_twice_shannen = 5 # five more
    twice_multiplier = 2 # twice as old as Shannen
    jack_age = jack_more_than_twice_shannen + (twice_multiplier * shannen_age)

    # L4
    total_age_sum = beckett_age + olaf_age + shannen_age + jack_age

    # FA
    answer = total_age_sum
    return answer