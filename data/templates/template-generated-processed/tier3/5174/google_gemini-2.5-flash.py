from fractions import Fraction

def solve():
    """Index: 5174.
    Returns: the average number of hours Alex needs to hang upside down each month.
    """
    # L1
    required_height = 54 # 54 inches tall
    current_height = 48 # 48 inches tall this year
    height_shortfall_initial = required_height - current_height

    # L2
    natural_growth_per_month = Fraction(1, 3) # 1/3 of an inch per month
    months_per_year = 12 # WK
    natural_growth_per_year = months_per_year * natural_growth_per_month

    # L3
    height_needed_from_hanging = height_shortfall_initial - natural_growth_per_year

    # L4
    growth_per_hour_hanging = Fraction(1, 12) # 1/12 of an inch
    total_hanging_hours_needed = height_needed_from_hanging / growth_per_hour_hanging

    # L5
    hanging_hours_per_month = total_hanging_hours_needed / months_per_year

    # FA
    answer = hanging_hours_per_month
    return answer