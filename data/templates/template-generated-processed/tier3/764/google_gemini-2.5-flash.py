from fractions import Fraction

def solve():
    """Index: 764.
    Returns: the number of calories over the recommended amount.
    """
    # L1
    lunch_fraction_numerator = 3 # three-fourths of her lunch
    lunch_fraction_denominator = 4 # three-fourths of her lunch
    total_lunch_calories = 40 # total amount of food she had prepared for lunch had 40 calories
    calories_eaten = Fraction(lunch_fraction_numerator, lunch_fraction_denominator) * total_lunch_calories

    # L2
    recommended_calories = 25 # recommended calorie intake by the FDA is 25
    excess_calories = calories_eaten - recommended_calories

    # FA
    answer = excess_calories
    return answer