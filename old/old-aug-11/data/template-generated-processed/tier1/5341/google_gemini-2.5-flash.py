def solve():
    """Index: 5341.
    Returns: how much taller Mike is than Mark in inches.
    """
    # L1
    mark_feet = 5 # 5 feet
    mark_inches_extra = 3 # 3 inches tall
    inches_per_foot = 12 # 1 foot is equal to 12 inches
    mark_total_inches = (mark_feet * inches_per_foot) + mark_inches_extra

    # L2
    mike_feet = 6 # 6 feet
    mike_inches_extra = 1 # 1 inch tall
    mike_total_inches = (mike_feet * inches_per_foot) + mike_inches_extra

    # L3
    difference_in_height = mike_total_inches - mark_total_inches

    # FA
    answer = difference_in_height
    return answer