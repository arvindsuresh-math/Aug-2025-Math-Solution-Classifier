def solve():
    """Index: 6401.
    Returns: the total number of fish Leo and Agrey caught together.
    """
    # L1
    leo_caught = 40 # Leo caught 40 fish
    agrey_more_than_leo = 20 # Agrey caught 20 more fish than Leo
    agrey_caught = leo_caught + agrey_more_than_leo

    # L2
    total_fish = agrey_caught + leo_caught

    # FA
    answer = total_fish
    return answer