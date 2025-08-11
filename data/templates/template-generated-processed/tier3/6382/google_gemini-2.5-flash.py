def solve():
    """Index: 6382.
    Returns: the number of additional bottles of water the camp organizer needs to buy.
    """
    # L1
    first_group_children = 14 # The first group has 14 children
    second_group_children = 16 # the second group has 16 children
    third_group_children = 12 # the third group has 12 children
    first_three_groups_children = first_group_children + second_group_children + third_group_children

    # L2
    fourth_group_divisor = 2 # half of the number of the first three groups combined
    fourth_group_children = first_three_groups_children / fourth_group_divisor

    # L3
    total_children = first_three_groups_children + fourth_group_children

    # L4
    bottles_per_child_per_day = 3 # each child consumes 3 bottles a day
    daily_consumption = bottles_per_child_per_day * total_children

    # L5
    camp_duration_days = 3 # for a 3-day camp
    total_bottles_needed = daily_consumption * camp_duration_days

    # L6
    cases_purchased = 13 # purchased 13 cases
    bottles_per_case = 24 # A case of water contains 24 bottles
    bottles_purchased = cases_purchased * bottles_per_case

    # L7
    bottles_still_needed = total_bottles_needed - bottles_purchased

    # FA
    answer = bottles_still_needed
    return answer