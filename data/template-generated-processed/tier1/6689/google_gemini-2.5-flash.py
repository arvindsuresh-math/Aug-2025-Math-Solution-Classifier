def solve():
    """Index: 6689.
    Returns: the total number of cans of soup Mark donates.
    """
    # L1
    num_shelters = 6 # 6 homeless shelters
    people_per_shelter = 30 # services 30 people
    total_people = num_shelters * people_per_shelter

    # L2
    cans_per_person = 10 # 10 cans of soup per person
    total_cans_donated = total_people * cans_per_person

    # FA
    answer = total_cans_donated
    return answer