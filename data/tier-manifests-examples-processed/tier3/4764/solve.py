from fractions import Fraction

def solve():
    """Index: 4764.
    Returns: the recommended number of cups of water per week.
    """
    # L1
    increase_percentage = Fraction(40, 100) # 40% more cups of water
    current_intake = 15 # currently drinking 15 cups of water
    additional_cups = increase_percentage * current_intake

    # L2
    recommended_cups = additional_cups + current_intake

    # FA
    answer = recommended_cups
    return answer