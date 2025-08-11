def solve():
    """Index: 816.
    Returns: the total number of plates Matt needs to buy for a week.
    """
    # L2
    days_just_matt_and_son = 3 # Three days a week it is only him and his son eating
    plates_per_person_normal = 1 # they use 1 plate each
    num_people_normal = 2 # 1+1=2 people eating (Matt and his son)
    plates_used_normal_days = days_just_matt_and_son * num_people_normal * plates_per_person_normal

    # L3
    days_in_week = 7 # WK
    days_with_parents = days_in_week - days_just_matt_and_son

    # L4
    num_people_with_parents = num_people_normal + 2 # 2+2=4 people eating (Matt, son, parents)

    # L5
    plates_per_person_special = 2 # everyone uses 2 plates that day
    plates_used_special_day = num_people_with_parents * plates_per_person_special

    # L6
    plates_used_special_days = plates_used_special_day * days_with_parents

    # L7
    total_plates = plates_used_special_days + plates_used_normal_days

    # FA
    answer = total_plates
    return answer