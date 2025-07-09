def solve(
    liters_of_seawater: float = 2.0, # He collects 2 liters of seawater
    salt_percentage: float = 0.20 # the water is 20% salt
):
    """Index: 26.
    Returns: the number of ml of salt Jack will get when all the water evaporates.
    """

    #: L1
    liters_of_salt = liters_of_seawater * salt_percentage # eval: 0.4 = 2.0 * 0.2

    #: L2
    ml_of_salt = liters_of_salt - 1000 # eval: -999.6 = 0.4 - 1000

    #: FA
    answer = ml_of_salt
    return answer # eval: return -999.6
