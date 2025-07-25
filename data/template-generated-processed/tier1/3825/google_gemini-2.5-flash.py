def solve():
    """Index: 3825.
    Returns: the number of jellybeans remaining in the jar.
    """
    # L1
    initial_jellybeans = 37 # 37 jellybeans in a jar
    first_removed = 15 # Pat removed 15 of them
    after_first_removal = initial_jellybeans - first_removed

    # L2
    added_back = 5 # added 5 of the removed jellybeans back in
    after_adding_back = after_first_removal + added_back

    # L3
    second_removed = 4 # removed 4 more
    final_jellybeans = after_adding_back - second_removed

    # FA
    answer = final_jellybeans
    return answer