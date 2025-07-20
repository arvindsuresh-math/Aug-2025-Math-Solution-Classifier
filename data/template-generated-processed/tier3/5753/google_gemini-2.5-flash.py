def solve():
    """Index: 5753.
    Returns: the number of girls with short hair.
    """
    # L1
    total_people = 55 # 55 people at the track meet
    num_boys = 30 # 30 of them are boys
    num_girls = total_people - num_boys

    # L2
    three_fifths_numerator = 3 # Three fifths of the girls
    three_fifths_denominator = 5 # Three fifths of the girls
    girls_with_long_hair = (num_girls / three_fifths_denominator) * three_fifths_numerator

    # L3
    girls_with_short_hair = num_girls - girls_with_long_hair

    # FA
    answer = girls_with_short_hair
    return answer