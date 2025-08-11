def solve():
    """Index: 2215.
    Returns: the number of men who finished the race.
    """
    # L1
    total_men_race = 80 # 80 men in a race
    tripped_fraction_denominator = 4 # 1/4 of the men tripped
    men_tripped = total_men_race / tripped_fraction_denominator

    # L2
    men_remaining_after_trip = total_men_race - men_tripped

    # L3
    dehydrated_numerator = 2 # 2/3 of the remaining men were dehydrated
    dehydrated_denominator = 3 # 2/3 of the remaining men were dehydrated
    men_dehydrated = men_remaining_after_trip * dehydrated_numerator / dehydrated_denominator

    # L4
    dehydrated_not_finish_numerator = 1 # 1/5 of those dehydrated men couldn't finish
    dehydrated_not_finish_denominator = 5 # 1/5 of those dehydrated men couldn't finish
    dehydrated_men_not_finish = men_dehydrated * dehydrated_not_finish_numerator / dehydrated_not_finish_denominator

    # L5
    men_finished_race = men_remaining_after_trip - dehydrated_men_not_finish

    # FA
    answer = men_finished_race
    return answer