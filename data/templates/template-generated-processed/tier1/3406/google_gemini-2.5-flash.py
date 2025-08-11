def solve():
    """Index: 3406.
    Returns: the total amount of bubble bath needed in millilitres.
    """
    # L1
    num_couple_rooms = 13 # 13 rooms for couples
    people_per_couple_room = 2 # couples implies 2 people per room
    people_in_couple_rooms = num_couple_rooms * people_per_couple_room

    # L2
    num_single_rooms = 14 # 14 single rooms
    total_people = people_in_couple_rooms + num_single_rooms

    # L3
    ml_per_bath = 10 # 10ml of bubble bath
    total_bubble_bath_needed = total_people * ml_per_bath

    # FA
    answer = total_bubble_bath_needed
    return answer