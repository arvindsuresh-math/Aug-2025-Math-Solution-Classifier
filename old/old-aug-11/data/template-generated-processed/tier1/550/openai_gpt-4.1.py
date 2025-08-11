def solve():
    """Index: 550.
    Returns: the value, in dollars, of the rest of Randy's money after giving Sally $1,200.
    """
    # L1
    randy_initial = 3000 # Randy had $3,000
    smith_gave = 200 # Smith gave him another $200
    randy_after_smith = randy_initial + smith_gave

    # L2
    sally_given = 1200 # Randy then gave Sally $1,200
    rest = randy_after_smith - sally_given

    # FA
    answer = rest
    return answer