from fractions import Fraction

def solve():
    """Index: 2478.
    Returns: the total points Samanta, Mark, and Eric have.
    """
    # L1
    mark_percentage_more = Fraction(50, 100) # 50% more points
    eric_points = 6 # Eric has 6 points
    mark_additional_points = mark_percentage_more * eric_points

    # L2
    mark_total_points = eric_points + mark_additional_points

    # L3
    samanta_more_than_mark = 8 # Samanta has 8 more points than Mark
    samanta_points = mark_total_points + samanta_more_than_mark

    # L4
    total_points = eric_points + mark_total_points + samanta_points

    # FA
    answer = total_points
    return answer