def solve():
    """Index: 4027.
    Returns: the number of boxes of Graham crackers left over.
    """
    # L1
    total_graham_crackers = 14 # bought 14 boxes of Graham crackers
    graham_crackers_per_cheesecake = 2 # needs 2 boxes of Graham crackers
    cheesecakes_from_graham_crackers = total_graham_crackers / graham_crackers_per_cheesecake

    # L2
    total_oreos = 15 # 15 packets of Oreos
    oreos_per_cheesecake = 3 # needs 3 packets of Oreos
    cheesecakes_from_oreos = total_oreos / oreos_per_cheesecake

    # L3
    max_cheesecakes = min(cheesecakes_from_graham_crackers, cheesecakes_from_oreos)

    # L4
    graham_crackers_used = graham_crackers_per_cheesecake * max_cheesecakes

    # L5
    graham_crackers_left_over = total_graham_crackers - graham_crackers_used

    # FA
    answer = graham_crackers_left_over
    return answer