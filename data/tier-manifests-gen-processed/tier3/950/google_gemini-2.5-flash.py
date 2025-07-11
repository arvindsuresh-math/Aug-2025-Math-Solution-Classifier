from fractions import Fraction

def solve():
    """Index: 950.
    Returns: Theodore's total monthly earnings after taxes.
    """
    # L1
    num_stone_statues = 10 # 10 stone statues
    cost_stone_statue = 20 # A stone statue costs $20
    earnings_stone_statues = num_stone_statues * cost_stone_statue

    # L2
    num_wooden_statues = 20 # 20 wooden statues
    cost_wooden_statue = 5 # a wooden statue costs $5
    earnings_wooden_statues = num_wooden_statues * cost_wooden_statue

    # L3
    total_earnings_before_tax = earnings_stone_statues + earnings_wooden_statues

    # L4
    tax_percentage_numerator = 10 # 10 percent of his total earnings in taxes
    tax_percentage_denominator = 100 # 10 percent of his total earnings in taxes
    tax_percentage = Fraction(tax_percentage_numerator, tax_percentage_denominator)
    tax_amount = total_earnings_before_tax * tax_percentage

    # L5
    total_monthly_earnings = total_earnings_before_tax - tax_amount

    # FA
    answer = total_monthly_earnings
    return answer