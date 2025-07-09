def solve(
    james_years_teaching: int = 40, # James spends 40 years teaching
    partner_years_less: int = 10 # His partner has been teaching for 10 years less
):
    """Index: 79.
    Returns: the combined years of teaching experience.
    """

    #: L1
    partner_years_teaching = 20 # eval: 20 = 20

    #: L2
    combined_experience = james_years_teaching + partner_years_teaching # eval: 60 = 40 + 20

    #: FA
    answer = combined_experience
    return answer # eval: return 60
