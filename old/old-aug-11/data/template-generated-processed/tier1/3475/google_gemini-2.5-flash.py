def solve():
    """Index: 3475.
    Returns: the total number of nail polishes Karen and Heidi have together.
    """
    # L1
    kim_nail_polishes = 12 # Kim has 12 nail polishes
    heidi_more_than_kim = 5 # Heidi has 5 more nail polishes than Kim
    heidi_nail_polishes = kim_nail_polishes + heidi_more_than_kim

    # L2
    karen_fewer_than_kim = 4 # Karen has 4 fewer nail polishes than Kim
    karen_nail_polishes = kim_nail_polishes - karen_fewer_than_kim

    # L3
    total_karen_heidi = heidi_nail_polishes + karen_nail_polishes

    # FA
    answer = total_karen_heidi
    return answer