def solve():
    """Index: 5154.
    Returns: James's age when Thomas reaches his current age.
    """
    # L1
    thomas_age = 6 # Thomas is 6 years old
    shay_older_than_thomas = 13 # Shay is 13 years older than him
    shay_age = thomas_age + shay_older_than_thomas

    # L2
    shay_younger_than_james = 5 # 5 years younger than their older brother, James
    james_age = shay_age + shay_younger_than_james

    # L3
    years_passed = james_age - thomas_age

    # L4
    james_future_age = james_age + years_passed

    # FA
    answer = james_future_age
    return answer