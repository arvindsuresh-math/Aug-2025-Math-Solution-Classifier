def solve():
    """Index: 3787.
    Returns: Jason's age when he retired from the military.
    """
    # L1
    years_to_chief = 8 # 8 years to raise to the rank of chief
    longer_percent = 0.25 # 25% longer
    years_longer_to_master_chief = years_to_chief * longer_percent

    # L2
    total_years_to_master_chief_from_chief = years_to_chief + years_longer_to_master_chief

    # L3
    total_years_to_master_chief_from_enlisting = total_years_to_master_chief_from_chief + years_to_chief

    # L4
    additional_years_before_retiring = 10 # spent 10 years more in the military before retiring
    total_years_in_military = total_years_to_master_chief_from_enlisting + additional_years_before_retiring

    # L5
    joining_age = 18 # joined the military when he turned 18
    retirement_age = total_years_in_military + joining_age

    # FA
    answer = retirement_age
    return answer