from fractions import Fraction

def solve():
    """Index: 3603.
    Returns: the amount of profit each person received.
    """
    # L1
    robi_contribution = 4000 # Robi contributed $4000
    rudy_extra_fraction = Fraction(1, 4) # 1/4 more money than Robi
    rudy_extra_money = rudy_extra_fraction * robi_contribution

    # L2
    rudy_total_contribution = robi_contribution + rudy_extra_money

    # L3
    total_contribution = rudy_total_contribution + robi_contribution

    # L4
    profit_percentage_numerator = 20 # 20 percent of the total amount
    profit_percentage_denominator = 100 # 20 percent of the total amount
    profit_percentage = Fraction(profit_percentage_numerator, profit_percentage_denominator)
    total_profit = profit_percentage * total_contribution

    # L5
    num_partners = 2 # decided to share the profits equally
    profit_per_person = total_profit / num_partners

    # FA
    answer = profit_per_person
    return answer