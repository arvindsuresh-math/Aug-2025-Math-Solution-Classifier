def solve():
    """Index: 995.
    Returns: Anna's age when they got married.
    """
    # L1
    years_married_today = 30 # celebrating 30 years of marriage
    josh_age_at_marriage = 22 # Josh turned 22
    josh_current_age = years_married_today + josh_age_at_marriage

    # L2
    combined_age_multiplier = 5 # exactly 5 times what Josh's age was when they married
    combined_current_age = combined_age_multiplier * josh_age_at_marriage

    # L3
    anna_current_age = combined_current_age - josh_current_age

    # L4
    anna_age_at_marriage = anna_current_age - years_married_today

    # FA
    answer = anna_age_at_marriage
    return answer