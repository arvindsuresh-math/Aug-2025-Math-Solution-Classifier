def solve():
    """Index: 608.
    Returns: Jung's age in years.
    """
    # L1
    zhang_multiplier = 2 # Zhang is twice as old as Li
    li_age = 12 # Li is 12 years old
    zhang_age = zhang_multiplier * li_age

    # L2
    jung_older_by = 2 # Jung is 2 years older than Zhang
    jung_age = jung_older_by + zhang_age

    # FA
    answer = jung_age
    return answer