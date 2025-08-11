def solve():
    """Index: 7051.
    Returns: the number of minnows left over.
    """
    # L1
    total_people = 800 # 800 people are going to play the game
    win_percentage_num = 15 # 15% win a prize
    percent_factor = 0.01 # WK
    winning_people = total_people * win_percentage_num * percent_factor

    # L2
    minnows_per_prize = 3 # each prize is a bowl with 3 minnows
    total_minnows_needed = winning_people * minnows_per_prize

    # L3
    initial_minnows = 600 # bought 600 minnows
    minnows_left_over = initial_minnows - total_minnows_needed

    # FA
    answer = minnows_left_over
    return answer