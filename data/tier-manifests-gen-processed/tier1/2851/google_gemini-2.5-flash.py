def solve():
    """Index: 2851.
    Returns: the combined age of the siblings.
    """
    # L1
    aaron_age = 15 # Aaron, Henry's brother, is 15 years old
    sister_age_multiplier = 3 # three times as old as Aaron
    sister_age = sister_age_multiplier * aaron_age

    # L2
    aaron_sister_combined_age = sister_age + aaron_age

    # L3
    henry_age_multiplier = 4 # Henry is four times as old as his sister
    henry_age = sister_age * henry_age_multiplier

    # L4
    total_siblings_age = aaron_sister_combined_age + henry_age

    # FA
    answer = total_siblings_age
    return answer