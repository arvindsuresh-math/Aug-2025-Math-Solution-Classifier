def solve():
    """Index: 2533.
    Returns: the number of tents needed.
    """
    # L1
    matt = 1 # Matt's family included his mom, dad, his older brother and his wife and their 4 kids. His Uncle Joe and his wife were also coming and would bring their 3 kids.
    mom_dad = 2 # Matt's family included his mom, dad
    brother_wife = 2 # his older brother and his wife
    brothers_kids = 4 # their 4 kids
    uncle_joe_wife = 2 # His Uncle Joe and his wife
    uncle_joes_kids = 3 # their 3 kids
    total_family_members = matt + mom_dad + brother_wife + brothers_kids + uncle_joe_wife + uncle_joes_kids

    # L2
    house_capacity = 4 # The house only sleeps 4 people
    people_needing_tents = total_family_members - house_capacity

    # L3
    tent_capacity = 2 # Everyone else would sleep 2 to a tent outside
    tents_needed = people_needing_tents / tent_capacity

    # FA
    answer = tents_needed
    return answer