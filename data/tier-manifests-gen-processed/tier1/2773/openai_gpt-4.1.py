def solve():
    """Index: 2773.
    Returns: James's age after 5 years.
    """
    # L1
    justin_age = 26 # Justin is 26 years old
    jessica_older_by = 6 # Jessica was 6 years old when Justin was born
    jessica_age = justin_age + jessica_older_by

    # L2
    james_older_by = 7 # James is 7 years older than Jessica
    james_age = jessica_age + james_older_by

    # L3
    years_in_future = 5 # after 5 years
    james_future_age = james_age + years_in_future

    # FA
    answer = james_future_age
    return answer