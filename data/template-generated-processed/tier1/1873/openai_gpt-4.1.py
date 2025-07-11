def solve():
    """Index: 1873.
    Returns: Sophia's age three years from now.
    """
    # L1
    jeremy_age = 40 # Jeremy's age is 40
    years_in_future = 3 # in three years
    jeremy_future_age = jeremy_age + years_in_future

    # L2
    sebastian_older = 4 # Sebastian is 4 years older than Jeremy
    sebastian_age = jeremy_age + sebastian_older

    # L3
    sebastian_future_age = sebastian_age + years_in_future

    # L4
    total_jeremy_sebastian_future = sebastian_future_age + jeremy_future_age

    # L5
    total_future_sum = 150 # sum of the ages of Jeremy, Sebastian and Sophia in three years is 150
    sophia_future_age = total_future_sum - total_jeremy_sebastian_future

    # FA
    answer = sophia_future_age
    return answer