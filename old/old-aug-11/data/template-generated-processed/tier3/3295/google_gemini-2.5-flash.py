def solve():
    """Index: 3295.
    Returns: the number of people not in the pool.
    """
    # L1
    karen_count = 1 # Karen
    donald_count = 1 # Donald
    karen_donald_children = 6 # their 6 children
    karen_donald_party_size = karen_count + donald_count + karen_donald_children

    # L2
    tom_count = 1 # Tom
    eva_count = 1 # Eva
    tom_eva_children = 4 # their 4 children
    tom_eva_party_size = tom_count + eva_count + tom_eva_children

    # L3
    total_people_at_house = karen_donald_party_size + tom_eva_party_size

    # L4
    legs_in_pool = 16 # 16 legs in the pool
    legs_per_person = 2 # everyone has 2 legs
    people_in_pool = legs_in_pool / legs_per_person

    # L5
    people_not_in_pool = total_people_at_house - people_in_pool

    # FA
    answer = people_not_in_pool
    return answer