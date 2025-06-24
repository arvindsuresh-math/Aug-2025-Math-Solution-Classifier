def solve(
    total_people_consumed: int = 847,  # Over three hundred years, it has consumed 847 people
    num_periods: int = 3  # Monster rises once every hundred years over three hundred years
):
    """Index: 10.
    Returns: the number of people on the first ship the monster consumed."""
    
    #: L1
    # Let S be the number of people on the first hundred years' ship

    #: L2
    # The second hundred years' ship had twice as many as the first

    #: L3
    # The third hundred years' ship had twice as many as the second

    #: L4
    # Total people across all ships: S + 2S + 4S = 7S
    total_ship_multiplier = 1 + 2 + 4  # S + 2S + 4S

    #: L5
    # Solve for S by dividing total people by total ship multiplier
    people_on_first_ship = total_people_consumed / total_ship_multiplier

    answer = people_on_first_ship  # FINAL ANSWER
    return answer