def solve():
    """Index: 5291.
    Returns: the number of people in the interview room.
    """
    # L1
    initial_waiting_room_people = 22 # twenty-two people in a waiting room
    people_arriving = 3 # three more people arrive
    new_waiting_room_people = initial_waiting_room_people + people_arriving

    # L2
    times_factor = 5 # five times the number of people
    interview_room_people = new_waiting_room_people / times_factor

    # FA
    answer = interview_room_people
    return answer