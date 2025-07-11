def solve():
    """Index: 2858.
    Returns: the number of people who stayed and enjoyed the birthday celebration.
    """
    # L1
    total_guests = 60 # 60 guests
    women_fraction_denominator = 2 # Half of the guests
    num_women = total_guests / women_fraction_denominator

    # L2
    num_men = 15 # 15 are men
    men_and_women = num_women + num_men

    # L3
    num_children = total_guests - men_and_women

    # L4
    men_left_denominator = 3 # 1/3 of the men
    men_who_left = num_men / men_left_denominator

    # L5
    children_who_left = 5 # 5 children left
    total_people_left = men_who_left + children_who_left

    # L6
    people_stayed = total_guests - total_people_left

    # FA
    answer = people_stayed
    return answer