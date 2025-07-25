def solve():
    """Index: 2851.
    Returns: the combined age of the siblings.
    """
    # L1
    aaron_age = 15 # Aaron is 15 years old
    sister_multiplier = 3 # sister is three times as old as Aaron
    sister_age = sister_multiplier * aaron_age

    # L2
    aaron_and_sister_total = sister_age + aaron_age

    # L3
    henry_multiplier = 4 # Henry is four times as old as his sister
    henry_age = sister_age * henry_multiplier

    # L4
    total_age = aaron_and_sister_total + henry_age

    # FA
    answer = total_age
    return answer