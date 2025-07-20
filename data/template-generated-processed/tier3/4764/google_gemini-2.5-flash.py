from fractions import Fraction

def solve():
    """Index: 4764.
    Returns: the recommended number of cups of water per week.
    """
    # L1
    increase_percentage = Fraction(40, 100) # 40% more cups of water
    current_cups_per_week = 15 # currently drinking 15 cups of water every week
    additional_cups = increase_percentage * current_cups_per_week

    # L2
    recommended_cups_per_week = additional_cups + current_cups_per_week

    # FA
    answer = recommended_cups_per_week
    return answer