def solve():
    """Index: 767.
    Returns: the number of kids who went rafting and tubing.
    """
    # L1
    total_kids = 40 # 40 kids on Lake Pleasant
    tubing_fraction_denominator = 4 # A fourth of the kids
    kids_tubing = total_kids / tubing_fraction_denominator

    # L2
    rafting_tubing_denominator = 2 # only half of the tubers
    kids_rafting_and_tubing = kids_tubing / rafting_tubing_denominator

    # FA
    answer = kids_rafting_and_tubing
    return answer