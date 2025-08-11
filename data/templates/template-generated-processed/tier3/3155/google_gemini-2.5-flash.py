from fractions import Fraction

def solve():
    """Index: 3155.
    Returns: the total number of bars left in the box.
    """
    # L1
    initial_total_bars = 200 # A chocolate box contains 200 bars
    fraction_taken_by_group = Fraction(1, 4) # take 1/4 of the bars
    bars_taken_by_group = fraction_taken_by_group * initial_total_bars

    # L2
    bars_left_after_group_takes = initial_total_bars - bars_taken_by_group

    # L3
    num_people_sharing = 5 # Thomas and his 4 friends
    bars_per_person = bars_taken_by_group / num_people_sharing

    # L4
    bars_returned_by_friend = 5 # returns 5 of his bars
    bars_after_return = bars_left_after_group_takes + bars_returned_by_friend

    # L5
    fewer_bars_piper_took = 5 # takes 5 fewer bars
    bars_taken_by_piper = bars_taken_by_group - fewer_bars_piper_took

    # L6
    total_remaining_bars = bars_after_return - bars_taken_by_piper

    # FA
    answer = total_remaining_bars
    return answer