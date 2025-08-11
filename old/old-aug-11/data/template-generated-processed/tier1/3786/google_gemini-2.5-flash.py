def solve():
    """Index: 3786.
    Returns: how much longer Patricia has to grow her hair.
    """
    # L1
    donation_length = 23 # donate 23 inches
    desired_length_after_donation = 12 # 12 inches long after the donation
    total_length_needed = donation_length + desired_length_after_donation

    # L2
    current_length = 14 # Her hair is 14 inches long
    length_to_grow = total_length_needed - current_length

    # FA
    answer = length_to_grow
    return answer