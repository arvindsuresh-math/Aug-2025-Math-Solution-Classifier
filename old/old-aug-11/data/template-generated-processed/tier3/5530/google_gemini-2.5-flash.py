def solve():
    """Index: 5530.
    Returns: the number of blueberry pies Simon can make.
    """
    # L1
    blueberries_from_own_bushes = 100 # 100 blueberries from his own bushes
    blueberries_from_nearby_bushes = 200 # another 200 blueberries from blueberry bushes growing nearby
    total_blueberries = blueberries_from_own_bushes + blueberries_from_nearby_bushes

    # L2
    blueberries_per_pie = 100 # each pie needs 100 blueberries
    num_pies = total_blueberries / blueberries_per_pie

    # FA
    answer = num_pies
    return answer