def solve():
    """Index: 2773.
    Returns: James's age after 5 years.
    """
    # L1
    justin_current_age = 26 # Justin is 26 years old
    jessica_age_at_justin_birth = 6 # Jessica was 6 years old
    jessica_current_age = justin_current_age + jessica_age_at_justin_birth

    # L2
    james_age_difference_from_jessica = 7 # James is their elder brother and is 7 years older than Jessica
    james_current_age = jessica_current_age + james_age_difference_from_jessica

    # L3
    years_in_future = 5 # after 5 years
    james_age_in_future = james_current_age + years_in_future

    # FA
    answer = james_age_in_future
    return answer