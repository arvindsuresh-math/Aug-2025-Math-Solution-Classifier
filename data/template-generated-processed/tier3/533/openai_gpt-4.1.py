from fractions import Fraction

def solve():
    """Index: 533.
    Returns: the number of jelly beans remaining in the bag after the children took their share.
    """
    # L1
    total_children = 40 # 40 children taking part in the Halloween celebration
    allowed_percentage = Fraction(80, 100) # 80% were allowed to draw
    allowed_children = allowed_percentage * total_children

    # L2
    jelly_beans_per_child = 2 # Each child drew two jelly beans
    total_drawn = allowed_children * jelly_beans_per_child

    # L3
    initial_jelly_beans = 100 # 100 jelly beans in a bag
    remaining_jelly_beans = initial_jelly_beans - total_drawn

    # FA
    answer = remaining_jelly_beans
    return answer