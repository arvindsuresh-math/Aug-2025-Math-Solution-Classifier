def solve():
    """Index: 5567.
    Returns: the number of jelly beans remaining in the container.
    """
    # L1
    num_last_people = 4 # last four people
    jelly_beans_per_last_person = 400 # each took 400 jelly beans
    total_last_people_took = num_last_people * jelly_beans_per_last_person

    # L2
    multiplier_first_people = 2 # twice as many jelly beans
    jelly_beans_per_first_person = multiplier_first_people * jelly_beans_per_last_person

    # L3
    num_first_people = 6 # first six people
    total_first_people_took = jelly_beans_per_first_person * num_first_people

    # L4
    total_all_people_took = total_first_people_took + total_last_people_took

    # L5
    initial_jelly_beans = 8000 # 8000 jelly beans in a certain barrel
    remaining_jelly_beans = initial_jelly_beans - total_all_people_took

    # FA
    answer = remaining_jelly_beans
    return answer