from fractions import Fraction

def solve():
    """Index: 1529.
    Returns: the number of females who wear glasses.
    """
    # L1
    total_population = 5000 # 5,000 people live in a small town
    male_population = 2000 # 2,000 males live in that town
    female_population = total_population - male_population

    # L2
    percentage_wear_glasses = Fraction(30, 100) # Thirty percent of the female population wears glasses
    females_wear_glasses = percentage_wear_glasses * female_population

    # FA
    answer = females_wear_glasses
    return answer