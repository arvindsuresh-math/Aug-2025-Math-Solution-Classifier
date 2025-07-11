from fractions import Fraction

def solve():
    """Index: 483.
    Returns: how much less Andy weighs now than at the beginning of the year.
    """
    # L1
    initial_weight = 156 # Andy started out the year weighing 156 pounds
    weight_gain = 36 # gained 36 pounds
    weight_after_gain = initial_weight + weight_gain

    # L2
    fraction_lost_numerator = 1 # lost an eighth of his weight
    fraction_lost_denominator = 8 # lost an eighth of his weight
    weight_lost_fraction = Fraction(fraction_lost_numerator, fraction_lost_denominator)
    weight_lost_per_month = weight_lost_fraction * weight_after_gain

    # L3
    months_exercising = 3 # Over the next 3 months
    total_weight_lost = weight_lost_per_month * months_exercising

    # L4
    current_weight = weight_after_gain - total_weight_lost

    # L5
    weight_difference = initial_weight - current_weight

    # FA
    answer = weight_difference
    return answer