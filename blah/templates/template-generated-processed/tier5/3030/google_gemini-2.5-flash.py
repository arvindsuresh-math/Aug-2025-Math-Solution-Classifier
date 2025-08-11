def solve():
    """Index: 3030.
    Returns: the number of videos Kelsey watched.
    """
    # L3
    ekon_less_than_uma = 17 # Ekon watched 17 less than Uma
    kelsey_more_than_ekon = 43 # Kelsey watched 43 more than Ekon
    kelsey_videos_simplified_constant = -ekon_less_than_uma + kelsey_more_than_ekon

    # Intermediate steps for solving U (Uma's videos)
    total_videos = 411 # Together 3 friends watched 411 short videos
    coefficient_U = 3 # From U + U + U in the combined equation
    constant_sum_in_equation = -ekon_less_than_uma + kelsey_more_than_ekon # The constant term in the combined equation (e.g., 9 in 3U + 9 = 411)
    rhs_after_subtraction = total_videos - constant_sum_in_equation # The right-hand side after moving the constant (e.g., 402 in 3U = 402)

    # L7
    uma_videos = rhs_after_subtraction / coefficient_U

    # L8
    kelsey_videos = uma_videos + kelsey_videos_simplified_constant

    # FA
    answer = kelsey_videos
    return answer