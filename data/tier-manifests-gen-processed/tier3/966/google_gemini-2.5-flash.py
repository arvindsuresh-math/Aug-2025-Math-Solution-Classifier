def solve():
    """Index: 966.
    Returns: the number of people at Ryan's party.
    """
    # L5
    total_combined_people = 240 # If both parties combined had 240 people
    combined_ratio_factor = 5 # 4n+n = 240, which translates to 5n=240
    taylors_party_people = total_combined_people / combined_ratio_factor

    # L7
    ryan_multiplier = 4 # Ryan's party was 4 times as huge as Taylor's birthday party
    ryans_party_people = taylors_party_people * ryan_multiplier

    # FA
    answer = ryans_party_people
    return answer