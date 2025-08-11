def solve():
    """Index: 1362.
    Returns: the number of gumballs each person received after sharing equally.
    """
    # L1
    joanna_initial_gumballs = 40 # 40 and 60 gumballs, respectively
    purchase_multiplier = 4 # purchased 4 times the number
    joanna_added_gumballs = joanna_initial_gumballs * purchase_multiplier

    # L2
    joanna_total_gumballs = joanna_added_gumballs + joanna_initial_gumballs

    # L3
    jacques_initial_gumballs = 60 # 40 and 60 gumballs, respectively
    jacques_added_gumballs = jacques_initial_gumballs * purchase_multiplier

    # L4
    jacques_total_gumballs = jacques_added_gumballs + jacques_initial_gumballs

    # L5
    total_gumballs_combined = jacques_total_gumballs + joanna_total_gumballs

    # L6
    number_of_people = 2 # shared them equally
    gumballs_per_person = total_gumballs_combined / number_of_people

    # FA
    answer = gumballs_per_person
    return answer