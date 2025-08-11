from fractions import Fraction

def solve():
    """Index: 1083.
    Returns: the total production of television by the factory in the second year.
    """
    # L1
    production_rate_per_day = 10 # constant rate of 10 per day
    days_in_year = 365 # WK
    total_production_first_year = production_rate_per_day * days_in_year

    # L2
    reduction_percentage = Fraction(10, 100) # reduced the total production by 10 percent
    reduction_amount = reduction_percentage * total_production_first_year

    # L3
    total_production_second_year = total_production_first_year - reduction_amount

    # FA
    answer = total_production_second_year
    return answer