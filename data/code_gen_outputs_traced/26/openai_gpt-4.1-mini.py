def solve(
    liters_seawater: float = 2,  # Jack collects 2 liters of seawater
    salt_percentage: float = 20   # water is 20% salt
):
    """Index: 26.
    Returns: the amount of salt in ml after evaporation of the seawater.
    """

    #: L1
    liters_salt = liters_seawater * salt_percentage * 0.01 # eval: 0.4 = 2 * 20 * 0.01

    #: L2
    ml_salt = liters_salt * 1000 # eval: 400.0 = 0.4 * 1000

    #: FA
    answer = ml_salt # eval: 400.0 = 400.0
    return answer # eval: return 400.0
