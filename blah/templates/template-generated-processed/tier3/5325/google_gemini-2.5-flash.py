def solve():
    """Index: 5325.
    Returns: Maurice's current age.
    """
    # L1
    ron_current_age = 43 # Ron's age now is 43
    years_in_future = 5 # After five years
    ron_age_future = ron_current_age + years_in_future

    # L2
    ron_multiple = 4 # four times as old as Maurice
    maurice_age_future = ron_age_future / ron_multiple

    # L3
    maurice_current_age = maurice_age_future - years_in_future

    # FA
    answer = maurice_current_age
    return answer