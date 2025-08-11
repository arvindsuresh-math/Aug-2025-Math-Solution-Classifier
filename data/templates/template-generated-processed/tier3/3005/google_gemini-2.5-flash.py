from fractions import Fraction

def solve():
    """Index: 3005.
    Returns: the total amount of money Aitana and Jayda spent together.
    """
    # L1
    jayda_spent = 400 # Jayda spent $400
    aitana_extra_fraction = Fraction(2, 5) # 2/5 times more money
    aitana_extra_money = aitana_extra_fraction * jayda_spent

    # L2
    aitana_total_spent = jayda_spent + aitana_extra_money

    # L3
    total_spent = jayda_spent + aitana_total_spent

    # FA
    answer = total_spent
    return answer