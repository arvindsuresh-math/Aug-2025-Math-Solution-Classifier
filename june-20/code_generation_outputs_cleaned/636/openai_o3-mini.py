def solve(
    assignment_time: int = 10,  # "assignment will only take 10 minutes to complete"
    dinner_time: str = "5:30",  # "Dinner will be ready at 5:30 p.m."
    sticky_keys: int = 15,  # "she counts 15 keys that are sticky"
    cleaning_time_per_key: int = 3,  # "times it to take 3 minutes to clean one"
    keys_cleaned: int = 1,  # "After Tina has cleaned one key"
    keys_remaining: int = 14  # "there are 14 left to clean"
):
    """Index: 636.
    Returns: the total number of minutes required to clean the remaining keys and complete the assignment.
    """
    #: L1
    total_cleaning_time = keys_remaining * cleaning_time_per_key  # 14 keys * 3 minutes/key = 42 minutes
    #: L2
    total_time = total_cleaning_time + assignment_time  # 42 minutes + 10 minutes = 52 minutes
    answer = total_time  # FINAL ANSWER
    return answer