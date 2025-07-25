def solve():
    """Index: 4355.
    Returns: how many more people attended the games than expected.
    """
    # L1
    people_saturday = 80 # 80 people at a football game on Saturday
    fewer_monday = 20 # 20 fewer people were at the football game
    people_monday = people_saturday - fewer_monday

    # L2
    more_wednesday = 50 # 50 more people were at the game than on Monday
    people_wednesday = people_monday + more_wednesday

    # L3
    people_friday = people_saturday + people_monday

    # L4
    total_attended = people_saturday + people_monday + people_wednesday + people_friday

    # L5
    expected_audience = 350 # expected total audience at the football game for a week is 350
    more_than_expected = total_attended - expected_audience

    # FA
    answer = more_than_expected
    return answer