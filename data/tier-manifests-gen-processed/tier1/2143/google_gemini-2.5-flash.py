def solve():
    """Index: 2143.
    Returns: the length, in feet, the fourth competitor jumped.
    """
    # L1
    first_competitor_jump = 22 # The first competitor jumped a distance of 22 feet.
    second_competitor_farther = 1 # The second competitor jumped one foot farther than the first competitor.
    second_competitor_jump = first_competitor_jump + second_competitor_farther

    # L2
    # Note: The question states "The third competitor jumped two feet shorter than the third competitor." 
    # The solution interprets this as "shorter than the second competitor", which is formalized below.
    third_competitor_shorter = 2 # two feet shorter than the third competitor (interpreted as second competitor)
    third_competitor_jump = second_competitor_jump - third_competitor_shorter

    # L3
    fourth_competitor_further = 3 # 3 feet further than the third competitor
    fourth_competitor_jump = third_competitor_jump + fourth_competitor_further

    # FA
    answer = fourth_competitor_jump
    return answer