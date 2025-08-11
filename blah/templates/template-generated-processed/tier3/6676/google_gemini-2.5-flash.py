def solve():
    """Index: 6676.
    Returns: the number of artifacts in each artifact wing.
    """
    # L1
    two_other_wings = 2 # the other two wings
    smaller_paintings_per_wing = 12 # 12 smaller paintings each
    large_painting_wing = 1 # One painting is so large it takes up an entire wing
    total_paintings = two_other_wings * smaller_paintings_per_wing + large_painting_wing

    # L2
    artifact_multiplier = 4 # four times as many artifacts
    total_artifacts = total_paintings * artifact_multiplier

    # L3
    total_wings = 8 # eight different wings
    painting_wings = 3 # Three of the wings are dedicated to paintings
    artifact_wings = total_wings - painting_wings

    # L4
    artifacts_per_wing = total_artifacts / artifact_wings

    # FA
    answer = artifacts_per_wing
    return answer