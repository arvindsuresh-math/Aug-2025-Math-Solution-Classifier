from fractions import Fraction

def solve():
    """Index: 122.
    Returns: the number of board members who attended the meeting.
    """
    # L1
    num_chairs = 40 # 40 chairs
    capacity_per_chair = 2 # capacity of 2 people each
    total_capacity = num_chairs * capacity_per_chair

    # L2
    unoccupied_fraction = Fraction(2, 5) # 2/5 of the chairs were not occupied
    people_missed_meeting = unoccupied_fraction * total_capacity

    # L3
    attended_members = total_capacity - people_missed_meeting

    # FA
    answer = attended_members
    return answer