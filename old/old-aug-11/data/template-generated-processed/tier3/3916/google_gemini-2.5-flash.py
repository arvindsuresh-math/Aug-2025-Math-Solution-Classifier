from fractions import Fraction

def solve():
    """Index: 3916.
    Returns: the total money saved by Thomas and Joseph.
    """
    # L1
    saving_years = 6 # six years
    months_per_year = 12 # WK
    thomas_saving_months = saving_years * months_per_year

    # L2
    thomas_monthly_saving = 40 # $40 in the bank every month
    thomas_total_savings = thomas_saving_months * thomas_monthly_saving

    # L3
    joseph_less_fraction = Fraction(2, 5) # 2/5 times less money
    joseph_less_per_month = joseph_less_fraction * thomas_monthly_saving

    # L4
    joseph_monthly_saving = thomas_monthly_saving - joseph_less_per_month

    # L5
    joseph_total_savings = joseph_monthly_saving * thomas_saving_months

    # L6
    total_savings_altogether = thomas_total_savings + joseph_total_savings

    # FA
    answer = total_savings_altogether
    return answer