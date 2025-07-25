from fractions import Fraction

def solve():
    """Index: 6566.
    Returns: the total number of chairs Thomas will order.
    """
    # L1
    initial_dozens_guests = 3 # 3 dozen guests he invites
    chairs_per_dozen = 12 # WK
    initial_guests = chairs_per_dozen * initial_dozens_guests

    # L2
    fraction_guests_bring_guest = Fraction(1, 3) # 1/3 of the guests want to bring a guest of their own
    guests_bringing_guests = fraction_guests_bring_guest * initial_guests

    # L3
    total_guests_after_additions = initial_guests + guests_bringing_guests

    # L4
    guests_cant_make_it = 5 # 5 of the guests he originally invited can't make it
    guests_after_cancellations = total_guests_after_additions - guests_cant_make_it

    # L5
    extra_chairs = 12 # 12 extra chairs
    final_chairs_needed = guests_after_cancellations + extra_chairs

    # FA
    answer = final_chairs_needed
    return answer