def solve():
    """Index: 2573.
    Returns: the number of problems of each type Frank composes.
    """
    # L1
    bill_problems = 20 # Bill composes 20 total math questions
    ryan_multiplier = 2 # twice as many problems as Bill
    ryan_problems = bill_problems * ryan_multiplier

    # L2
    frank_multiplier = 3 # Frank composes 3 times as many as Ryan
    frank_problems = ryan_problems * frank_multiplier

    # L3
    num_types = 4 # 4 different types of math problems
    problems_per_type = frank_problems / num_types

    # FA
    answer = problems_per_type
    return answer