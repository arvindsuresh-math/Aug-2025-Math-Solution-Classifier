def solve():
    """Index: 4191.
    Returns: the combined experience of James, John, and Mike.
    """
    # L1
    james_current_experience = 20 # James has 20 years of experience
    years_ago = 8 # 8 years ago
    james_experience_8_years_ago = james_current_experience - years_ago

    # L2
    john_experience_multiplier = 2 # twice as much experience as James
    john_experience_8_years_ago = james_experience_8_years_ago * john_experience_multiplier

    # L3
    john_current_experience = john_experience_8_years_ago + years_ago

    # L4
    john_experience_when_mike_started = 16 # John had 16 years of experience
    mike_current_experience = john_current_experience - john_experience_when_mike_started

    # L5
    combined_experience = james_current_experience + john_current_experience + mike_current_experience

    # FA
    answer = combined_experience
    return answer