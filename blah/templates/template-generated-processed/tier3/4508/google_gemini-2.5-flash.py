def solve():
    """Index: 4508.
    Returns: the total number of dislikes the video has.
    """
    # L1
    likes = 3000 # 3000 likes
    half_divisor = 2 # half as many
    dislikes_from_half_likes = likes / half_divisor

    # L2
    initial_dislikes_offset = 100 # 100 more than half as many dislikes
    current_dislikes = dislikes_from_half_likes + initial_dislikes_offset

    # L3
    additional_dislikes = 1000 # 1000 more dislikes
    final_dislikes = current_dislikes + additional_dislikes

    # FA
    answer = final_dislikes
    return answer