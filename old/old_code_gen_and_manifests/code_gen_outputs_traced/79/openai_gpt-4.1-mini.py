def solve(
    james_years: int = 40,  # James spends 40 years teaching
    years_less_partner: int = 10  # His partner has been teaching for 10 years less
):
    """Index: 79.
    Returns: the combined years of teaching experience of James and his partner.
    """

    #: L1
    partner_years = james_years - years_less_partner # eval: 30 = 40 - 10

    #: L2
    combined_experience = james_years + partner_years # eval: 70 = 40 + 30

    #: FA
    answer = combined_experience
    return answer # eval: return 70
