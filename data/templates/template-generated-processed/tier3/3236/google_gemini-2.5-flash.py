def solve():
    """Index: 3236.
    Returns: the number of roses each person will get.
    """
    # L1
    initial_roses = 40 # Ricky has 40 roses
    stolen_roses = 4 # steals 4 roses
    remaining_roses = initial_roses - stolen_roses

    # L2
    num_people = 9 # to 9 different people
    roses_per_person = remaining_roses / num_people

    # FA
    answer = roses_per_person
    return answer