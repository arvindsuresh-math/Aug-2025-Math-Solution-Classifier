def solve():
    """Index: 3063.
    Returns: the number of more years Roger has to work before he retires.
    """
    # L1
    daughter_current_age = 19 # now she is 19 years old
    daughter_age_when_peter_joined = 7 # his daughter was 7 years old
    peter_experience = daughter_current_age - daughter_age_when_peter_joined

    # L2
    robert_less_than_peter = 4 # 4 years of experience less than Peter
    robert_experience = peter_experience - robert_less_than_peter

    # L3
    robert_more_than_mike = 2 # 2 more years of experience than Mike
    mike_experience = robert_experience - robert_more_than_mike

    # L4
    tom_multiplier = 2 # twice as many years of experience as Robert
    tom_experience = tom_multiplier * robert_experience

    # L5
    roger_experience = peter_experience + robert_experience + mike_experience + tom_experience

    # L6
    roger_retirement_target = 50 # 50 years of experience
    years_to_retirement = roger_retirement_target - roger_experience

    # FA
    answer = years_to_retirement
    return answer