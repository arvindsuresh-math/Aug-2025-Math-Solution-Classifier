from fractions import Fraction

def solve():
    """Index: 927.
    Returns: the total number of people at the party, including Ashley.
    """
    # L1
    invited_friends = 20 # invited 20 of her friends
    fraction_came_with_extra = Fraction(1, 2) # half the number of the invited guests
    friends_with_extra_person = fraction_came_with_extra * invited_friends

    # L2
    total_guests = invited_friends + friends_with_extra_person

    # L3
    ashley = 1 # including Ashley
    total_people_at_party = total_guests + ashley

    # FA
    answer = total_people_at_party
    return answer