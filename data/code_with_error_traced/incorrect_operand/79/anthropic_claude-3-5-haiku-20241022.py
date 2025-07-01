def solve(
    james_years: int = 40,  # James spends 40 years teaching
    years_difference: int = 10  # His partner has been teaching for 10 years less
):
    """Index: 79.
    Returns: the combined teaching experience of James and his partner."""

    #: L1
    partner_years = james_years - years_difference # eval: 30 = 40 - 10

    #: L2
    combined_experience = years_difference + partner_years # eval: 40 = 10 + 30

    #: FA
    answer = combined_experience
    return answer # eval: return 40
