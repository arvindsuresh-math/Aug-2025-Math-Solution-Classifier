from fractions import Fraction

def solve():
    """Index: 533.
    Returns: the number of jelly beans remaining in the bag.
    """
    # L1
    total_children = 40 # 40 children taking part
    allowed_percentage = Fraction(80, 100) # 80% were allowed to draw
    children_allowed_to_draw = allowed_percentage * total_children

    # L2
    jelly_beans_per_child = 2 # Each child drew two jelly beans
    total_jelly_beans_drawn = children_allowed_to_draw * jelly_beans_per_child

    # L3
    initial_jelly_beans = 100 # 100 jelly beans in a bag
    remaining_jelly_beans = initial_jelly_beans - total_jelly_beans_drawn

    # FA
    answer = remaining_jelly_beans
    return answer