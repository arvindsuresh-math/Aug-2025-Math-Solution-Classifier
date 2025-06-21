def solve(
    rise_rate: int = 50, # the balloon would rise at a rate of 50 feet per minute
    descend_rate: int = 10, # descend at a rate of 10 feet per minute
    first_rise_minutes: int = 15, # pulled the chain for 15 minutes
    first_descend_minutes: int = 10, # released the rope for 10 minutes
    second_rise_minutes: int = 15 # pulled the chain for another 15 minutes
):
    """Index: 5918.
    Returns: the highest elevation reached by the balloon during the ride."""
    #: L1
    first_rise = rise_rate * first_rise_minutes

    #: L2
    first_descend = descend_rate * first_descend_minutes

    #: L3
    second_rise = rise_rate * second_rise_minutes

    #: L4
    highest_elevation = first_rise - first_descend + second_rise # FINAL ANSWER
    return highest_elevation