def solve():
    """Index: 1693.
    Returns: the average age of the three people.
    """
    # L1
    devin_age = 12 # If Devin is 12 years old
    eden_multiplier = 2 # twice as old as Devin
    eden_age = eden_multiplier * devin_age

    # L2
    mom_multiplier = 2 # twice as old as Eden
    mom_age = eden_age * mom_multiplier

    # L3
    total_age = mom_age + eden_age + devin_age

    # L4
    number_of_people = 3 # average age of the three
    average_age = total_age / number_of_people

    # FA
    answer = average_age
    return answer