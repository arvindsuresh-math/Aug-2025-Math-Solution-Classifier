def solve():
    """Index: 6530.
    Returns: the number of pictures Charles drew when he came back from work.
    """
    # L1
    today_drew = 6 # Today Charles drew 6 pictures
    yesterday_before_work = 6 # Yesterday he drew 6 pictures before going to work
    total_drawn_before_return = today_drew + yesterday_before_work

    # L2
    total_papers_bought = 20 # Charles bought 20 papers to draw
    papers_remaining_before_return_drawings = total_papers_bought - total_drawn_before_return

    # L3
    final_papers_left = 2 # he has 2 papers left
    pictures_drawn_after_work = papers_remaining_before_return_drawings - final_papers_left

    # FA
    answer = pictures_drawn_after_work
    return answer