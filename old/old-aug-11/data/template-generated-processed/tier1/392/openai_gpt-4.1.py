def solve():
    """Index: 392.
    Returns: the total number of minutes it will take Naomi to wash everything.
    """
    # L1
    clothes_minutes = 30 # The clothes take 30 minutes to wash
    towels_multiplier = 2 # towels take twice as long as the clothes
    towels_minutes = clothes_minutes * towels_multiplier

    # L2
    sheets_less_than_towels = 15 # sheets take 15 minutes less time to wash than the towels
    sheets_minutes = towels_minutes - sheets_less_than_towels

    # L3
    total_minutes = clothes_minutes + towels_minutes + sheets_minutes

    # FA
    answer = total_minutes
    return answer