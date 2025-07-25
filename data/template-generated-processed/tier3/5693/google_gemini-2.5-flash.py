from fractions import Fraction

def solve():
    """Index: 5693.
    Returns: the total number of sweaters Kim knit that week.
    """
    # L1
    sweaters_monday = 8 # 8 sweaters on Monday
    more_on_tuesday = 2 # 2 more sweaters on Tuesday than on Monday
    sweaters_tuesday = sweaters_monday + more_on_tuesday

    # L2
    total_monday_tuesday = sweaters_tuesday + sweaters_monday

    # L3
    fewer_on_wednesday = 4 # 4 fewer sweaters on both Wednesday and Thursday than on Tuesday
    sweaters_wednesday = sweaters_tuesday - fewer_on_wednesday

    # L4
    total_by_wednesday = total_monday_tuesday + sweaters_wednesday

    # L5
    sweaters_thursday = sweaters_wednesday # 4 fewer sweaters on both Wednesday and Thursday than on Tuesday
    total_by_thursday = total_by_wednesday + sweaters_thursday

    # L6
    fraction_friday = Fraction(1, 2) # half the number of sweaters
    sweaters_friday = fraction_friday * sweaters_monday

    # L7
    total_sweaters_week = total_by_thursday + sweaters_friday

    # FA
    answer = total_sweaters_week
    return answer