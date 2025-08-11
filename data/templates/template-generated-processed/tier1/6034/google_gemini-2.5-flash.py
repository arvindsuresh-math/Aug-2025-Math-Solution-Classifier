def solve():
    """Index: 6034.
    Returns: the total number of fish caught by Brendan and his dad.
    """
    # L1
    brendan_morning_fish = 8 # caught 8 fish in the morning
    brendan_afternoon_fish = 5 # caught 5 more in the afternoon
    brendan_total_caught = brendan_morning_fish + brendan_afternoon_fish

    # L2
    brendan_threw_back = 3 # threw 3 back that were too small
    brendan_fish_kept = brendan_total_caught - brendan_threw_back

    # L3
    dad_caught_fish = 13 # Brendan’s dad caught 13 fish
    total_fish_caught = brendan_fish_kept + dad_caught_fish

    # FA
    answer = total_fish_caught
    return answer