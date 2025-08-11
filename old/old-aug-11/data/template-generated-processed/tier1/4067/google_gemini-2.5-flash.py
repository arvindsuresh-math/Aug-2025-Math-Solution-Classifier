def solve():
    """Index: 4067.
    Returns: the total amount spent by the group of children.
    """
    # L1
    children_ferris_wheel = 3 # Only 3 of them were daring enough to get on the Ferris wheel
    cost_ferris_wheel_per_child = 5 # which cost $5 per child
    cost_ferris_wheel = children_ferris_wheel * cost_ferris_wheel_per_child

    # L2
    total_children = 5 # A group of 5 children
    cost_merry_go_round_per_child = 3 # at $3 per child
    cost_merry_go_round = total_children * cost_merry_go_round_per_child

    # L3
    cones_per_child = 2 # bought 2 cones of ice cream each
    cost_cone = 8 # each cone cost $8
    cost_ice_cream = total_children * cones_per_child * cost_cone

    # L4
    total_spent = cost_ferris_wheel + cost_merry_go_round + cost_ice_cream

    # FA
    answer = total_spent
    return answer