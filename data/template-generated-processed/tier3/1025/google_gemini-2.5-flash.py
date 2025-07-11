from fractions import Fraction

def solve():
    """Index: 1025.
    Returns: the number of parents who disagree with the tuition fee increase.
    """
    # L1
    total_parents = 800 # 800 parents
    agree_percentage = Fraction(20, 100) # 20% of the 800 parents agree
    agreed_parents = total_parents * agree_percentage

    # L2
    disagreed_parents = total_parents - agreed_parents

    # FA
    answer = disagreed_parents
    return answer