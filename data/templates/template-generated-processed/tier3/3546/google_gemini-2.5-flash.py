def solve():
    """Index: 3546.
    Returns: the number of Burmese pythons needed.
    """
    # L1
    total_alligators = 15 # fifteen 50-centimeter alligators
    total_weeks = 3 # three weeks
    alligators_per_week_needed = total_alligators / total_weeks

    # L2
    alligators_per_week_per_python = 1 # one Burmese python can eat one 50-cm alligator per week
    num_pythons = alligators_per_week_needed / alligators_per_week_per_python

    # FA
    answer = num_pythons
    return answer