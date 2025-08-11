def solve():
    """Index: 4539.
    Returns: the total number of beds in the hotel.
    """
    # L1
    total_rooms = 13 # 13 hotel rooms
    rooms_with_two_beds = 8 # Eight of the rooms have two beds
    rooms_with_three_beds = total_rooms - rooms_with_two_beds

    # L2
    beds_per_three_bed_room = 3 # the rest have three beds
    total_beds_three_bed_rooms = rooms_with_three_beds * beds_per_three_bed_room

    # L3
    beds_per_two_bed_room = 2 # two beds in them
    total_beds_two_bed_rooms = rooms_with_two_beds * beds_per_two_bed_room

    # L4
    total_beds = total_beds_three_bed_rooms + total_beds_two_bed_rooms

    # FA
    answer = total_beds
    return answer