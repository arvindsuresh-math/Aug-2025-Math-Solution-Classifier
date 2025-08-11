def solve():
    """Index: 1742.
    Returns: the average number of calls Jean answers per day.
    """
    # L1
    calls_monday = 35 # answered 35 phone calls on Monday
    calls_tuesday = 46 # answered 46
    calls_wednesday = 27 # took 27 calls on Wednesday
    calls_thursday = 61 # answered 61 calls
    calls_friday = 31 # finished off answering 31 calls on Friday
    total_calls = calls_monday + calls_tuesday + calls_wednesday + calls_thursday + calls_friday

    # L2
    number_of_days = 5 # over 5 days
    average_calls_per_day = total_calls / number_of_days

    # FA
    answer = average_calls_per_day
    return answer