def solve():
    """Index: 4168.
    Returns: the average weight of the three people.
    """
    # L1
    rachel_weight = 75 # Rachel weighs 75 pounds
    less_than_jimmy = 6 # 6 pounds less than Jimmy
    jimmy_weight = rachel_weight + less_than_jimmy

    # L2
    more_than_adam = 15 # 15 pounds more than Adam
    adam_weight = rachel_weight - more_than_adam

    # L3
    total_weight = rachel_weight + jimmy_weight + adam_weight

    # L4
    number_of_people = 3 # three people
    average_weight = total_weight / number_of_people

    # FA
    answer = average_weight
    return answer