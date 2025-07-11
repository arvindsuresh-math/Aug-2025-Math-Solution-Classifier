def solve():
    """Index: 2952.
    Returns: the total number of lollipops given away.
    """
    # L1
    initial_attendees = 45 # 45 people show up for class
    later_attendees = 15 # another 15 come in a while later
    total_attendees = initial_attendees + later_attendees

    # L2
    people_per_lollipop = 5 # For every 5 people that attend a poetry class, the teacher gives one of the students a lollipop
    total_lollipops = total_attendees / people_per_lollipop

    # FA
    answer = total_lollipops
    return answer