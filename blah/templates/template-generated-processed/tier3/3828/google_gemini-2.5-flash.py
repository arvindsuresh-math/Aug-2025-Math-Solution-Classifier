def solve():
    """Index: 3828.
    Returns: the total number of people who stayed in the movie screening.
    """
    # L1
    total_guests = 50 # a total of 50 guests
    women_fraction_denominator = 2 # half of the guests are women
    women_guests = total_guests / women_fraction_denominator

    # L2
    men_guests = 15 # 15 are men
    men_and_women_guests = women_guests + men_guests

    # L3
    children_guests = total_guests - men_and_women_guests

    # L4
    men_left_denominator = 5 # 1/5 of the men
    men_who_left = men_guests / men_left_denominator

    # L5
    children_who_left = 4 # 4 children left
    total_people_left = men_who_left + children_who_left

    # L6
    people_stayed = total_guests - total_people_left

    # FA
    answer = people_stayed
    return answer