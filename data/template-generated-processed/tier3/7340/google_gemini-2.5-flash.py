def solve():
    """Index: 7340.
    Returns: the number of children Yasmin has.
    """
    # L2
    john_multiplier = 2 # John has twice the number of children that her sister has
    john_children_factor = john_multiplier

    # L4
    combined_yasmin_john_factor = john_children_factor + 1

    # L5
    gabriel_grandkids = 6 # Gabriel has six grandkids
    yasmin_children = gabriel_grandkids / combined_yasmin_john_factor

    # FA
    answer = yasmin_children
    return answer