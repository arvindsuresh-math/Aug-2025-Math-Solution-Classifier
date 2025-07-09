def solve(
    liters_seawater: float = 2,  # Jack collects 2 liters of seawater
    salt_percentage: float = 20   # water is 20% salt
):
    """Index: 26.
    Returns: the amount of salt in ml after evaporation of the seawater.
    """

    #: L1
    liters_salt = 1.4 # eval: 1.4 = 1.4

    #: L2
    ml_salt = liters_salt * 1000 # eval: 1400.0 = 1.4 * 1000

    #: FA
    answer = ml_salt
    return answer # eval: return 1400.0
