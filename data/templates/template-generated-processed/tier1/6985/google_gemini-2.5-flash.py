def solve():
    """Index: 6985.
    Returns: the total earnings of Andy before taxes during his shift.
    """
    # L1
    hours_worked = 8 # an 8-hour shift
    hourly_wage = 9 # $9 an hour
    wage_from_hours = hours_worked * hourly_wage

    # L2
    racquets_strung = 7 # strings 7 racquets
    restring_fee = 15 # $15 for each racquet he restrings
    earnings_from_stringing = racquets_strung * restring_fee

    # L3
    grommet_jobs = 2 # changes 2 sets of grommets
    grommet_fee = 10 # $10 for changing out the grommets
    earnings_from_grommets = grommet_jobs * grommet_fee

    # L4
    stencil_jobs = 5 # paints 5 stencils
    stencil_fee = 1 # $1 for painting a stencil
    earnings_from_stenciling = stencil_jobs * stencil_fee

    # L5
    total_earnings = wage_from_hours + earnings_from_stringing + earnings_from_grommets + earnings_from_stenciling

    # FA
    answer = total_earnings
    return answer