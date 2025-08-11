def solve():
    """Index: 1672.
    Returns: Ophelia's current age.
    """
    # L1
    years_in_future = 2 # In two years
    lennon_current_age = 8 # Lennon is currently eight years old
    lennon_future_age = years_in_future + lennon_current_age

    # L2
    ophelia_multiplier = 4 # four times as old as Lennon
    ophelia_future_age = ophelia_multiplier * lennon_future_age

    # L3
    ophelia_current_age = ophelia_future_age - years_in_future

    # FA
    answer = ophelia_current_age
    return answer