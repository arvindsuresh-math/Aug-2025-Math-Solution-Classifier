def solve():
    """Index: 7235.
    Returns: Charlie's age when Jenny becomes twice as old as Bobby.
    """
    # L1
    jenny_older_than_charlie_years = 5 # Jenny is older than Charlie by five years
    charlie_older_than_bobby_years = 3 # Charlie is older than Bobby by three years
    jenny_older_than_bobby_years = jenny_older_than_charlie_years + charlie_older_than_bobby_years

    # L2
    twice_factor = 2 # twice as old
    # Based on J = B + jenny_older_than_bobby_years and J = twice_factor * B,
    # we deduce B = jenny_older_than_bobby_years.
    bobby_age_at_that_point = jenny_older_than_bobby_years
    jenny_age_at_that_point = bobby_age_at_that_point * twice_factor

    # L3
    charlie_age_at_that_point = jenny_age_at_that_point - jenny_older_than_charlie_years

    # FA
    answer = charlie_age_at_that_point
    return answer