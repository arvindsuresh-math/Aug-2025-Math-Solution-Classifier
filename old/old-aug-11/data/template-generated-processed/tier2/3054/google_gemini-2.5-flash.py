def solve():
    """Index: 3054.
    Returns: the total number of people in John's family.
    """
    # L1
    father_side_members = 10 # 10 members of his family on his father's side
    mother_side_increase_percent = 0.3 # mother's side is 30% larger
    mother_side_increase_amount = father_side_members * mother_side_increase_percent

    # L2
    mother_side_members = father_side_members + mother_side_increase_amount

    # L3
    total_members = mother_side_members + father_side_members

    # FA
    answer = total_members
    return answer