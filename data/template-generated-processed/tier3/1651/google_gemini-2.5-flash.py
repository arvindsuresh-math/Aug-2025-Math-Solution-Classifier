def solve():
    """Index: 1651.
    Returns: the internal volume of the box in cubic feet.
    """
    # L1
    sides_per_dimension = 2 # WK
    wall_thickness = 1 # The walls are 1 inch thick
    thickness_reduction_per_dimension = sides_per_dimension * wall_thickness

    # L2
    longer_side_outer_inches = 26 # 26 inches by 26 inches
    longer_side_internal_inches = longer_side_outer_inches - thickness_reduction_per_dimension

    # L3
    inches_per_foot = 12 # WK
    longer_side_internal_feet = longer_side_internal_inches / inches_per_foot

    # L4
    smaller_side_outer_inches = 14 # by 14 inches
    smaller_side_internal_inches = smaller_side_outer_inches - thickness_reduction_per_dimension

    # L5
    smaller_side_internal_feet = smaller_side_internal_inches / inches_per_foot

    # L6
    internal_volume_cubic_feet = longer_side_internal_feet * longer_side_internal_feet * smaller_side_internal_feet

    # FA
    answer = internal_volume_cubic_feet
    return answer