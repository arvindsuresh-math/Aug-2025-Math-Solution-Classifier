def solve():
    """Index: 5209.
    Returns: the number of rubber bands Aira had.
    """
    # L1
    bands_per_person = 6 # 6 rubber bands each
    number_of_people = 3 # Samantha, Aira, and Joe
    total_bands = bands_per_person * number_of_people

    # L7
    samantha_extra_bands = 5 # Samantha had 5 more bands than Aira
    joe_extra_bands = 1 # Aira had 1 fewer band than Joe
    num_people_in_equation = 3 # WK
    
    numerator_for_x = total_bands - (samantha_extra_bands + joe_extra_bands)
    denominator_for_x = num_people_in_equation
    aira_bands = numerator_for_x / denominator_for_x

    # FA
    answer = aira_bands
    return answer