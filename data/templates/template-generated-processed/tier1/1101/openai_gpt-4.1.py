def solve():
    """Index: 1101.
    Returns: the sum of the ages of Beckett, Olaf, Shannen, and Jack.
    """
    # L1
    beckett_age = 12 # Beckett is 12
    olaf_younger_by = 3 # three years younger than Olaf
    olaf_age = beckett_age + olaf_younger_by

    # L2
    shannen_younger_by = 2 # Shannen is two years younger than Olaf
    shannen_age = olaf_age - shannen_younger_by

    # L3
    jack_base = 5 # Jack is five more than twice as old as Shannen
    jack_multiplier = 2 # twice as old as Shannen
    jack_age = jack_base + (jack_multiplier * shannen_age)

    # L4
    total_age = beckett_age + olaf_age + shannen_age + jack_age

    # FA
    answer = total_age
    return answer