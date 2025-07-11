def solve():
    """Index: 475.
    Returns: the number of apples Layla picked.
    """
    # L1
    average_apples = 30 # averaged 30 apples picked
    num_people = 3 # The three averaged
    total_apples_expected = average_apples * num_people

    # L2
    maggie_apples = 40 # Maggie picked 40 apples
    kelsey_apples = 28 # Kelsey picked 28 apples
    apples_accounted_for = maggie_apples + kelsey_apples

    # L3
    layla_apples = total_apples_expected - apples_accounted_for

    # FA
    answer = layla_apples
    return answer