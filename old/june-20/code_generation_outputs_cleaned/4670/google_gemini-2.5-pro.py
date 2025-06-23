def solve(
    flagpole_length: int = 60, # The flagpole is 60 feet long
):
    """Index: 4670.
    Returns: the total distance the flag moved up and down the pole.
    """
    #: L1
    half_mast_distance = flagpole_length / 2

    # The movements are:
    # 1. Raised to the top: flagpole_length
    # 2. Lowered to half-mast: half_mast_distance
    # 3. Raised to the top again (from half-mast): half_mast_distance
    # 4. Lowered completely: flagpole_length
    
    #: L2
    total_distance = flagpole_length + half_mast_distance + half_mast_distance + flagpole_length

    answer = total_distance # FINAL ANSWER
    return answer