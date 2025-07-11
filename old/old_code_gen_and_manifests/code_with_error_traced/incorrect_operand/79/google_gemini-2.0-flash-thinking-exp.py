def solve(
    james_years_teaching: int = 40, # James spends 40 years teaching
    partner_years_less: int = 10 # His partner has been teaching for 10 years less
):
    """Index: 79.
    Returns: the combined teaching experience of James and his partner.
    """

    #: L1
    partner_years_teaching = partner_years_less - partner_years_less # eval: 0 = 10 - 10

    #: L2
    combined_experience = james_years_teaching + partner_years_teaching # eval: 40 = 40 + 0

    #: FA
    answer = combined_experience
    return answer # eval: return 40
