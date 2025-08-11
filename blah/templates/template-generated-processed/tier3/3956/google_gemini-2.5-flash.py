def solve():
    """Index: 3956.
    Returns: the amount each family member will pay.
    """
    # L1
    dozens_of_people = 5 # Five dozens of people
    items_per_dozen = 12 # WK
    total_people = dozens_of_people * items_per_dozen

    # L2
    cans_per_person = 2 # each person can consume 2 cans of soda
    total_cans_needed = total_people * cans_per_person

    # L3
    cans_per_box = 10 # Each box of soda contains 10 cans
    boxes_needed = total_cans_needed / cans_per_box

    # L4
    cost_per_box = 2 # costs $2 per box
    total_cost = cost_per_box * boxes_needed

    # L5
    family_members = 6 # you are six in the family
    cost_per_family_member = total_cost / family_members

    # FA
    answer = cost_per_family_member
    return answer