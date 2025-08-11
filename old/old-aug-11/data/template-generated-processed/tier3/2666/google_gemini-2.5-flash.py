def solve():
    """Index: 2666.
    Returns: the number of times Jim's apples can fit into the average amount of apples.
    """
    # L1
    jim_apples = 20 # Jim has 20 apples
    jane_apples = 60 # Jane has 60 apples
    jerry_apples = 40 # Jerry has 40 apples
    total_apples = jim_apples + jane_apples + jerry_apples

    # L2
    number_of_people = 3 # WK
    average_apples = total_apples / number_of_people

    # L3
    times_fit = average_apples / jim_apples

    # FA
    answer = times_fit
    return answer