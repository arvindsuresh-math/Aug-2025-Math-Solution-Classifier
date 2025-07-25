from fractions import Fraction

def solve():
    """Index: 4121.
    Returns: the probability that all three ingredients will be good.
    """
    # L1
    total_percentage = 100 # WK
    spoiled_milk_percentage = 20 # 20% of the bottles of milk are spoiled
    fresh_milk_percentage = total_percentage - spoiled_milk_percentage

    # L2
    rotten_eggs_percentage = 60 # 60% of the eggs are rotten
    good_eggs_percentage = total_percentage - rotten_eggs_percentage

    # L3
    weevils_flour_numerator = 1 # 1/4 of the cannisters of flour have weevils
    weevils_flour_denominator = 4 # 1/4 of the cannisters of flour have weevils
    whole_unit_value = 1 # WK
    good_flour_fraction_obj = Fraction(whole_unit_value) - Fraction(weevils_flour_numerator, weevils_flour_denominator)
    good_flour_numerator = good_flour_fraction_obj.numerator
    good_flour_denominator = good_flour_fraction_obj.denominator

    # L4
    percentage_multiplier = 100 # WK
    good_flour_percentage = (good_flour_numerator / good_flour_denominator) * percentage_multiplier

    # L5
    fresh_milk_decimal = fresh_milk_percentage / total_percentage
    good_eggs_decimal = good_eggs_percentage / total_percentage
    good_flour_decimal = good_flour_percentage / total_percentage
    overall_good_probability_decimal = fresh_milk_decimal * good_eggs_decimal * good_flour_decimal
    overall_good_probability_percentage = overall_good_probability_decimal * total_percentage

    # FA
    answer = overall_good_probability_percentage
    return answer