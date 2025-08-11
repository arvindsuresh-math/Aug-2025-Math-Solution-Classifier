from fractions import Fraction

def solve():
    """Index: 1963.
    Returns: the amount Christine saved this month.
    """
    # L1
    commission_rate = Fraction(12, 100) # 12% commission
    total_sales = 24000 # sold $24000 worth of items
    commission_earned = commission_rate * total_sales

    # L2
    personal_needs_percentage = Fraction(60, 100) # Sixty percent of all her earning
    allocated_for_personal_needs = personal_needs_percentage * commission_earned

    # L3
    amount_saved = commission_earned - allocated_for_personal_needs

    # FA
    answer = amount_saved
    return answer