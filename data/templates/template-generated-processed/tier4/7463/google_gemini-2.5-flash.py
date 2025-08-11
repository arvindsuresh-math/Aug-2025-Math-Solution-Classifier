from fractions import Fraction

def solve():
    """Index: 7463.
    Returns: the total percentage of women in the company now.
    """
    # L1
    total_fraction_whole = 1 # WK
    men_fraction = Fraction(2, 3) # 2/3rds of them are men
    initial_women_fraction = total_fraction_whole - men_fraction

    # L2
    total_initial_workers = 90 # 90 workers
    initial_women_count = initial_women_fraction * total_initial_workers

    # L3
    new_women_hires = 10 # 10 new employees and 100% of them are women
    current_women_count = initial_women_count + new_women_hires

    # L4
    total_new_employees = 10 # 10 new employees
    total_current_workers = total_initial_workers + total_new_employees

    # L5
    women_proportion = current_women_count / total_current_workers

    # L6
    percent_multiplier = 100 # WK
    women_percentage = women_proportion * percent_multiplier

    # FA
    answer = women_percentage
    return answer